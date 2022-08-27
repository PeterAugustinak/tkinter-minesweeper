from random import sample
from tkinter import Button

import settings


class Cell:

    GRID = []  # lst with all cells

    def __init__(self, tag, row, col, is_mine=False):
        self.tag = tag
        self.row = row
        self.col = col
        self.is_mine = is_mine
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
            # text=self.tag,
        )

        btn.bind(
            '<Button-1>',  # <Button-1> -> left click
            self._left_click_actions
        )

        btn.bind(
            '<Button-3>',  # <Button-3> -> right click
            self._right_click_actions
        )

        self.cell_btn_object = btn

    def _left_click_actions(self, event):
        print(
            f"Button {self.tag} {[self.row, self.col]} "
            f"left-clicked! (info: {event}")

        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def show_mine(self):
        # interrupt the game as mine was hit
        self.cell_btn_object.configure(bg='red')

    def show_cell(self):
        pass

    def get_cell_by_axis(self, row, col):
        # return cell based on row and col
        for cell in Cell.GRID:
            if cell.row == row and cell.col == col:
                return cell


    def _right_click_actions(self, event):
        print(f"Button {self.tag} right-clicked! (info: {event}")

    @staticmethod
    def randomize_mines():
        mines = sample(Cell.GRID, settings.MINES_COUNT)
        for cell in mines:
            cell.is_mine = True
