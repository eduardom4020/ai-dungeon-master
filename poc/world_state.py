"""Persistent shared world state -- the cohesion backbone across agents.

Each agent reads a compact text brief derived from this instead of relying
purely on its own conversation history, so facts stay consistent even as
individual agent contexts are small/rotate.
"""
import json
import re
from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class NPC:
    name: str
    persona: str
    important: bool = False
    known_facts: list = field(default_factory=list)
    thread: list = field(default_factory=list)  # this NPC's own message history
    # Where this NPC is. "" = whereabouts unknown (only mentioned so far).
    # An NPC is "present" when this equals WorldState.location.
    location: str = ""
    # Ways the player may refer to them without the name ("the dwarf").
    aliases: list = field(default_factory=list)

    def name_tokens(self) -> set:
        """Lower-case name parts long enough to match safely ("Grimbold",
        "Ironfist"), used to spot the player naming this NPC."""
        return {t for t in re.findall(r"[a-z]+", self.name.lower()) if len(t) >= 3}


@dataclass
class WorldState:
    location: str = ""
    scene_summary: str = ""
    npcs: dict = field(default_factory=dict)  # name -> NPC
    flags: list = field(default_factory=list)  # established facts, plain strings
    active_npc: str = ""  # name of the NPC the player is currently engaging
    recent_history: list = field(default_factory=list)  # [(player, dm_text), ...]
    places: list = field(default_factory=list)  # every location visited, in order
    # After a refused claim: the rest of the player's line (their own action),
    # waiting for "yes" before it is played. "" = nothing pending.
    pending_action: str = ""

    def add_npc(self, npc: NPC):
        self.npcs[npc.name] = npc

    def add_fact(self, fact: str):
        if fact not in self.flags:
            self.flags.append(fact)

    def add_turn(self, player_text, dm_text, keep_last=6):
        self.recent_history.append((player_text, dm_text))
        self.recent_history = self.recent_history[-keep_last:]

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

    def known_places(self) -> list:
        seen = []
        for p in self.places + [self.location] + [n.location for n in self.npcs.values()]:
            if p and p not in seen:
                seen.append(p)
        return seen

    def move_to(self, new_location: str):
        self.location = new_location
        if new_location not in self.places:
            self.places.append(new_location)

    def context_brief(self) -> str:
        lines = [f"LOCATION: {self.location}", f"SCENE: {self.scene_summary}"]
        here = self.present_npcs()
        elsewhere = [n for n in self.npcs.values() if not self.is_present(n)]
        if here:
            lines.append("CHARACTERS HERE:")
            for npc in here:
                lines.append(f"  - {npc.name}: {npc.persona}")
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

    def to_dict(self):
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, d):
        d = dict(d)
        npcs = {}
        for name, data in d.get("npcs", {}).items():
            data = dict(data)
            # Saves from before NPCs had a location: assume they are where the
            # player is, which is what the old code implicitly assumed.
            data.setdefault("location", d.get("location", ""))
            npcs[name] = NPC(**data)
        d["npcs"] = npcs
        d["recent_history"] = [tuple(x) for x in d.get("recent_history", [])]
        d.setdefault("places", [d.get("location", "")] if d.get("location") else [])
        return cls(**d)

    def save(self, path: Path):
        Path(path).write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path):
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
