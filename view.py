import tkinter as tk
from tkinter import ttk


class LabelEntry(tk.Frame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent)

        self.label_text = kwargs.pop('labeltext', None)

        self.label = tk.Label(self, text=self.label_text)
        self.label.grid(row=0, column=0, sticky=tk.W)

        self.entry = ttk.Entry(self, **kwargs)
        self.entry.grid(row=0, column=1, sticky=tk.EW)

        self.columnconfigure(1, weight=2)


class View(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # create the menu
        #######################################################################

        # add the file menu
        # the open menu item
        # the save menu item
        # the separator
        # the exit menu item

        # create the widgets
        #######################################################################

        # add the so number display box and label
        self.order_number_label = ttk.Label(self, text='Order #')
        self.order_number_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.order_number_display = ttk.Entry(self)
        self.order_number_display.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        # add the customer name box
        self.customer_name_label = ttk.Label(self, text='Customer Name')
        self.customer_name_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.customer_name_display = ttk.Entry(self)
        self.customer_name_display.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)

        # add the treeview
        self.table = ttk.Treeview(self)
        self.table.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

        # add the vertical scroll bar
        self.y_scrollbar = ttk.Scrollbar(self, orient='vertical')
        self.y_scrollbar.grid(row=2, column=2, sticky=tk.NS)

        # add the horizontal scroll bar
        self.x_scrollbar = ttk.Scrollbar(self, orient='horizontal')
        self.x_scrollbar.grid(row=3, column=0, columnspan=2, sticky=tk.EW)

        self.rowconfigure(0, weight=2)
        self.columnconfigure(0, weight=2)

