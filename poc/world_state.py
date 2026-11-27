"""Persistent shared world state -- the cohesion backbone across agents.

Each agent reads a compact text brief derived from this instead of relying
purely on its own conversation history, so facts stay consistent even as
individual agent contexts are small/rotate.

The world itself (characters, places, facts and how they relate) lives in a
typed graph (world_graph.WorldGraph). This class keeps the API the rest of
the code already used -- world.location, npc.location, present_npcs(),
add_fact()... -- on top of it. What is conversation state rather than world
(recent history, each NPC agent's thread, the pending refused action) stays
as plain fields.
"""
import json
import re
from datetime import datetime
from pathlib import Path

from world_graph import PLAYER_ID, WorldGraph


class NPC:
    """A character Kael can meet. Once added to a world, its values (name,
    persona, important, aliases) and its location are read from and written
    to its graph node; `thread` and `known_facts` are its agent's own state.
    Before that (just constructed) they are held locally."""

    _VALUES = ("name", "persona", "important", "aliases")

    def __init__(self, name: str, persona: str, important: bool = False,
                 known_facts=None, thread=None, location: str = "", aliases=None):
        self.known_facts = list(known_facts or [])
        self.thread = list(thread or [])  # this NPC's own message history
        self.id = ""          # graph node id, set by WorldState.add_npc
        self._world = None
        self._local = {"name": name, "persona": persona, "important": important,
                       "aliases": list(aliases or [])}
        # Where this NPC is. "" = whereabouts unknown (only mentioned so far).
        # An NPC is "present" when this equals WorldState.location.
        self._local_location = location

    def _values(self) -> dict:
        return self._world.graph.node(self.id) if self._world else self._local

    name = property(lambda self: self._values()["name"],
                    lambda self, v: self._values().__setitem__("name", v))
    persona = property(lambda self: self._values()["persona"],
                       lambda self, v: self._values().__setitem__("persona", v))
    important = property(lambda self: self._values()["important"],
                         lambda self, v: self._values().__setitem__("important", v))
    aliases = property(lambda self: self._values()["aliases"],
                       lambda self, v: self._values().__setitem__("aliases", list(v)))

    @property
    def location(self) -> str:
        if not self._world:
            return self._local_location
        return self._world.place_name(self._world.graph.target(self.id, "AT"))

    @location.setter
    def location(self, place: str):
        if not self._world:
            self._local_location = place
        else:
            self._world.put_at(self.id, place)

    def name_tokens(self) -> set:
        """Lower-case name parts long enough to match safely ("Grimbold",
        "Ironfist"), used to spot the player naming this NPC."""
        return {t for t in re.findall(r"[a-z]+", self.name.lower()) if len(t) >= 3}

    def __repr__(self):
        return f"NPC({self.id or 'unbound'} {self.name!r} @ {self.location!r})"


# The world clock (Day 4). Free-text year and month (the world's own
# calendar), a day number and a part of the day. It only moves forward, and
# only when the player or the narration says time passed
# (agents.time_passed). No month/year rollover yet (TO DO Day 5).
PARTS_OF_DAY = ["dawn", "morning", "midday", "afternoon", "evening", "night", "late night"]
DEFAULT_CLOCK = {"year": "Year 200", "month": "Frostmonth", "day": 14, "part": "evening"}


def _ordinal(n: int) -> str:
    suffix = "th" if 10 <= n % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")
    return f"{n}{suffix}"


class WorldState:
    def __init__(self, location: str = "", scene_summary: str = "", npcs=None,
                 flags=None, active_npc: str = "", recent_history=None,
                 places=None, pending_action: str = "", clock=None):
        self.clock = dict(clock or DEFAULT_CLOCK)
        self.graph = WorldGraph()
        self.graph.add_node("Character", node_id=PLAYER_ID, name="Kael", player=True)
        self.scene_summary = scene_summary
        self.npcs = {}  # name -> NPC (the graph holds their values)
        self.active_npc = active_npc  # name of the NPC the player is currently engaging
        self.recent_history = list(recent_history or [])  # [(player, dm_text), ...]
        # After a refused claim: the rest of the player's line (their own action),
        # waiting for "yes" before it is played. "" = nothing pending.
        self.pending_action = pending_action
        for p in places or []:
            self.move_to(p)
        if location:
            self.move_to(location)
        for npc in (npcs or {}).values():
            self.add_npc(npc)
        for f in flags or []:
            self.add_fact(f)

    # ---- places ----------------------------------------------------------
    def place_id(self, name: str, create: bool = True) -> str:
        """Id of the Place called `name` (made if new and create), or ""."""
        name = (name or "").strip()
        if not name:
            return ""
        pid = self.graph.find("Place", name)
        if not pid and create:
            pid = self.graph.add_node("Place", name=name)
        return pid

    def place_name(self, place_id: str) -> str:
        return self.graph.node(place_id)["name"] if place_id else ""

    def put_at(self, node_id: str, place: str):
        """Set where a character is; "" = whereabouts unknown."""
        pid = self.place_id(place)
        if pid:
            self.graph.add_edge(node_id, "AT", pid)
        else:
            self.graph.remove_edge(node_id, "AT")

    @property
    def location(self) -> str:
        return self.place_name(self.graph.target(PLAYER_ID, "AT"))

    @location.setter
    def location(self, place: str):
        self.move_to(place)

    @property
    def places(self) -> list:
        """Every location Kael has visited, in order of first visit."""
        visited = [p for p in self.graph.nodes("Place") if "visit" in self.graph.node(p)]
        visited.sort(key=lambda p: self.graph.node(p)["visit"])
        return [self.place_name(p) for p in visited]

    def move_to(self, new_location: str):
        """Move Kael, and everyone travelling with him, to new_location."""
        self.put_at(PLAYER_ID, new_location)
        pid = self.graph.target(PLAYER_ID, "AT")
        if pid and "visit" not in self.graph.node(pid):
            visits = [self.graph.node(p).get("visit", 0) for p in self.graph.nodes("Place")]
            self.graph.node(pid)["visit"] = max(visits) + 1
        for npc in self.party():
            npc.location = new_location

    def known_places(self) -> list:
        seen = []
        for p in self.places + [self.location] + [n.location for n in self.npcs.values()]:
            if p and p not in seen:
                seen.append(p)
        return seen

    # ---- characters --------------------------------------------------------
    def add_npc(self, npc: NPC):
        old = self.npcs.get(npc.name)
        if old is not None and old.id:
            self.graph.g.remove_node(old.id)
        values = dict(npc._local)
        location = npc._local_location
        npc.id = self.graph.add_node("Character", **values)
        npc._world = self
        npc.location = location
        self.npcs[npc.name] = npc

    # ---- the party: NPCs travelling with Kael ------------------------------
    def party(self) -> list:
        """NPCs with a TRAVELS_WITH edge to Kael: they follow every move
        until they are left behind."""
        ids = set(self.graph.sources(PLAYER_ID, "TRAVELS_WITH"))
        return [n for n in self.npcs.values() if n.id in ids]

    def join_party(self, name: str, by: str = ""):
        npc = self.npcs.get(name)
        if npc and npc.id:
            self.graph.add_edge(npc.id, "TRAVELS_WITH", PLAYER_ID, by=by)

    def leave_party(self, name: str):
        npc = self.npcs.get(name)
        if npc and npc.id:
            self.graph.remove_edge(npc.id, "TRAVELS_WITH", PLAYER_ID)

    def is_present(self, npc) -> bool:
        return bool(npc) and npc.location == self.location

    def present_npcs(self) -> list:
        return [n for n in self.npcs.values() if self.is_present(n)]

    def find_npc(self, name: str):
        """The known NPC this name refers to, matching on any shared name
        part ("Borgar" == "Borgar Ironvein"), or None."""
        tokens = {t for t in re.findall(r"[a-z]+", name.lower()) if len(t) >= 3}
        for npc in self.npcs.values():
            if tokens & npc.name_tokens():
                return npc
        return None

    # ---- facts -----------------------------------------------------------
    @property
    def flags(self) -> list:
        """Established facts, plain strings, in the order they were added."""
        return [self.graph.node(f)["text"] for f in self.graph.nodes("Fact")]

    def add_fact(self, fact: str):
        if fact not in self.flags:
            self.graph.add_node("Fact", text=fact)

    # ---- history -----------------------------------------------------------
    def add_turn(self, player_text, dm_text, keep_last=6, witnesses=None):
        """Record a played turn: in recent_history (the DM's view: it knows
        everything) and as an Event node KNOWN by Kael and every NPC that
        witnessed it (default: everyone here now). NPC agents only hear the
        events they witnessed (events_known_by), so a secret told to Tallow
        at the smithy no longer reaches Grimbold's prompt at the tavern."""
        self.recent_history.append((player_text, dm_text))
        self.recent_history = self.recent_history[-keep_last:]
        if witnesses is None:
            witnesses = [n.name for n in self.present_npcs()]
        eid = self.graph.add_node("Event", player=player_text, dm=dm_text,
                                  short=player_text[:40])
        here = self.graph.target(PLAYER_ID, "AT")
        if here:
            self.graph.add_edge(eid, "AT_PLACE", here)
        self.graph.add_edge(PLAYER_ID, "KNOWS", eid)
        for name in witnesses:
            npc = self.npcs.get(name)
            if npc and npc.id:
                self.graph.add_edge(npc.id, "KNOWS", eid)

    def events_known_by(self, npc, last: int = 2) -> list:
        """The last `last` exchanges (whole turns) this NPC witnessed, oldest
        first, as (player_text, dm_text)."""
        known = set(self.graph.targets(npc.id, "KNOWS")) if npc and npc.id else set()
        events = [e for e in self.graph.nodes("Event") if e in known and "player" in self.graph.node(e)]
        return [(self.graph.node(e)["player"], self.graph.node(e)["dm"]) for e in events[-last:]]

    # ---- the world clock ---------------------------------------------------
    def clock_text(self) -> str:
        c = self.clock
        return f"{c['year']}, {_ordinal(int(c['day']))} of {c['month']}, {c['part']}"

    def advance_clock(self, part: str = "", next_day: bool = False):
        """Move time forward to `part` of the day (the next day if that part
        is not later today, or if next_day)."""
        cur = PARTS_OF_DAY.index(self.clock["part"]) if self.clock["part"] in PARTS_OF_DAY else 0
        new = PARTS_OF_DAY.index(part) if part in PARTS_OF_DAY else (cur + 1) % len(PARTS_OF_DAY)
        if next_day or new <= cur:
            self.clock["day"] = int(self.clock["day"]) + 1
        self.clock["part"] = PARTS_OF_DAY[new]

    # ---- the timeline log ----------------------------------------------------
    def log(self, text: str, witnesses=(), place: str = None):
        """One timeline line, MMO-log style: what happened, stamped with the
        full in-game date and place (repeated on every line, so a line never
        depends on an earlier one), plus the real time as metadata. KNOWN by
        Kael and each witness (NPC names)."""
        place = self.location if place is None else place
        eid = self.graph.add_node("Event", text=text, clock=self.clock_text(), place=place,
                                  real_time=datetime.now().isoformat(timespec="seconds"),
                                  short=text[:40])
        pid = self.place_id(place, create=False)
        if pid:
            self.graph.add_edge(eid, "AT_PLACE", pid)
        self.graph.add_edge(PLAYER_ID, "KNOWS", eid)
        for name in witnesses:
            npc = self.npcs.get(name)
            if npc and npc.id:
                self.graph.add_edge(npc.id, "KNOWS", eid)
        return eid

    def timeline(self, viewer=None, last: int = 10) -> list:
        """The last `last` log lines, oldest first, as numbered text. viewer:
        an NPC -> only the lines they witnessed (None = everything, the DM)."""
        known = set(self.graph.targets(viewer.id, "KNOWS")) if viewer is not None else None
        lines = [e for e in self.graph.nodes("Event") if "text" in self.graph.node(e)
                 and (known is None or e in known)][-last:]
        return [f"{i}. [{self.graph.node(e)['clock']} | {self.graph.node(e)['place']}] "
                f"{self.graph.node(e)['text']}" for i, e in enumerate(lines, 1)]

    def scene_block(self) -> str:
        """Where things stand right now, as plain text for a prompt."""
        pid = self.graph.target(PLAYER_ID, "AT")
        situation = self.graph.node(pid).get("situation", "") if pid else ""
        lines = [f"Place: {self.location}" + (f" ({situation})" if situation else ""),
                 f"Time: {self.clock_text()}"]
        party = {n.name for n in self.party()}
        here = self.present_npcs()
        lines.append("Here: Kael" + "".join(
            f"; {n.name}{' (travelling with Kael)' if n.name in party else ''}: {n.persona}" for n in here))
        active = self.npcs.get(self.active_npc)
        if self.is_present(active):
            lines.append(f"Talking with: {active.name}")
        elsewhere = [n for n in self.npcs.values() if not self.is_present(n)]
        if elsewhere:
            lines.append("Not here: " + "; ".join(
                f"{n.name} ({n.location or 'whereabouts unknown'})" for n in elsewhere))
        return "\n".join(lines)

    def context_brief(self) -> str:
        lines = [f"LOCATION: {self.location}", f"SCENE: {self.scene_summary}"]
        here = self.present_npcs()
        elsewhere = [n for n in self.npcs.values() if not self.is_present(n)]
        if here:
            lines.append("CHARACTERS HERE:")
            for npc in here:
                lines.append(f"  - {npc.name}: {npc.persona}")
            party = [n.name for n in self.party() if self.is_present(n)]
            if party:
                lines.append(f"TRAVELLING WITH KAEL: {', '.join(party)}")
            active = self.npcs.get(self.active_npc)
            if self.is_present(active):
                lines.append(f"TALKING WITH: {active.name}")
        if elsewhere:
            lines.append("OTHER KNOWN CHARACTERS (NOT here right now):")
            for npc in elsewhere:
                where = f"last seen at {npc.location}" if npc.location else "whereabouts unknown"
                lines.append(f"  - {npc.name} ({where}): {npc.persona}")
        if self.flags:
            lines.append("ESTABLISHED FACTS:")
            for f in self.flags:
                lines.append(f"  - {f}")
        if self.recent_history:
            lines.append("RECENT HISTORY:")
            for player_text, dm_text in self.recent_history:
                lines.append(f"  Player: {player_text}")
                lines.append(f"  DM: {dm_text}")
        return "\n".join(lines)

    def dm_brief(self, timeline_lines: int = 10) -> str:
        """The DM's world context, built from the graph (Day 4): the story
        premise, established facts, a timeline log with the full date and
        place on every line, the last exchange verbatim (so dialogue flows),
        and the current scene LAST. Replaces the last 6 exchanges of raw
        narration, whose old scene details the DM kept carrying into new
        places ("the barrel of pickled herrings ... against the porch" on the
        ridge). The DM still knows everything; this only orders it."""
        lines = [f"STORY PREMISE: {self.scene_summary}"]
        if self.flags:
            lines.append("ESTABLISHED FACTS:")
            lines += [f"  - {f}" for f in self.flags]
        tl = self.timeline(last=timeline_lines)
        if tl:
            lines.append("TIMELINE (what happened so far, oldest first; each line has its own date and place):")
            lines += [f"  {t}" for t in tl]
        if self.recent_history:
            player_text, dm_text = self.recent_history[-1]
            lines.append("LAST EXCHANGE (verbatim):")
            lines.append(f"  Player: {player_text}")
            lines.append(f"  DM: {dm_text}")
        lines.append("CURRENT SCENE (this is where things stand RIGHT NOW):")
        lines += [f"  {x}" for x in self.scene_block().splitlines()]
        return "\n".join(lines)

    # ---- persistence -------------------------------------------------------
    def to_dict(self):
        return {
            "clock": self.clock,
            "graph": self.graph.to_dict(),
            "scene_summary": self.scene_summary,
            "active_npc": self.active_npc,
            "recent_history": [list(t) for t in self.recent_history],
            "pending_action": self.pending_action,
            # Conversation state per NPC; their world values are in the graph.
            "npcs": {name: {"id": n.id, "thread": n.thread, "known_facts": n.known_facts}
                     for name, n in self.npcs.items()},
        }

    @classmethod
    def from_dict(cls, d):
        if "graph" not in d:
            return cls._from_legacy_dict(d)
        world = cls(scene_summary=d.get("scene_summary", ""),
                    active_npc=d.get("active_npc", ""),
                    recent_history=[tuple(x) for x in d.get("recent_history", [])],
                    pending_action=d.get("pending_action", ""), clock=d.get("clock"))
        world.graph = WorldGraph.from_dict(d["graph"])
        for name, data in d.get("npcs", {}).items():
            npc = NPC(name=name, persona="", known_facts=data.get("known_facts"),
                      thread=data.get("thread"))
            npc.id, npc._world = data["id"], world
            world.npcs[name] = npc
        if not world.graph.nodes("Event"):
            world._history_known_by_all()
        return world

    def _history_known_by_all(self):
        """Saves from before Events: nobody recorded who saw what, so every
        NPC knows the stored history (what NPC agents were shown before)."""
        for player_text, dm_text in self.recent_history:
            eid = self.graph.add_node("Event", player=player_text, dm=dm_text,
                                      short=player_text[:40])
            for who in [PLAYER_ID] + [n.id for n in self.npcs.values()]:
                self.graph.add_edge(who, "KNOWS", eid)

    @classmethod
    def _from_legacy_dict(cls, d):
        """Saves from before the graph: flat strings for locations and facts."""
        d = dict(d)
        location = d.get("location", "")
        npcs = {}
        for name, data in d.get("npcs", {}).items():
            data = dict(data)
            # Saves from before NPCs had a location: assume they are where the
            # player is, which is what the old code implicitly assumed.
            data.setdefault("location", location)
            npcs[name] = NPC(**data)
        world = cls(scene_summary=d.get("scene_summary", ""), npcs=npcs,
                    flags=d.get("flags", []), active_npc=d.get("active_npc", ""),
                    recent_history=[tuple(x) for x in d.get("recent_history", [])],
                    places=d.get("places") or ([location] if location else []),
                    location=location, pending_action=d.get("pending_action", ""))
        if not location:
            world.graph.remove_edge(PLAYER_ID, "AT")
        world._history_known_by_all()
        return world

    def save(self, path: Path):
        Path(path).write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path):
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
