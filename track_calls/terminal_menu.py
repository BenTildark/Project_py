import os

from tkinter import *

from tkinter.messagebox import *

# Catch & ..
root = Tk()
# hide the default popup
root.withdraw()

"""

Terminal Menu #9-2-2
=============

Developed by: Michael Devenport
Email: croxleyway@gmail.com

Implement save / load data

"""

# Main assignments
exit_selection = 'E'
selection = ""
data_file = "data.txt"

# Menu prompt/input assignments
blank_line = " "
selection_prompt = "Please select from one of the following options."
item_prompt = "1) Enter an item."
remove_one_item_prompt = "2) Remove an item by its element number."
count_items_prompt = "3) Display the number of items in the list."
display_items_prompt = "4) Display a list of the items."
remove_all_items_prompt = "5) Remove all items from the list."
instance_count_prompt = "6) Count the instances of an item in the list."
save_data_prompt = "s) Save data."
load_data_prompt = "l) Load data."
exit_prompt = "9) Exit.".replace('9', 'E')

option_prompt = "Option: "

# Option assignments
enter_item = 1
remove_item_by_id = 2
num_of_items = 3
list_items = 4
remove_all_items = 5
count_instance = 6

# Confirm & Proceed
confirmation_choice_true = 'y'

# Option input/function & return statement assignments
enter_item_prompt = "Please enter the item: "  # option 1 input field prompt
append_confirmation_prompt = "[{}] is already in the list," \
                             " please confirm that you want to add another [Y/N]: "  # option 1 confirmation prompt
list_addition_singular = "[{}] has been added to the list." \
                         " There is now {} item in the list."  # singular statement for option 1 success
list_addition_plural = "[{}] has been added to the list." \
                       " There are now {} items in the list."  # plural statement for option 1 success
list_addition_failure = "[{}] was not added."  # option 1 return confirm False
remove_one_item = "Please enter the" \
                  " element number of the item to remove: "  # option 2 int input field prompt
element_deletion_success = "Element {} has been removed from the list."  # return statement for option 2 success
element_deletion_failure = "Sorry element {}" \
                           " does not exist in the list."  # return statement for option 2 failure
count_item_singular = "There is {} item in the list."  # option 3 only 1 item in list
count_item_plural = "There are {} items in the list."  # option 3 zero / more than 1 item in list
display_list = "Item {}: {}"  # option 4 is items in list
list_failure = "Sorry, the list is empty."  # options 4, 5 & 7 empty list return
all_items_removed_confirmation = "All the items have been removed from the list."  # option 5 populated list

instance_count_singular = "There is {} instance of [{}] in the list."  # option 6 singular return
instance_count_plural = "There are {} instances of [{}] in the list."  # option 6 plural return

overwrite_confirmation_prompt = "The file exists, overwrite? (Y/N): "  # option 7 prompt for overwrite file
write_confirmation = "Data has been saved."  # write confirm for overwrite
write_opt_out = "Data was not saved."  # write opt out

items_deletion_confirmation_prompt = "Data already exists in the list, overwrite? (Y/N): "
load_confirmation = "Data has been loaded."
load_opt_out = "Data was not loaded."

exit_statement = "Bye."  # exit option 9

# Create a list of menu options
menu_options = [
    item_prompt,
    remove_one_item_prompt,
    count_items_prompt,
    display_items_prompt,
    remove_all_items_prompt,
    instance_count_prompt,
    save_data_prompt,
    load_data_prompt,
    exit_prompt
]

items = []  # to be aggregate assignment list object, required outside of loop for compiling.

while selection != exit_selection:

    print(" ")
    print(selection_prompt)

    # Iterate our aggregate( menu_options )
    for constituent in menu_options:
        print(constituent)

    # Call to input function( menu options )
    selection = input(option_prompt)

    # check if selection value is numeric
    if selection.isnumeric():
        selection = int(selection)  # if True covert selection str_to_int for options evaluations below.

    # option 1 evaluation
    if selection == enter_item:
        add_item = True
        item_new = input(enter_item_prompt).replace(' ', '_').strip()  # work around for multiple word input/whitespace
        if item_new in items:
            confirmation_choice = input(append_confirmation_prompt.format(item_new)).strip().lower()
            if confirmation_choice != confirmation_choice_true:  # = 'Y'
                add_item = False

        if add_item:
            items.append(item_new)
            if len(items) == 1:
                print(list_addition_singular.format(item_new, len(items)))
            else:
                print(list_addition_plural.format(item_new, len(items)))
        else:
            print(list_addition_failure.format(item_new))

    # option 2 evaluation
    elif selection == remove_item_by_id:
        if len(items) > 0:
            element_num = int(input(remove_one_item))
            if all([element_num <= len(items), element_num > 0]):
                items.pop(element_num-1)
                print(element_deletion_success.format(element_num))
            else:
                print(element_deletion_failure.format(element_num))
        else:
            print(list_failure)

    # option 3 evaluation
    elif all([selection == num_of_items, len(items) == 1]):
        print(count_item_singular.format(len(items)))

    elif all([selection == num_of_items, not len(items) == 1]):
        print(count_item_plural.format(len(items)))

    # option 4 evaluation
    elif all([selection == list_items, len(items) >= 1]):
        # print(str(items)) debugging save/load options 7/8
        count = 0
        for item in items:
            count += 1
            print(display_list.format(count, item))
    elif all([selection == list_items, len(items) == 0]):  # 'len(items) == 0' will evaluate to True if list empty
        print(list_failure)

    # option 5 evaluation
    elif all([selection == remove_all_items, len(items) > 0]):
        items.clear()
        print(all_items_removed_confirmation)
    elif all([selection == remove_all_items, not items]):  # 'not items' will evaluate to True if list empty
        print(list_failure)

    # option 6 evaluation
    elif all([selection == count_instance, items]):  # are there any items in our list object
        instance_query = input(enter_item_prompt).replace(' ', '_').strip()
        instance_count = items.count(instance_query)
        if instance_count == 1:
            print(instance_count_singular.format(instance_count, instance_query))
        elif any([instance_count > 1, instance_count == 0]):
            print(instance_count_plural.format(instance_count, instance_query))
    elif all([selection == count_instance, not items]):
        print(list_failure)

    # option 7 evaluation ( save data from list obj )
    elif str(selection).lower() == 's':
        if items:
            save_data = True
            # The file is present in the cwd
            if os.path.exists(data_file):
                overwrite_confirm = input(overwrite_confirmation_prompt).lower()
                if overwrite_confirm != confirmation_choice_true:
                    save_data = False

            if save_data:
                df = open(data_file, "w")
                for item in items:
                    df.write(item + '\n')
                df.close()
                print(write_confirmation)
            else:
                showwarning(None, write_opt_out)
                #print(write_opt_out)
        else:
            print(list_failure)

    # option 8 evaluation( load saved data into list[items] )
    elif str(selection).lower() == 'l':
        # The file is present in the cwd (line 199)
        # Required as program runs an error if one tries retrieving data from file that does not exist
        if os.path.exists(data_file):
            load_data = True
            items_deletion_confirm = input(items_deletion_confirmation_prompt).lower()
            if items_deletion_confirm != confirmation_choice_true:
                load_data = False

            # if "load_data" is still True( so option Y was clicked ) or no items in items list obj do: [..] else do:
            if any([load_data, not items]):
                items.clear()
                df = open(data_file, "r")
                for entry in df:
                    items.append(entry.replace('\n', ''))
                df.close()
                print(load_confirmation)
            else:
                showwarning(None, load_opt_out)
                #print(load_opt_out)

# Exit program
print(exit_statement)
