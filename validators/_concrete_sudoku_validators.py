from grid import Grid, Position

from .sudoku_validator import SudokuValidator


class RowSudokuValidator(SudokuValidator):
    def is_placement_valid(self, grid: Grid, pos: Position, val: int) -> bool:
        if val in grid[pos.row]:
            return False

        if self._successor is None:
            return True

        return self._successor.is_placement_valid(grid=grid, pos=pos, val=val)


class ColumnSudokuValidator(SudokuValidator):
    def is_placement_valid(self, grid: Grid, pos: Position, val: int) -> bool:
        for row in grid:
            if val == row[pos.col]:
                return False

        if self._successor is None:
            return True

        return self._successor.is_placement_valid(grid=grid, pos=pos, val=val)


class BlockSudokuValidator(SudokuValidator):
    def is_placement_valid(self, grid: Grid, pos: Position, val: int) -> bool:
        block_row = pos.row // 3 * 3
        block_col = pos.col // 3 * 3

        for y in range(3):
            for x in range(3):
                if val == grid[block_row + y][block_col + x]:
                    return False

        if self._successor is None:
            return True

        return self._successor.is_placement_valid(grid=grid, pos=pos, val=val)
