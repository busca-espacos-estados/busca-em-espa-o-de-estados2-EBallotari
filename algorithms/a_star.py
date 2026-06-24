import heapq
from puzzle.base_search import BaseSearch
from puzzle.state import State
from puzzle.result import SearchResult

_GOAL_POS = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1), 0: (2, 2), 
}


class AStar(BaseSearch):

    def heuristic(self, state: State) -> int:
        """Distância de Manhattan — heurística admissível e consistente."""
        total = 0
        for idx, value in enumerate(state.tiles):
            if value == 0:
                continue  
            cur_row, cur_col = divmod(idx, 3)
            goal_row, goal_col = _GOAL_POS[value]
            total += abs(cur_row - goal_row) + abs(cur_col - goal_col)
        return total

    def search(self, initial: State) -> SearchResult:

        counter = 0
        h0 = self.heuristic(initial)
        heap: list[tuple[int, int, State]] = [(h0, counter, initial)]

        g_cost: dict[tuple, int] = {initial.tiles: 0}

        nodes_expanded = 0
        nodes_generated = 1
        max_frontier = 1

        while heap:
            f, _, node = heapq.heappop(heap)

            if node.is_goal:
                return SearchResult(
                    solution=node,
                    nodes_expanded=nodes_expanded,
                    nodes_generated=nodes_generated,
                    max_frontier_size=max_frontier,
                    depth=node.cost,
                )

            if node.cost > g_cost.get(node.tiles, float("inf")):
                continue

            nodes_expanded += 1

            for child in node.neighbors():
                nodes_generated += 1
                g = child.cost  

                if g < g_cost.get(child.tiles, float("inf")):
                    g_cost[child.tiles] = g
                    h = self.heuristic(child)
                    counter += 1
                    heapq.heappush(heap, (g + h, counter, child))

            max_frontier = max(max_frontier, len(heap))

        return SearchResult(
            solution=None,
            nodes_expanded=nodes_expanded,
            nodes_generated=nodes_generated,
            max_frontier_size=max_frontier,
        )
