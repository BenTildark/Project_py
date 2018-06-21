from tkinter import *
from tkinter import messagebox


def protocolhandler():
    print("running protocolhandler")
    protocolhandler.has_been_called = True
    pass

    if messagebox.askokcancel("Exit", "Wanna leave?"):
        if messagebox.askyesno("Exit", "You sure?"):
            if messagebox.askyesnocancel("Exit", "Really."):
                root.destroy()
                print("Bye.")
                


protocolhandler.has_been_called = False

if protocolhandler.has_been_called:
    root = Tk()
    root.protocol("WM_DELETE_WINDOW", protocolhandler)
    root.withdraw()
    root.mainloop()
