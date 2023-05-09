import tkinter as tk
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

global score
score = 0
#___________________________________ANOTHER_NUMBER_______________________________________________
class GuessingGameGUI:
    def __init__(self, master):

        self.master = master
        self.master.title("Guessing Game")
        # Get the screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Set the window size
        window_width = 450
        window_height = 170
        self.master.geometry(f"{window_width}x{window_height}")

        # Calculate the x and y coordinates for the top-left corner of the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the position of the window to the center of the screen
        self.master.geometry(f"+{x}+{y}") 
        
        # Create a label to display the prompt
        self.prompt_label = tk.Label(master, text="According to the numbers below, what is the number that should come next?")
        self.prompt_label.pack()
        
        # Create a label to display the sequence
        self.sequence_label = tk.Label(master, text="0, 2, 6, 12, 20, 30")
        self.sequence_label.pack()
        
        # Create an entry widget for the user to input their answer
        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()
        
        # Create a button to submit the user's answer
        self.submit_button = tk.Button(master, text="Submit", command=self.check_answer)
        self.submit_button.pack()
        
        # Create a label to display feedback on the user's answer
        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack()
        
        # Create a label to display the user's score
        self.score_label = tk.Label(master, text="Score: 0")
        self.score_label.pack()
        
        # Create a button to switch the language
        self.switch_button = tk.Button(master, text="Switch Language", command=self.switch_language)
        self.switch_button.pack()
        
        # Initialize game variables
        self.language = "eng"
        self.score = 0
        
    def check_answer(self):
        # Get the user's answer from the entry widget
        answer = self.answer_entry.get()
        
        # Check the answer and update the feedback label and score
        if answer == "42":
            self.feedback_label.config(text="Correct!")
            self.score += 1
            global score
            score+=1
            if self.language == "eng":
                self.feedback_label.config(text="Correct!", fg="green")
            elif self.language == "gr":
                self.feedback_label.config(text="Σωστά!", fg="green")
            # Schedule the destruction of the window after 1 second
            root.after(1000, root.destroy)
        else:
            if self.language == "eng":
                self.feedback_label.config(text="Wrong! The correct value is 42.", fg="red")
            elif self.language == "gr":
                self.feedback_label.config(text="Λάθος! Η σωστή τιμή είναι 42.", fg="red")
            root.after(1000, root.destroy)
        if self.language == "eng":
            self.score_label.config(text=f"Score: {self.score}")
        elif self.language == "gr":
            self.score_label.config(text=f"Σκορ: {self.score}")
        
        # Clear the answer entry widget
        self.answer_entry.delete(0, tk.END)
    
    def switch_language(self):
        # Update the language and prompt label
        if self.language == "eng":
            self.language = "gr"
            self.prompt_label.config(text="Συμφωνα με τους αριθμούς παρακάτω ποιός θα έπρεπε να είναι ο επόμενος;")
            self.score_label.config(text=f"Σκορ: {self.score}")
            self.switch_button.config(text="Αλλαγή γλώσσας")
            self.submit_button.config(text="Υποβολή")
        else:
            self.language = "eng"
            self.prompt_label.config(text="According to the numbers below, what is the number that should come next?")
            self.score_label.config(text=f"Score: {self.score}")
            self.switch_button.config(text="Switch Language")
            self.submit_button.config(text="Submit")
        
        # Update the sequence label
        self.sequence_label.config(text="0, 2, 6, 12, 20, 30")
        
        # Clear the answer entry widget and feedback label
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        
root = tk.Tk()
app = GuessingGameGUI(root)
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 450
window_height = 170
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}")
root.mainloop()

#___________________________________CORRECT_NUMBER_______________________________________________

array = [[2, 8, 7], 
         [6, 9, 5], 
         [9, 5, 9], 
         [7, 4, None]]

def replace_none(array_display):
    # Get the user's input from the Entry widget
    new_value = entry.get()
    
    # Check if the user entered 9 and update the array if true
    if new_value == '9':
        array[-1][-1] = int(new_value)
        # Update the array_display Label with the new array
        array_display.config(text=array)
        error_label.config(text="Correct! Good bye!", fg="green")
        global score
        score+=1
        score_label.config(text=f"Score: {score}")
        # Schedule the destruction of the window after 1 second
        root.after(1000, root.destroy)

    else:
        # Display an error message if the user entered an invalid value
        error_label.config(text="Invalid input. The correct value for 'None' is 9.", fg="red")
        root.after(1000, root.destroy)
    # Clear the input in the Entry widget
    entry.delete(0, 'end')

# Create the main window
root = tk.Tk()
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 350
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}") 


# Create a Label and an Entry widget to prompt the user for input
input_label = tk.Label(root, text="Enter a value for None:")
input_label.pack()
entry = tk.Entry(root)
entry.pack()

# Create a Button to replace the None value
replace_button = tk.Button(root, text="Replace", command=lambda: replace_none(array_display))
replace_button.pack()

# Create a label to display the user's score
score_label = tk.Label(root, text=f"Score: {score}")
score_label.pack()

# Create a Label to display error messages
error_label = tk.Label(root, fg="red")
error_label.pack()

 # Create a Label to display the array in the main window
array_display = tk.Label(root, text=array)
array_display.pack()

# Start the GUI event loop
root.mainloop()

#___________________________________RANDOM_EQUATION_______________________________________________

# Generate a random equation with random coefficients
def random_equation(a):
    b=0
    while b==0:
        b = random.randint(-10, 10)
    c = random.randint(-100, 100)
    equation = f"{b}*x + {c} = {b*a + c}"
    return equation

# Check the answer and update the score
def check_answer():
    global score
    answer = answer_entry.get()
    if answer == str(a):
        if language_pref == "eng":
            result_label.config(text="Correct!", fg="green")
        elif language_pref == "gr":
            result_label.config(text="Σωστά!", fg="green")
        score += 1
        # Schedule the destruction of the window after 1 second
        root.after(1000, root.destroy)
    else:
        if language_pref == "eng":
            result_label.config(text=f"Wrong! The value of x is {a}.", fg="red")
        elif language_pref == "gr":
            result_label.config(text=f"Λάθος! Η τιμή του χ είναι {a}.", fg="red")
        root.after(1000, root.destroy)
    if language_pref == "eng":
        score_label.config(text=f"Score: {score}")
    elif language_pref == "gr":
        score_label.config(text=f"Σκορ: {score}")

    check_button.config(state=tk.DISABLED)

    # Clear the answer entry widget
    answer_entry.delete(0, tk.END)

# Generate a new equation and update the GUI
def new_equation():
    global a
    a = random.randint(-10, 10)
    equation = random_equation(a)
    equation_label.config(text=equation)
    result_label.config(text="")
    answer_entry.delete(0, tk.END)
    check_button.config(state=tk.ACTIVE)

# Set the language preference to English
def set_english():
    global language_pref
    language_pref = "eng"
    language_label.config(text="Language: English")
    check_button.config(text="Check")
    new_button.config(text="New Equation")
    score_label.config(text=f"Score: {score}")

# Set the language preference to Greek
def set_greek():
    global language_pref
    language_pref = "gr"
    language_label.config(text="Γλώσσα: Ελληνικά")
    check_button.config(text="Έλεγχος")
    new_button.config(text="Νέα εξίσωση")
    score_label.config(text=f"Σκορ: {score}")

# Initialize the GUI and language preference
a = 0
language_pref = "eng"
root = tk.Tk()
root.title("Random Equation Game")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 350
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}") 

# Create the language preference buttons
language_frame = tk.Frame(root)
language_frame.pack(pady=10)

english_button = tk.Button(language_frame, text="English", font=("Arial", 14), command=set_english)
english_button.pack(side=tk.LEFT, padx=10)

greek_button = tk.Button(language_frame, text="Ελληνικά", font=("Arial", 14), command=set_greek)
greek_button.pack(side=tk.LEFT, padx=10)

language_label = tk.Label(root, font=("Arial", 14))
language_label.pack(pady=10)

equation_label = tk.Label(root, font=("Arial", 18))
equation_label.pack(pady=20)

answer_entry = tk.Entry(root, font=("Arial", 18), width=5)
answer_entry.pack(pady=10)

check_button = tk.Button(root, text="Check", font=("Arial", 18), command=check_answer)
check_button.pack(pady=10)

result_label = tk.Label(root, font=("Arial", 18))
result_label.pack(pady=10)

new_button = tk.Button(root, text="New Equation", font=("Arial", 18), command=new_equation)
new_button.pack(pady=10)

score_label = tk.Label(root, font=("Arial", 18))
score_label.pack(pady=20)

# Set the initial language preference to English and generate a new equation
set_english()
new_equation()

root.mainloop()

#___________________________________HANOI_______________________________________________

"""
Tower of Hanoi for Python - Main Module
"""

import models_eng

# Define screen constants
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
# Color constants object
color = models_eng.ColorConstants()
# Init pygame
pygame.init()
# Define the screen (and it's properties)
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tower of Hanoi for Python")
# Create main menu object
menu = models_eng.MainMenu(SCREEN_WIDTH,SCREEN_HEIGHT)
# Create game object
game = models_eng.Game(SCREEN_WIDTH,SCREEN_HEIGHT)
# Discs' move variables
done = False
drag = False
drop = False
move = False
game_over = False
init_game = False
disc_index = None
last_pos = [0,0]
# Moves counter
moves_counter = 0
# Manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Game Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drag = True
            drop = False
            if init_game:
                if not game_over:
                    for i in range(0,game.n_discs):
                        if game.discs[i].is_clicked():
                            current_pos = game.discs[i].current_pos
                            pos_length = len(game.positions[current_pos].discs)
                            if game.discs[i] == game.positions[current_pos].discs[pos_length-1]:
                                disc_index = i
                                last_pos = [game.discs[i].rect.x,game.discs[i].rect.y]
                                move = True
                else:
                    if menu.btn_quit.is_clicked():
                        done = True
                    if menu.btn_play_again.is_clicked():
                        game.sprites_list.remove(game.discs)
                        game.positions[2].discs = []
                        moves_counter = 0
                        game.discs = []
                        game.draw_discs()
                        game_over = False
                    if menu.btn_return.is_clicked():
                        menu.sprites_list.remove([menu.btn_play_again,menu.btn_return,menu.btn_quit])
                        menu.sprites_list.add([menu.btn_discs,menu.label])
                        game.sprites_list.remove(game.discs)
                        init_game = False
            else:
                for i in range(0,len(menu.btn_discs)):
                    if menu.btn_discs[i].is_clicked():
                        game.set_n_discs(menu.btn_discs[i].value)
                        game.sprites_list.remove(game.discs)
                        game.discs = []
                        game.positions[2].discs = []
                        moves_counter = 0
                        game.draw_discs()
                        init_game = True
                        game_over = False
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            drag = False
            drop = True
    screen.fill(game.WHITE)
    # Title line
    pygame.draw.line(screen, game.BLACK, [0, 60], [SCREEN_WIDTH,60], 5)
    # Text font,size, bold and italic
    font = pygame.font.SysFont('Calibri', 30, False, False)
    title_font = pygame.font.SysFont('Calibri', 50, False, False)
    # Info Texts
    game_title = title_font.render("Tower of Hanoi ", True, color.BLACK)
    screen.blit(game_title, [((SCREEN_WIDTH/2)-(game_title.get_width()/2)),20])
    if init_game:
        player_moves = font.render("Player moves: "+str(moves_counter), True, color.BLACK)
        min_moves = font.render("Minimum of required movements: "+str(game.min_moves), True, color.BLACK)
        screen.blit(player_moves, [20, 80])
        screen.blit(min_moves, [20, 110])
        if game_over:
            menu.sprites_list.draw(screen)
            if len(game.positions[2].discs) == game.n_discs:
                if moves_counter == game.min_moves:
                    #9score +=1
                    game_over_title = font.render("Congratulations! You finished with the minimums movements! :)", True, color.BLACK)
                    screen.blit(game_over_title, [((SCREEN_WIDTH/2)-(game_over_title.get_width()/2)),SCREEN_HEIGHT/2])
                else:
                    game_over_title = font.render("You finished, now try again with the minimums movements! ;)", True, color.BLACK)
                    screen.blit(game_over_title, [((SCREEN_WIDTH/2)-(game_over_title.get_width()/2)),SCREEN_HEIGHT/2])
        else:
            if drag:
                if move:
                    pos = pygame.mouse.get_pos()
                    game.discs[disc_index].rect.x = pos[0] - (game.discs[disc_index].width/2)
                    game.discs[disc_index].rect.y = pos[1] - (game.discs[disc_index].height/2)
            elif drop:
                if move:
                    current_pos = game.discs[disc_index].current_pos
                    new_pos = None
                    change = False
                    turn_back = True
                    position = pygame.sprite.spritecollideany(game.discs[disc_index],game.pos_sprites_list)
                    if position != None:
                        new_pos = position.pos_index
                        if new_pos != current_pos:
                            disc_length = len(position.discs)
                            if disc_length == 0:
                                turn_back = False
                                change = True
                            elif game.discs[disc_index].id > position.discs[disc_length-1].id:
                                turn_back = False
                                change = True
                    if change:
                        moves_counter = moves_counter + 1
                        game.positions[current_pos].discs.remove(game.discs[disc_index])
                        game.discs[disc_index].current_pos = new_pos
                        game.positions[new_pos].discs.append(game.discs[disc_index])
                        new_pos_length = len(game.positions[new_pos].discs)
                        game.discs[disc_index].rect.x = game.positions[new_pos].rect.x - ((game.DISC_WIDTH/(game.discs[disc_index].id+1)/2)-(game.DISC_HEIGHT/2))
                        game.discs[disc_index].rect.y = (game.BOARD_Y - game.DISC_HEIGHT) - (game.DISC_HEIGHT*(new_pos_length-1))
                        #Check if the game is over
                        if (len(game.positions[2].discs) == game.n_discs):
                            game_over = True
                            menu.sprites_list.add([menu.btn_play_again,menu.btn_quit,menu.btn_return])
                            menu.sprites_list.remove([menu.label,menu.btn_discs])
                    if turn_back:
                        game.discs[disc_index].rect.x = last_pos[0]
                        game.discs[disc_index].rect.y = last_pos[1]
                    move = False
        game.sprites_list.draw(screen)
    else:
        menu.sprites_list.draw(screen)

    # --- update  screen.
    pygame.display.flip()
    # --- Limit to 60 frames per second
    clock.tick(60)
pygame.quit()

#___________________________________HANGMAN_______________________________________________

def new_game():
    global word, hidden_word, attempts
    word = random.choice(words)
    revealed_word = ['_' if i not in [0, len(word)-1] else word[i] for i in range(len(word))]
    for i in range(len(word)):
        if i not in [0, len(word)-1] and word[i] in [word[0], word[len(word)-1]]:
            revealed_word[i] = word[i]
    hidden_word.set(' '.join(revealed_word))
    attempts.set(6)
    guessed_letters.set('')
    update_display()
    result_label.config(text='')

def guess_letter():
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha() or letter in guessed_letters.get():
        return
    
    guessed_letters.set(guessed_letters.get() + letter + ' ')

    if attempts.get() != 0:
        if letter in hidden_word.get() or letter not in word:
            attempts.set(attempts.get() - 1)
        else:
            current_hidden_word = list(hidden_word.get().replace(' ', ''))
            for i, char in enumerate(word):
                if char == letter:
                    current_hidden_word[i] = letter
            hidden_word.set(' '.join(current_hidden_word))
    else:
        # Reset the game and choose a new word
        new_game()

    update_display()

    if attempts.get() == 0 or '_' not in hidden_word.get():
        show_result()


def update_display():
    word_label.config(text=hidden_word.get())
    attempts_label.config(text=f'Attempts left: {attempts.get()}')
    guessed_letters_label.config(text=f'Guessed letters: {guessed_letters.get()}')

def show_result():
    result = "You won!" if '_' not in hidden_word.get() else "You lost!"
    result_label.config(text=result)
    
    if result == "You won!":
        global score
        score+=1

    if attempts.get() == 0:
        # Reveal the entire word when the player loses
        hidden_word.set(word)
        update_display()

    # delay for 2 seconds before ending the new
    root.after(1000, root.destroy)

# Read words from file
with open('Psychometric_IQ_Team_Formation-main\hangman_words_eng.txt', 'r') as f:
    words = [line.strip() for line in f]

# Set a new word for the game
word = random.choice(words)


root = tk.Tk()
root.title('Hangman')
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 450
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}") 

hidden_word = tk.StringVar()
attempts = tk.IntVar()
guessed_letters = tk.StringVar()

word_label = tk.Label(root, font=('Arial', 24))
word_label.grid(row=0, column=0, columnspan=2, pady=20)

# Create a label to display the user's score
score_label = tk.Label(root, text=f"Score: {score}", font=('Arial', 18))
score_label.grid(row=6, column=0, columnspan=2, pady=20)

entry = tk.Entry(root, font=('Arial', 24))
entry.grid(row=1, column=0, pady=20)

guess_button = tk.Button(root, text='Guess', font=('Arial', 18), command=guess_letter)
guess_button.grid(row=1, column=1, pady=10)

attempts_label = tk.Label(root, font=('Arial', 18))
attempts_label.grid(row=2, column=0, columnspan=2, pady=20)

new_game_button = tk.Button(root, text='New Game', font=('Arial', 18), command=new_game)
new_game_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, font=('Arial', 18))
result_label.grid(row=4, column=0, columnspan=2, pady=20)

guessed_letters_label = tk.Label(root, font=('Arial', 18))
guessed_letters_label.grid(row=5, column=0, columnspan=2, pady=20)

new_game()
root.mainloop()

#___________________________________QUESTIONS_______________________________________________

class IQTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("IQ Test")
        # Get the screen width and height
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Calculate the x and y coordinates for the top-left corner of the window
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Set the position of the window to the center of the screen
        master.geometry(f"+{x}+{y}") 

        self.question_label = tk.Label(master, text="Question 1: What color is a banana?", font=("Helvetica", 16))
        self.question_label.grid(row=0, column=0, sticky="w")

        self.answer_entry = tk.Entry(master, font=("Helvetica", 16))
        self.answer_entry.grid(row=1, column=0, sticky="w")

        self.submit_button = tk.Button(master, text="Submit", font=("Helvetica", 16), command=self.submit_answer)
        self.submit_button.grid(row=2, column=0, sticky="w")

        self.score_label = tk.Label(master, text="Score: {}".format(score), font=("Helvetica", 16))
        self.score_label.grid(row=3, column=0, sticky="w")

        self.question_index = 0
        self.questions = [
            ("What color is a banana?", "yellow"),
            ("What is 2-2+2*2^2/2?", "4"),
            ("What is the capital of France?", "Paris"),
            ("What is the name of the largest ocean on Earth?", "Pacific"),
            ("What is the opposite of 'up'?", "down"),
            ("What is the last 4 digits number?", "9999"),
            ("What is the name of the tallest mountain in the world?", "Everest"),
            ("What is the capital of Greece?", "Athens"),
            ("What is the name of the smallest planet in our solar system?", "Mercury"),
            ("What is the name of the famous scientist who developed the theory of relativity?", "Albert Einstein"),
            ("What is the square root of 256?", "16"),
            ("What is the next number in this sequence? 1, 4, 9, 16, 25, ...", "36"),
            ("Which country has the largest population in the world?", "China"),
            ("What is the name of the largest desert in the world?", "Sahara"),
            ("In what year did World War II end?", "1945")
        ]
        self.score = score

    def submit_answer(self):
        answer = self.answer_entry.get().lower()
        correct_answer = self.questions[self.question_index][1].lower()
        if answer == correct_answer:
            self.score += 1
            global score
            score += 1
            self.question_label.config(fg="green", text="Correct!")
        else:
            self.question_label.config(fg="red", text="Incorrect!")
        self.score_label.config(text="Score: {}".format(self.score))
        self.question_index += 1
        if self.question_index < len(self.questions):
            self.answer_entry.delete(0, tk.END)
            self.submit_button.config(state=tk.DISABLED)
            self.master.after(500, self.display_next_question)
        else:
            self.display_final_score()
            self.answer_entry.delete(0, tk.END)
            self.answer_entry.config(state=tk.DISABLED)
            self.submit_button.config(state=tk.DISABLED)
            
            # show final score and message
            final_score = "Final Score: {}/{}".format(self.score, 19)
            if self.score >= 15:
                message = "Congratulations! You are a genius!"
            elif self.score >= 10:
                message = "Good job! You have above average intelligence."
            elif self.score >= 5:
                message = "Not bad! You have average intelligence."
            else:
                message = "Oops! You may want to read more books."
            result_window = tk.Toplevel(self.master)
            result_window.title("IQ Test Result")
            # Get the screen width and height
            screen_width = result_window.winfo_screenwidth()
            screen_height = result_window.winfo_screenheight()

            # Calculate the x and y coordinates for the top-left corner of the window
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)

            # Set the position of the window to the center of the screen
            result_window.geometry(f"+{x}+{y}")

            tk.Label(result_window, text=final_score, font=("Helvetica", 16)).pack()
            tk.Label(result_window, text=message, font=("Helvetica", 16)).pack()

    def display_next_question(self):
        self.question_label.config(text="Question {}: {}".format(self.question_index + 1, self.questions[self.question_index][0]), fg="black")
        self.submit_button.config(state=tk.ACTIVE)

    def display_final_score(self):
        self.question_label.config(text="You have completed the IQ test!", fg="black")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.master.after(1000, self.show_final_score)

    def show_final_score(self):
        final_message = "You scored {} out of {}!".format(self.score, 19)
        self.score_label.config(text=final_message)
        # Schedule the destruction of the window after 1 second
        root.after(2000, root.destroy)


root = tk.Tk()
app = IQTestGUI(root)
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 900
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}")
root.mainloop()

print(score)
