from ._concrete_sudoku_validators import (
    BlockSudokuValidator,
    ColumnSudokuValidator,
    RowSudokuValidator,
)
from .sudoku_validator import SudokuValidator


def create_sudoku_validator() -> SudokuValidator:
    row_validator = RowSudokuValidator()
    column_validator = ColumnSudokuValidator()
    block_validator = BlockSudokuValidator()

    column_validator.set_successor(successor=block_validator)
    row_validator.set_successor(successor=column_validator)

    return row_validator
