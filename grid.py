from dataclasses import dataclass
from typing import List

Grid = List[List[int]]


@dataclass(frozen=True)
class Position:
    col: int
    row: int
