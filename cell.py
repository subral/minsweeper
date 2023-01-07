import sys
from tkinter import Button, Label
import random
import settings
import ctypes


class cell:
    all = []
    cell_count = settings.CELL_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opend = False
        self.is_mine_candidate = False
        self.cell_button_object = None
        self.x = x
        self.y = y

        # append the object to the cell.all list
        cell.all.append(self)

    def create_button_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,

        )
        btn.bind('<Button-1>', self.left_check_action)  # <Button-1> = right click
        btn.bind('<Button-3>', self.right_check_action)  # <Buttton-3> = left click
        self.cell_button_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f'Cells Left:{cell.cell_count}',
            font=("", 30)
        )
        cell.cell_count_label_object = lbl

    def left_check_action(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cell_mine_length == 0:
                for ce in self.surrounded_cell:
                    ce.show_cell()
            self.show_cell()
            if cell.cell_count == settings.MINE_SIZE:
                ctypes.windll.user32.MessageBoxW(0, 'you won the game', 'Winnig message', 0)
        self.cell_button_object.unbind('<Button-1>')
        self.cell_button_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for c in cell.all:
            if c.x == x and c.y == y:
                return c

    @property
    def surrounded_cell(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    def show_cell(self):
        if not self.is_opend:
            cell.cell_count -= 1
            self.cell_button_object.configure(text=self.surrounded_cell_mine_length)
            # change the cell count of text
            if cell.cell_count_label_object:
                cell.cell_count_label_object.configure(
                    text=f'Cells Left:{cell.cell_count}'
                )
                self.cell_button_object.configure(
                    bg='SystemButtonFace'
                )
        self.is_opend = True

    @property
    def surrounded_cell_mine_length(self):
        counter = 0
        for c in self.surrounded_cell:
            if c.is_mine:
                counter += 1
        return counter

    def show_mine(self):
        self.cell_button_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'you clicked on a mine', 'you loos', 0)
        sys.exit()

    def right_check_action(self, event):
        if not self.is_mine_candidate:
            self.cell_button_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_button_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mine():
        picked_cell = random.sample(
            cell.all, settings.MINE_SIZE
        )
        for pick in picked_cell:
            pick.is_mine = True

    def __repr__(self):
        return f"cell({self.x}, {self.y})"
