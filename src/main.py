from tkinter import Tk, Frame, Label

import settings
import utils
from cell import Cell


# create non-resizable screen with grey background and title
root = Tk()
root.configure(bg='grey')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('MINESWEEPER')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_percent(20),
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='gray',
    text='MINESWEEPER GAME',
    font=('Verdana', 30)
)

game_title.place(
    x=utils.width_percent(25),
    y=10
)


left_frame = Frame(
    root,
    bg='white',
    width=utils.width_percent(20),
    height=utils.height_percent(80),
)
left_frame.place(x=0, y=utils.height_percent(20))


center_frame = Frame(
    root,
    bg='green',
    width=utils.width_percent(80),
    height=utils.height_percent(80),
)
center_frame.place(x=utils.width_percent(20), y=utils.height_percent(20))

# demo how grid work
# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(column=0, row=0)

# create grid of cells by looping
cell_number = 1
for column in range(settings.GRID_SIZE):
    for row in range(settings.GRID_SIZE):
        cell = Cell(
            str(cell_number if cell_number > 9 else f'0{cell_number}'),
            column,
            row,
        )

        cell.create_btn_object(center_frame)
        cell.cell_btn_object.grid(column=column, row=row)
        cell_number += 1


Cell.create_cell_count_label(left_frame)
Cell.CELL_COUNT_LABEL_OBJ.place(x=5, y=5)

Cell.randomize_mines()

# run the window
root.mainloop()
