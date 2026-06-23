from collections import deque
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult


class BFS(BaseSearch):

    def search(self, initial: State) -> SearchResult:
        if initial.is_goal:
            return SearchResult(solution=initial)

        frontier: deque[State] = deque([initial])
        visited: set[tuple] = {initial.tiles}

        nodes_expanded = 0
        nodes_generated = 1          
        max_frontier = 1

        while frontier:
            node = frontier.popleft()
            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1

                if child.is_goal:
                    return SearchResult(
                        solution=child,
                        nodes_expanded=nodes_expanded,
                        nodes_generated=nodes_generated,
                        max_frontier_size=max_frontier,
                        depth=child.cost,
                    )

                if child.tiles not in visited:
                    visited.add(child.tiles)
                    frontier.append(child)

            max_frontier = max(max_frontier, len(frontier))

        # Sem solução
        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier,
        )
