import sys

from random import sample
from tkinter import Button, Label, messagebox

import settings


class Cell:

    GRID = []  # lst with all cells
    CELL_COUNT = settings.CELL_COUNT
    CELL_COUNT_LABEL_OBJ = None
    DEFAULT_CELL_COLOR = "gray"

    def __init__(self, tag, row, col, is_mine=False):
        self.tag = tag
        self.row = row
        self.col = col
        self.is_mine = is_mine
        self.is_open = False
        self.is_mine_candidate = False
        self.cell_btn_object = None

        Cell.GRID.append(self)

    def __str__(self):
        return f'cell #{self.tag}'


    def __repr__(self):
        return f'c{self.tag} {self.row, self.col}: {self.is_mine}'

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=10,
            height=4,
            bg=self.DEFAULT_CELL_COLOR
            # text=self.tag
        )

        btn.bind('<Button-1>', self._left_click_actions)  # left mouse btn
        btn.bind('<Button-3>', self._right_click_actions) # right mouse btn

        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='white',
            fg='black',
            text=f"CELLS LEFT: {Cell.CELL_COUNT}",
            width=12,
            height=4,
            font=("Verdana", 8)

        )

        Cell.CELL_COUNT_LABEL_OBJ = lbl


    def _left_click_actions(self, event):

        print(f'{self.tag} - {self.is_mine} - {self.surrounding_cells}')
        print(self.surrounding_mines_count)

        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
            if self.surrounding_mines_count == 0:
                for cell in self.surrounding_cells:
                    cell.show_cell()


    def show_mine(self):
        # interrupt the game as mine was hit
        self.cell_btn_object.configure(bg='red', text='MINE!')
        message = messagebox.askquestion(
            'GAME OVER',
            'You hit the mine :(\nPlay again?',
        )

        if message == 'yes':
            pass
        else:
            sys.exit()

    def show_cell(self):
        if not self.is_open:
            self.cell_btn_object.configure(
                text=self.surrounding_mines_count,
                bg=self.DEFAULT_CELL_COLOR
            )

            # replace the text of cells left to actual one
            Cell.CELL_COUNT -= 1
            if Cell.CELL_COUNT_LABEL_OBJ:
                Cell.CELL_COUNT_LABEL_OBJ.configure(
                    text=f"CELLS LEFT: {Cell.CELL_COUNT}"
                )

        self.is_open = True

    @property
    def surrounding_cells(self):
        cells = [
            self.get_cell_by_axis(self.col - 1, self.row -1),
            self.get_cell_by_axis(self.col - 1, self.row),
            self.get_cell_by_axis(self.col - 1, self.row + 1),
            self.get_cell_by_axis(self.col, self.row - 1),
            self.get_cell_by_axis(self.col, self.row + 1),
            self.get_cell_by_axis(self.col + 1, self.row - 1),
            self.get_cell_by_axis(self.col + 1, self.row),
            self.get_cell_by_axis(self.col + 1, self.row + 1),
        ]

        return [cell for cell in cells if cell]

    def get_cell_by_axis(self, col, row):
        # return cell based on row and col
        for cell in Cell.GRID:
            if cell.col == col and cell.row == row:
                return cell

    @property
    def surrounding_mines_count(self):
        mines_count = 0
        for cell in self.surrounding_cells:
            if cell.is_mine:
                mines_count += 1

        return mines_count


    def _right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
            print(f"Cell {self.tag} marked as mine candidate")
        else:
            self.cell_btn_object.configure(
                bg=self.DEFAULT_CELL_COLOR
            )
            self.is_mine_candidate = False
            print(f"Cell {self.tag} unmarked as mine candidate")


    @staticmethod
    def randomize_mines():
        mines = sample(Cell.GRID, settings.MINES_COUNT)
        for cell in mines:
            cell.is_mine = True
