from typing import List


def create_horizontal_bar() -> str:
    return "#" * 25 + "\n"


def print_grid(grid: List[List[int]]) -> None:
    ascii_grid = ""
    for row_idx, row in enumerate(grid):
        if row_idx % 3 == 0:
            ascii_grid += create_horizontal_bar()

        cells_in_row = "#"
        for col_idx, cell in enumerate(row):
            cells_in_row += " "
            cells_in_row += str(cell) if cell != 0 else " "
            if col_idx % 3 == 2:
                cells_in_row += " #"
        cells_in_row += "\n"
        ascii_grid += cells_in_row
    ascii_grid += create_horizontal_bar()
    print(ascii_grid)
