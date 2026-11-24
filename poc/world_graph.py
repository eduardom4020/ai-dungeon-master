"""The world as a typed graph: nodes with ids and values, edges between ids.

Nodes have short opaque ids made by code (C0, C1, P1, F3, ...) and a value
dict (name, short label, description...). Edges only ever hold ids, with the
relation as the edge key, so there is at most one edge per (from, to,
relation). Names never appear in an edge: a character can be renamed or get
a long title without touching any relationship.

The schema is fixed here. LLMs never see or write ids: they see names in the
rendered briefs, and code turns names back into ids with find().

networkx does not enforce any of this; every write goes through WorldGraph.
"""
import networkx as nx

# Node type -> id prefix.
NODE_TYPES = {"Character": "C", "Place": "P", "Item": "I", "Fact": "F"}

# Relation -> allowed (from type, to type) pairs.
EDGE_TYPES = {
    "AT": {("Character", "Place"), ("Item", "Place")},
    "PART_OF": {("Place", "Place")},
    "CONNECTED_TO": {("Place", "Place")},
    "TRAVELS_WITH": {("Character", "Character")},
    "HAS": {("Character", "Item")},
    "KNOWS": {("Character", "Fact"), ("Character", "Character")},
    "ABOUT": {("Fact", t) for t in NODE_TYPES},
}

# Relations a node can have at most one of, going out (a character is in
# one place at a time). add_edge() replaces the old one.
SINGLE_OUT = {"AT", "PART_OF"}

PLAYER_ID = "C0"


class WorldGraph:
    def __init__(self):
        self.g = nx.MultiDiGraph()
        self.counters = {prefix: 0 for prefix in NODE_TYPES.values()}

    # ---- nodes -----------------------------------------------------------
    def add_node(self, type_: str, node_id: str = "", **values) -> str:
        if type_ not in NODE_TYPES:
            raise ValueError(f"unknown node type {type_!r}")
        if not node_id:
            prefix = NODE_TYPES[type_]
            self.counters[prefix] += 1
            node_id = f"{prefix}{self.counters[prefix]}"
        if node_id in self.g:
            raise ValueError(f"node {node_id} already exists")
        self.g.add_node(node_id, type=type_, **values)
        return node_id

    def node(self, node_id: str) -> dict:
        """The node's value dict (live: changes to it are stored)."""
        return self.g.nodes[node_id]

    def type_of(self, node_id: str) -> str:
        return self.g.nodes[node_id]["type"]

    def nodes(self, type_: str = "") -> list:
        """Ids of all nodes (of one type), in creation order."""
        return [n for n, d in self.g.nodes(data=True) if not type_ or d["type"] == type_]

    def find(self, type_: str, label: str) -> str:
        """Id of the node of this type whose name, short label or an alias is
        exactly `label` (case-insensitive), or "". Exact on purpose: fuzzy
        name matching stays with the callers that already do it."""
        key = label.strip().lower()
        if not key:
            return ""
        for n in self.nodes(type_):
            d = self.g.nodes[n]
            labels = [d.get("name", ""), d.get("short", "")] + list(d.get("aliases", []))
            if key in (x.strip().lower() for x in labels if x):
                return n
        return ""

    def label(self, node_id: str) -> str:
        d = self.g.nodes[node_id]
        return d.get("short") or d.get("name") or d.get("text", "")[:40] or node_id

    # ---- edges -----------------------------------------------------------
    def add_edge(self, src: str, rel: str, dst: str, **provenance):
        """src -rel-> dst. provenance: by="tracker"/"player"/..., turn=N."""
        pair = (self.type_of(src), self.type_of(dst))
        if pair not in EDGE_TYPES.get(rel, set()):
            raise ValueError(f"{rel} not allowed from {pair[0]} to {pair[1]}")
        if rel in SINGLE_OUT:
            for old in self.targets(src, rel):
                self.g.remove_edge(src, old, key=rel)
        self.g.add_edge(src, dst, key=rel, **provenance)

    def remove_edge(self, src: str, rel: str, dst: str = ""):
        """Remove src -rel-> dst, or every src -rel-> * when dst is empty."""
        for old in ([dst] if dst else self.targets(src, rel)):
            if self.g.has_edge(src, old, key=rel):
                self.g.remove_edge(src, old, key=rel)

    def targets(self, src: str, rel: str) -> list:
        return [v for _, v, k in self.g.out_edges(src, keys=True) if k == rel]

    def sources(self, dst: str, rel: str) -> list:
        return [u for u, _, k in self.g.in_edges(dst, keys=True) if k == rel]

    def target(self, src: str, rel: str) -> str:
        t = self.targets(src, rel)
        return t[0] if t else ""

    # ---- debugging -------------------------------------------------------
    def describe(self) -> str:
        """Readable dump: nodes by id, then edges as `C2 Vexin -AT-> P1 ...`."""
        lines = [f"{n} [{d['type']}] {self.label(n)}" for n, d in self.g.nodes(data=True)]
        for u, v, k in self.g.edges(keys=True):
            lines.append(f"{u} {self.label(u)} -{k}-> {v} {self.label(v)}")
        return "\n".join(lines)

    # ---- persistence -----------------------------------------------------
    def to_dict(self) -> dict:
        return {"counters": dict(self.counters),
                "data": nx.node_link_data(self.g, edges="edges")}

    @classmethod
    def from_dict(cls, d: dict) -> "WorldGraph":
        wg = cls()
        wg.g = nx.node_link_graph(d["data"], edges="edges", directed=True, multigraph=True)
        wg.counters.update(d.get("counters", {}))
        return wg
