from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

DEFAULT_DEPTH_LIMIT = 50


class DFS(BaseSearch):

    def __init__(self, depth_limit: int = DEFAULT_DEPTH_LIMIT):
        self.depth_limit = depth_limit

    def search(self, initial: State) -> SearchResult:

        stack: list[tuple[State, frozenset]] = [(initial, frozenset())]

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier = 1

        while stack:
            node, ancestors = stack.pop()

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier,
                    depth=node.cost,
                )

            if node.cost >= self.depth_limit or node.tiles in ancestors:
                continue

            nodes_expanded += 1
            new_ancestors = ancestors | {node.tiles}

            for child in reversed(node.neighbors()):
                nodes_generated += 1
                stack.append((child, new_ancestors))

            max_frontier = max(max_frontier, len(stack))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier,
        )
