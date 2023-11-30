from __future__ import annotations

import heapq
from abc import ABC, abstractmethod


class Node(ABC):
    parent: Node | None
    parent_edge: Edge | None
    accumulated_cost: int

    def __init__(self, accumulated_cost=0, parent=None, parent_edge=None):
        self.parent = parent
        self.accumulated_cost = accumulated_cost
        self.parent_edge = parent_edge


    @abstractmethod
    def neighbor_edges(self) -> [(Edge, Node)]: ...
    @abstractmethod
    def heuristic(self) -> int: ...
    @abstractmethod
    # return the fields that should be hashed from the subclass
    # fields that are important to the algorithm working should
    # be hashed, but as few as possible for speed
    def hash(self): ...

    @abstractmethod
    # returns whether a node is a goal node
    def is_goal(self) -> bool: ...

    def __hash__(self):
        return hash((self.hash(), self.parent))

    def __gt__(self, other: Node):
        return self.accumulated_cost > other.accumulated_cost


class Edge(ABC):
    def cost(self) -> int: ...


def astar(initial: Node) -> [Edge]:
    q: [Node] = []
    had: set[Node] = set()

    heapq.heappush(q, initial)

    while q:
        curr: Node = heapq.heappop(q)
        if curr in had:
            continue
        had.add(curr)

        if curr.is_goal():
            path = [curr.parent_edge]
            while (curr := curr.parent) is not None:
                path.append(curr.parent_edge)
            # reverse path
            return path[::-1]

        for (edge, node) in curr.neighbor_edges():
            if node not in had:
                heapq.heappush(q, Node(
                    accumulated_cost=curr.accumulated_cost + edge.cost(),
                    parent=curr,
                    parent_edge=edge,
                ))



