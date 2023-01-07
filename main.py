from tkinter import *
import settings
import utilities
from cell import cell

root = Tk()  # starting point for window
root.configure(bg='black')  # bg color of window
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')  # size of gaming window
root.title("Minesweeper Game")  # title of gaming window
root.resizable(False, False)  # can't change the size of gaming window
top_frame = Frame(  # make frame
    root,
    bg='black',
    width=settings.WIDTH,
    height=utilities.height_prct(25)
)
top_frame.place(x=0, y=0)  # where to place that frame

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utilities.width_prct(25),
    y=0
)

left_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(25),
    height=utilities.height_prct(75)
)
left_frame.place(x=0, y=utilities.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_prct(75),
    height=utilities.height_prct(75)
)
center_frame.place(x=utilities.width_prct(25), y=utilities.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = cell(x, y)
        c1.create_button_object(center_frame)
        c1.cell_button_object.grid(
            column=y, row=x
        )

# call label from the cell class
cell.create_cell_count_label(left_frame)
cell.cell_count_label_object.place(
    x=0, y=0
)

cell.randomize_mine()

root.mainloop()  # ending point of window
