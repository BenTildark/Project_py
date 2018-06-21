from tkinter import *
from tkinter.messagebox import *

# Define a function to handle the event.
def check_password():
	"""display resault of program"""
	if str(entered_data1.get()) == str(entered_data2.get()):
		showinfo(None, "The password has been changed.")
	else:
		showinfo(None, "Password mismatch. The password has not been changed.")


# Create root window
root = Tk()

# Add label to root window
pwd_label = Label(root, text="Please enter your password")
pwd_label.pack()

# Add password fields
entered_data1 = StringVar()
pwd1 = Entry(root, show="*", textvariable=entered_data1)
pwd1.pack()
entered_data2 = StringVar()
pwd2 = Entry(root, show="*", textvariable=entered_data2)
pwd2.pack()

# Add submit button
pwd_btn = Button(None, text="Change password", command=check_password)
pwd_btn.pack()

root.mainloop()