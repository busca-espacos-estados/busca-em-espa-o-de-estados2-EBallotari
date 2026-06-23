from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional
from puzzle.state import State


@dataclass
class SearchResult:
    """Resultado padronizado retornado por qualquer algoritmo de busca."""

    solution: Optional[State]           
    nodes_expanded: int = 0             
    nodes_generated: int = 0            
    max_frontier_size: int = 0         
    depth: int = 0                      

    @property
    def found(self) -> bool:
        return self.solution is not None

    @property
    def actions(self) -> List[str]:
        return self.solution.actions() if self.found else []

    @property
    def path_cost(self) -> int:
        return self.solution.cost if self.found else -1
