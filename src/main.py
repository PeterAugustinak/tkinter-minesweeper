from tkinter import *

import settings
import utils


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

# run the window
root.mainloop()
