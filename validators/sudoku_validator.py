from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional

from grid import Grid, Position


class SudokuValidator(ABC):
    def __init__(self) -> None:
        self._successor: Optional[SudokuValidator] = None

    def set_successor(self, successor: SudokuValidator) -> None:
        self._successor = successor

    @abstractmethod
    def is_placement_valid(self, grid: Grid, pos: Position, val: int) -> bool:
        pass
