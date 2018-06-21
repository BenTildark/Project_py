from tkinter import *

from tkinter.messagebox import *

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 13 1 q5

def response_widget():
	"""shows option response"""
	option_response = {'1': 'You selected to enter a new item.', '2': 'You selected to remove an item by its element number.', '3': 'You selected to display the number of items in the list.', '4': 'You selected to display a list of the items.', '5': 'You selected to remove all of the items.'}
	option_field = str(option.get())
	if option_field in option_response:
		showwarning(None, option_response[str(option.get())])

# Create the root window
root = Tk()

# Set window title
root.title("DTEC501 MENU")
# Set window size in pixels
root.geometry("400x400")

root_label = Label(root, text="Please select the number from one of the following options.")
root_label.pack()

root_label = Label(root, text="1) Enter a new item.")
root_label.pack()

root_label = Label(root, text="2) Remove an item by its element number.")
root_label.pack()

root_label = Label(root, text="3) Display the number of items in the list.")
root_label.pack()

root_label = Label(root, text="4) Display a list of the items.")
root_label.pack()

root_label = Label(root, text="5) Remove all items from the list.")
root_label.pack()

option = StringVar()
text_area = Entry(root, textvariable=option)
text_area.pack()

submit_button = Button(None, text="Click to enter.", command=response_widget)
submit_button.pack()

label = Label(root)
label.pack()

# Keep the window running​
root.mainloop()   





