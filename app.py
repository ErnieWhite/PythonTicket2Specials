import tkinter as tk
from model import Model
from view import View
from controller import Controller


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Ticket 2 Specials')

        # create the model
        model = Model()

        # create the view
        view = View(self)
        view.grid(row=0, column=0)

        # create the controller
        controller = Controller(model, view)


if __name__ == '__main__':
    app = App()
    app.mainloop()
