from tkinter import *

from tkinter.messagebox import *

# Auth: Michael Devenport
# Email: croxleyway@gmail.com

# Q: 13 1 q4

def response_widget():
	"""shows option response"""
	option_response = {'1': 'You selected to enter a new item.', '2': 'You selected to remove an item by its element number.', '3': 'You selected to display the number of items in the list.', '4': 'You selected to display a list of the items.', '5': 'You selected to remove all of the items.'}
	showinfo(None, option_response[str(option.get())])
    
# Create the root window
root = Tk()
option = IntVar()
# Set window title
root.title("DTEC501 MENU")
# Set window size in pixels
root.geometry("400x400")

root_label = Label(root, text="Please select the number from one of the following options.")
root_label.pack()

radio_btn1 = Radiobutton(root, text=") Enter a new item.", variable=option, value=1, command=response_widget)
radio_btn1.pack(anchor=W)

radio_btn2 = Radiobutton(root, text=") Remove an item by its element number.", variable=option, value=2, command=response_widget)
radio_btn2.pack(anchor=W)

radio_btn3 = Radiobutton(root, text=") Display the number of items in the list.", variable=option, value=3, command=response_widget)
radio_btn3.pack(anchor=W)

radio_btn4 = Radiobutton(root, text=") Display a list of the items.", variable=option, value=4, command=response_widget)
radio_btn4.pack(anchor=W)

radio_btn5 = Radiobutton(root, text=") Remove all items from the list.", variable=option, value=5, command=response_widget)
radio_btn5.pack(anchor=W)

label = Label(root)
label.pack()

# Keep the window running​
root.mainloop()   




