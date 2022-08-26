from tkinter import Button


class Cell:

    def __init__(self, tag, is_mine=False):
        self.tag = tag
        self.is_mine = is_mine
        self.cell_btn_object = None


    def create_btn_object(self, locaton):
        btn = Button(
            locaton,
            width=12,
            height=4,
            text=self.tag,
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
        print(f"Button {self.tag} left-clicked! (info: {event}")


    def _right_click_actions(self, event):
        print(f"Button {self.tag} right-clicked! (info: {event}")
