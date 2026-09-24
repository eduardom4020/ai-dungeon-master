"""Persistent shared world state -- the cohesion backbone across agents.

Each agent reads a compact text brief derived from this instead of relying
purely on its own conversation history, so facts stay consistent even as
individual agent contexts are small/rotate.
"""
import json
from dataclasses import dataclass, field, asdict
from pathlib import Path


@dataclass
class NPC:
    name: str
    persona: str
    important: bool = False
    known_facts: list = field(default_factory=list)
    thread: list = field(default_factory=list)  # this NPC's own message history


@dataclass
class WorldState:
    location: str = ""
    scene_summary: str = ""
    npcs: dict = field(default_factory=dict)  # name -> NPC
    flags: list = field(default_factory=list)  # established facts, plain strings
    active_npc: str = ""  # name of NPC currently in the scene, if any
    recent_history: list = field(default_factory=list)  # [(player, dm_text), ...]

    def add_npc(self, npc: NPC):
        self.npcs[npc.name] = npc

    def add_fact(self, fact: str):
        if fact not in self.flags:
            self.flags.append(fact)

    def add_turn(self, player_text, dm_text, keep_last=6):
        self.recent_history.append((player_text, dm_text))
        self.recent_history = self.recent_history[-keep_last:]

    def context_brief(self) -> str:
        lines = [f"LOCATION: {self.location}", f"SCENE: {self.scene_summary}"]
        if self.npcs:
            lines.append("KNOWN NPCS:")
            for npc in self.npcs.values():
                lines.append(f"  - {npc.name}: {npc.persona}")
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
        npcs = {name: NPC(**data) for name, data in d.get("npcs", {}).items()}
        d = dict(d)
        d["npcs"] = npcs
        d["recent_history"] = [tuple(x) for x in d.get("recent_history", [])]
        return cls(**d)

    def save(self, path: Path):
        Path(path).write_text(json.dumps(self.to_dict(), indent=2), encoding="utf-8")

    @classmethod
    def load(cls, path: Path):
        return cls.from_dict(json.loads(Path(path).read_text(encoding="utf-8")))
