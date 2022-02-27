from copy import deepcopy

from grid import Grid, Position
from validators import SudokuValidator


class SudokuSolver:
    def __init__(self, grid: Grid, validator: SudokuValidator) -> None:
        self.__grid = deepcopy(grid)
        self.__solution_found = False
        self.__validator = validator

    def solve(self) -> Grid:
        self.__internal_solve()
        return self.__grid

    def __internal_solve(self) -> None:
        for row_idx, row in enumerate(self.__grid):
            for col_idx, cell in enumerate(row):
                if cell != 0:
                    continue
                for possible_val in range(1, 10):
                    if self.__validator.is_placement_valid(
                        grid=self.__grid,
                        pos=Position(col=col_idx, row=row_idx),
                        val=possible_val,
                    ):
                        self.__grid[row_idx][col_idx] = possible_val
                        self.__internal_solve()
                        if self.__solution_found:
                            return
                        self.__grid[row_idx][col_idx] = 0
                return

        self.__solution_found = True
