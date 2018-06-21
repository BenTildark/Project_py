from tkinter import *
import random
 
def process_guess():
    guess_string = guess.get()
    # Check that the entered guess is a digit
    if guess_string.isdigit():
        # If it is convert it to an integer
        the_guess = int(guess.get())
 
        # For testing
        print("You entered {}".format(the_guess))
 
        # Examine their guess
        if the_guess == random_number.get():
            # Correct guess
            print("Correct")
            # Start a new game
            initialise_game()
        else:
            # Incorrect guess
            guess_state.set("Incorrect")
            # Decrement available guesses
            guesses.set(guesses.get()-1)
            # Update the filed so the user knows how many guesses are remaining
            remaining_guesses.set("Guess #"+str(guesses.get()))
 
            # Was that their last go?
            if guesses.get() == 0:
                # Yes so tell them the number and start a new game
                print("Game over")
                print("Answer was {}".format(random_number.get()))
                initialise_game()
                
    # Blank the entered guess field ready for their next guess
    guess.set("")
    return
 
def initialise_game():
    # Generate random number
    random_number.set(random.randrange(min_random_number, max_random_number + 1))
    # Print out for testing
    print("Random number is: {}".format(random_number.get()))
    # Set maximum guesses
    guesses.set(max_guesses)
    # Blank the guess field
    guess.set("")
    # Tell the user how many guesses they have
    remaining_guesses.set("Guess #"+str(guesses.get()))
    # Set the status to sy this is a new game
    guess_state.set("New game")
    return
max_guesses = 4
min_random_number = 0
max_random_number = 10
 
root_window = Tk()
root_window.title("Random number game.") 
random_number = IntVar()
 
# Maximum guesses
guesses = IntVar()
 
# Remaining guesses
remaining_guesses=StringVar()
remaining_guesses_label = Label(root_window,textvariable=remaining_guesses) 
remaining_guesses_label.pack()
 
# The state or result of their guess
guess_state = StringVar()
# guess_state_label = Label( root_window, textvariable=guess_state, relief=RAISED )
guess_state_label = Label( root_window, textvariable=guess_state )
guess_state_label.pack()
 
# The guess entered by the user
guess = StringVar() 
guess_entry = Entry(root_window,textvariable=guess) 
guess_entry.pack()
 
# Button for triggering the processing of the entered guess
guess_button = Button(root_window,text="Enter guess", command=process_guess)
guess_button.pack()
 
initialise_game()
 
root_window.mainloop()

