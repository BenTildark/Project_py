from tkinter import *
from tkinter.messagebox import *


def reset_password():
    """Reset pwd handler."""
    print("This is the password handler.")


def display_help_about():
    """ Display typical help about."""
    showinfo("This is the help about section.", "About")


def exit_menu():
    """Tidy up and exit gracefully."""
    root_window.destroy()


root_window = Tk()
menubar = Menu(root_window)

file_menu = Menu(menubar, tearoff=0)

file_menu.add_command(label="Reset", command=reset_password)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_menu)
menubar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menubar, tearoff=0)

help_menu.add_command(label="About", command=display_help_about)
menubar.add_cascade(label="Help", menu=help_menu)


root_window.config(menu=menubar)

root_window.mainloop()






