import tkinter as tk
import random
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

global score
score = 0
#___________________________________ΑΛΛΟΣ_ΑΡΙΘΜΟΣ_______________________________________________
class GuessingGameGUI:
    def __init__(self, master):

        self.master = master
        self.master.title("Guessing Game")
        
        # Λήψη του πλάτους και του ύψους της οθόνης
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Καθορισμός του μεγέθους του παραθύρου
        window_width = 450
        window_height = 170
        self.master.geometry(f"{window_width}x{window_height}")

        # Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
        self.master.geometry(f"+{x}+{y}")

        # Δημιούργησε ένα label με την ερώτηση
        self.prompt_label = tk.Label(master, text="Συμφωνα με τους αριθμούς παρακάτω ποιός θα έπρεπε να είναι ο επόμενος;")
        self.prompt_label.pack()
        
        # # Δημιούργησε ένα label με την ακολουθία
        self.sequence_label = tk.Label(master, text="0, 2, 6, 12, 20, 30")
        self.sequence_label.pack()
        
        # Δημιουργία ενός entry widget για τον χρήστη έτσι ώστε να εισάγει την απάντηση
        self.answer_entry = tk.Entry(master)
        self.answer_entry.pack()
        
        # Δημιουργία κουμπιού για την υποβολή των απαντήσεων
        self.submit_button = tk.Button(master, text="Υποβολή", command=self.check_answer)
        self.submit_button.pack()
        
        # Δημιουργία ενός label για να δωθεί ανατροφοδότηση στην απάντηση του χρήστη
        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack()
        
        # Δημιουργία ενός label για την παρουσίαση του σκορ
        self.score_label = tk.Label(master, text="Σκορ: 0")
        self.score_label.pack()
        
        # Δημιουργία κουμπιού αλλαγής γλώσσας
        self.switch_button = tk.Button(master, text="Αλλαγή γλώσσας", command=self.switch_language)
        self.switch_button.pack()
        
        # Αρχικοποίηση μεταβλητών
        self.language = "gr"
        self.score = 0
        
    def check_answer(self):
        # Πάρε την απάντηση του χρήστη από την είσοδο
        answer = self.answer_entry.get()
        
        # Έλεγξε την απάντηση και ενημέρωσε το σκορ και το feedback label
        if answer == "42":
            self.feedback_label.config(text="Correct!")
            self.score += 1
            global score
            score+=1
            if self.language == "eng":
                self.feedback_label.config(text="Correct!", fg="green")
            elif self.language == "gr":
                self.feedback_label.config(text="Σωστά!", fg="green")
            # Προγραμματισμός της καταστροφής του παραθύρου 1 δευτερόλεπτο μετά
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
        
        # Εκαθάρηση της εισόδου δεδομένων
        self.answer_entry.delete(0, tk.END)
    
    def switch_language(self):
        # Ενημέρωση γλώσσαας και του prompt label
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
        
        # Ενημέρωση του label ακολουθίας
        self.sequence_label.config(text="0, 2, 6, 12, 20, 30")
        
        # Καθαρισμός της εισόδου και του feedback label
        self.answer_entry.delete(0, tk.END)
        self.feedback_label.config(text="")
        
root = tk.Tk() 
app = GuessingGameGUI(root)
# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 450
window_height = 170
root.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}")
root.mainloop()

#___________________________________ΣΩΣΤΟΣ_ΑΡΙΘΜΟΣ_______________________________________________

array = [[2, 8, 7], 
         [6, 9, 5], 
         [9, 5, 9], 
         [7, 4, None]]

def replace_none(array_display):
    # Πάρε την είσοδου του χρήστη από το winget εισόδου
    new_value = entry.get()
    
    # Έλεγξε αν ο χρήστης έδωσε 9 και ενημέρωσε αν είναι Αληθής η συνθήκη
    if new_value == '9':
        array[-1][-1] = int(new_value)
        # Αναβάθμιση του array_display Label με τον καινούργιο πίνακα
        array_display.config(text=array)
        error_label.config(text="Σωστά! Αντίο!", fg="green")
        global score
        score+=1
        score_label.config(text=f"Σκορ: {score}")
        # Προγραμματισμός της καταστροφής του παραθύρου σε ένα δευτερόλεπτο
        root.after(1000, root.destroy)

    else:
        # Εμφάνισε μήνυμα λάθους αν ο χρήστης δεν δώσει 9
        error_label.config(text="Μη έγκυρη τιμή. Η σωστή τιμή για το 'None' είναι το 9.", fg="red")
        root.after(1000, root.destroy)
    # Καθαρισμός του widget εισόδου
    entry.delete(0, 'end')

# Λήψη του πλάτους και του ύψους της οθόνης
root = tk.Tk()
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 350
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}") 

# Δημιουργία Label και ενός Entry widget για να προτρέψουμε το χρήστη να εισάγει απάντηση
input_label = tk.Label(root, text="Δώστε μια τιμή για το 'None':")
input_label.pack()
entry = tk.Entry(root)
entry.pack()

# Δημιυργία κουμπιού για αντικατάσταση του "None"
replace_button = tk.Button(root, text="Αντικατάσταση", command=lambda: replace_none(array_display))
replace_button.pack()

# Δημιουργία label για παρουσίασει του σκορ του χρήστη
score_label = tk.Label(root, text=f"Σκορ: {score}")
score_label.pack()

# Δημιουργία Label για την εμφάνιση μηνύματος σφάλματος
error_label = tk.Label(root, fg="red")
error_label.pack()

 # Δημιουργία Label για εμφάνιση του πίνακα στο κύριο παράθυρο
array_display = tk.Label(root, text=array)
array_display.pack()

# Έναρξη του βρόγχου γεγονότων GUI
root.mainloop()

#___________________________________ΤΥΧΑΙΑ ΕΞΙΣΩΣΗ_______________________________________________

# Δημουργία τυχαίας συνάρτησης με τυχαίους συντελεστές
def random_equation(a):
    b=0
    while b==0:
        b = random.randint(-10, 10)
    c = random.randint(-100, 100)
    equation = f"{b}*x + {c} = {b*a + c}"
    return equation

# Έλεγχος απάντησης και ενημέρωηση σκορ
def check_answer():
    # Συνάρτηση ελέγχου απάντησης
    global score
    answer = answer_entry.get()
    if answer == str(a):
        if language_pref == "eng":
            result_label.config(text="Correct!", fg="green")
        elif language_pref == "gr":
            result_label.config(text="Σωστά!", fg="green")
        score += 1
        # Προγραμματισμός της καταστορφής του παραθύρου σε 1 δευτερόλεπτο
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

    # Καθαρισμός της εισόδου δεδομένων
    answer_entry.delete(0, tk.END)

# Δημιουργία νέας εξίσωσης και ενημέρωση GUI
def new_equation():
    global a
    a = random.randint(-10, 10)
    equation = random_equation(a)
    equation_label.config(text=equation)
    result_label.config(text="")
    answer_entry.delete(0, tk.END)
    check_button.config(state=tk.ACTIVE)

# Προτίμηση γλώσσαας Αγγλικά
def set_english():
    global language_pref
    language_pref = "eng"
    language_label.config(text="Language: English")
    check_button.config(text="Check")
    new_button.config(text="New Equation")
    score_label.config(text=f"Score: {score}")

# Προτίμηση γλώσσας Ελληνικά
def set_greek():
    global language_pref
    language_pref = "gr"
    language_label.config(text="Γλώσσα: Ελληνικά")
    check_button.config(text="Έλεγχος")
    new_button.config(text="Νέα εξίσωση")
    score_label.config(text=f"Σκορ: {score}")

# Αρχικοποίηση  GUI και της γλώσσας προτίμησης
a = 0
language_pref = "gr"
root = tk.Tk()
# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 350
window_height = 500
root.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}") 
root.title("Random Equation Game")

# Δημιουργία κουμπιών προτίμησης γλώσσας
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

check_button = tk.Button(root, text="Έλεγχος", font=("Arial", 18), command=check_answer)
check_button.pack(pady=10)

result_label = tk.Label(root, font=("Arial", 18))
result_label.pack(pady=10)

new_button = tk.Button(root, text="Νέα εξίσωση", font=("Arial", 18), command=new_equation)
new_button.pack(pady=10)

score_label = tk.Label(root, font=("Arial", 18))
score_label.pack(pady=20)

# Ορισμός της αρχικής γλώσσας προτίμησης στα Ελληνικά και ενημερώση GUI
set_greek()
new_equation()

root.mainloop()

#___________________________________HANOI_______________________________________________

"""
Πύργοι του Ανόι για Python - Main Module
"""
import models_gr
# Ορισμός σταθερών οθόνης
SCREEN_WIDTH = 900
SCREEN_HEIGHT = 700
# Χεώμα σταθερών αντικειμένου
color = models_gr.ColorConstants()
# Init pygame / κλάση κατασκευής
pygame.init()
# Ορισμός της οθόνης και των ιδιοτήτων της
size = [SCREEN_WIDTH, SCREEN_HEIGHT]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Πύργος του Ανόι για Python")
# Δημιουργία αντικειμένου του κεντρικού μενού
menu = models_gr.MainMenu(SCREEN_WIDTH,SCREEN_HEIGHT)
# Δημιουργία αντικειμένου παιχνιδιού
game = models_gr.Game(SCREEN_WIDTH,SCREEN_HEIGHT)
# Μεταβλητές κίνησης δίσκων
done = False
drag = False
drop = False
move = False
game_over = False
init_game = False
disc_index = None
last_pos = [0,0]
# Μετακίνηση μετρητή
moves_counter = 0
# Διαχείρηση του πόσο γρήγορα ανανεώωνεται η οθόνη
clock = pygame.time.Clock()
# -------- Βρόγχος κύριου παιχνιδιού -----------
while not done:
    # --- Κύριος βρόγχος
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
    # Γραμμή τίτλου
    pygame.draw.line(screen, game.BLACK, [0, 60], [SCREEN_WIDTH,60], 5)
    # Τύπος γραμματοσειράς,μέγεθος, έντονη γραμματοσειρά και πλάγια γράμματα
    font = pygame.font.SysFont('Calibri', 30, False, False)
    title_font = pygame.font.SysFont('Calibri', 50, False, False)
    # Κείμενο πληροφορίας
    game_title = title_font.render("Πύργος του Ανόι ", True, color.BLACK)
    screen.blit(game_title, [((SCREEN_WIDTH/2)-(game_title.get_width()/2)),20])
    if init_game:
        player_moves = font.render("Κινήσεις παίχτη: "+str(moves_counter), True, color.BLACK)
        min_moves = font.render("Ελάχιστες κινήσεις: "+str(game.min_moves), True, color.BLACK)
        screen.blit(player_moves, [20, 80])
        screen.blit(min_moves, [20, 110])
        if game_over:
            menu.sprites_list.draw(screen)
            if len(game.positions[2].discs) == game.n_discs:
                if moves_counter == game.min_moves:
                    game_over_title = font.render("Συγχαρητήρια! Τελείωσες με τις ελάχιστες κινήσεις! :)", True, color.BLACK)
                    screen.blit(game_over_title, [((SCREEN_WIDTH/2)-(game_over_title.get_width()/2)),SCREEN_HEIGHT/2])
                else:
                    game_over_title = font.render("Τελείωσες τώρα προσπάθησε με λιγότερες κινήσεις! ;)", True, color.BLACK)
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

    # --- Αναννέωση οθόμης.
    pygame.display.flip()
    # --- Περιορισμός σε 60 frames στο δευτερόλεπτο
    clock.tick(60)
pygame.quit()

#___________________________________ΚΡΕΜΑΛΑ_______________________________________________

import tkinter as tk
import random

def new_game():
    # Συνάρτηση δημιουργίας νέου παιχνιδιού
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
    # Συνάρτηση μαντεηιας και γνώσης
    letter = entry.get().upper()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
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
        # Επαναφορά παιχνιδιύ
        new_game()

    update_display()

    if attempts.get() == 0 or '_' not in hidden_word.get():
        show_result()


def update_display():
    # Συνάρτηση ενημέρωσης.
    word_label.config(text=hidden_word.get())
    attempts_label.config(text=f'Προσπάθειες που απομένουν: {attempts.get()}')
    guessed_letters_label.config(text=f'Γράμματα που μαντέυτηκαν: {guessed_letters.get()}')

def show_result():
    #Συνάρτηση αποτελεσμάυων
    result = "Συγχαρητήρια, βρήκες την λέξη!" if '_' not in hidden_word.get() else "Έχασες!"
    result_label.config(text=result)
    
    if result == "Συγχαρητήρια, βρήκες την λέξη!":
        global score
        score +=1

    if attempts.get() == 0:
        # RΑποκάλυψη της κρυμμένης λέξης και ενημέρψσει του σκρο.
        hidden_word.set(word)
        update_display()

    # Αναμονή 2 δευτερόλεπτα πριν κλείσει
    root.after(1000, root.destroy)

# Διάβασμα αρεχχείων από αρχεία
with open('hangman_words_gr.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f]

# Αρχικοποίηση νέας λέξης για το παιχνίδι
word = random.choice(words)

root = tk.Tk()
root.title('ΚΡΕΜΑΛΑ')
# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 600
window_height = 550
root.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}") 

hidden_word = tk.StringVar()
attempts = tk.IntVar()
guessed_letters = tk.StringVar()

word_label = tk.Label(root, font=('Arial', 24))
word_label.grid(row=0, column=0, columnspan=2, pady=20)

entry = tk.Entry(root, font=('Arial', 24))
entry.grid(row=1, column=0, pady=20)

guess_button = tk.Button(root, text='Μάντεψε ένα γράμμα:', font=('Arial', 18), command=guess_letter)
guess_button.grid(row=1, column=1, pady=10)

attempts_label = tk.Label(root, font=('Arial', 18))
attempts_label.grid(row=2, column=0, columnspan=2, pady=20)

# Δημιυργία ενός label για παρουσίασει του σκορ
score_label = tk.Label(root, text=f"Σκορ: {score}", font=('Arial', 18))
score_label.grid(row=6, column=0, columnspan=2, pady=20)

new_game_button = tk.Button(root, text='Νέο Παιχνίδι!', font=('Arial', 18), command=new_game)
new_game_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, font=('Arial', 18))
result_label.grid(row=4, column=0, columnspan=2, pady=20)

guessed_letters_label = tk.Label(root, font=('Arial', 18))
guessed_letters_label.grid(row=5, column=0, columnspan=2, pady=20)

new_game()
root.mainloop()

#___________________________________QUESTIONS_______________________________________________

import tkinter as tk

class IQTestGUI:
    def __init__(self, master):
        self.master = master
        master.title("IQ Test")

        # Λήψη του πλάτους και του ύψους της οθόνης
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
        x = (screen_width // 2) - (window_width // 2)
        y = (screen_height // 2) - (window_height // 2)

        # Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
        master.geometry(f"+{x}+{y}")

        self.question_label = tk.Label(master, text="Ερώτσηση 1: Τι χρώμα είναι η μπανάνα?", font=("Helvetica", 16))
        self.question_label.grid(row=0, column=0, sticky="w")

        self.answer_entry = tk.Entry(master, font=("Helvetica", 16))
        self.answer_entry.grid(row=1, column=0, sticky="w")

        self.submit_button = tk.Button(master, text="Υποβολή", font=("Helvetica", 16), command=self.submit_answer)
        self.submit_button.grid(row=2, column=0, sticky="w")

        self.score_label = tk.Label(master, text="Σκορ:{}".format(score), font=("Helvetica", 16))
        self.score_label.grid(row=3, column=0, sticky="w")

        self.question_index = 0
        self.questions = [
            ("Τι χρώμα είναι η μπανάνα;", "ΚΙΤΡΙΝΟ"),
            ("Ποιό το αποτέλεσμα της παράστασης 2-2+2*2^2/2;", "4"),
            ("Ποιά είναι η πρωτεύουσα της Γαλλίας;", "ΠΑΡΙΣΙ"),
            ("Ποιός είναι ο μεγαλύτερος ωκεανός της γης;", "ΕΙΡΗΝΙΚΟΣ"),
            ("Ποιό είναι το αντίθετο του 'ΠΑΝΩ';", "ΚΑΤΩ"),
            ("Ποιός είναι ο τελευταίος τετραψήφιος αριθμός;", "9999"),
            ("Ποιό είναι το ψηλότερο βουνό του κόσμου;", "ΕΒΕΡΕΣΤ"),
            ("Ποιά είναι η πρωτεύουσα της Ελλάδας;", "ΑΘΗΝΑ"),
            ("Ποιός είναι ο μικρότερος πλανήτης στο ηλιακό μας σύστημα;", "ΕΡΜΗΣ"),
            ("Ποιός είναι ο διάσημος επιστήμονας ο οποίος ανακάλυψε την θεωρία της σχετικότητας;", "ΑΙΝΣΤΑΙΝ"),
            ("Ποιά είναι η τετραγωνική ρίζα του 256;", "16"),
            ("Ποιός είναι ο επόμενος αριθμός στην ακολουθία: 1, 4, 9, 16, 25, ...", "36"),
            ("Ποιά χώρα έχει τον μεγαλύτερο πληθυσμό του κόσμου;", "ΙΝΔΙΑ"),
            ("Ποιά είναι η μεγαλύτερη έρημος του κόσμου;", "ΣΑΧΑΡΑ"),
            ("Πότε τελείωσε ο 2ος Παγκόσμιος Πόλεμος;", "1945")
        ]
        self.score = score


    def submit_answer(self):
        #Συνάρτηση υποβολής απάντησης
        answer = self.answer_entry.get().upper()
        correct_answer = self.questions[self.question_index][1].upper()
        if answer == correct_answer:
            self.score += 1
            global score
            score += 1
            self.question_label.config(fg="green", text="Σωστά!")
        else:
            self.question_label.config(fg="red", text="Λάθος!")
        self.score_label.config(text="Σκορ: {}".format(self.score))
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
            
            # Παρουσίαση τελικού σκορ και του μηνύματος
            final_score = "Τελικό Σκορ: {}/{}".format(self.score, 19)
            if self.score >= 15:
                message = "Συγχαρητήρια! Είσαι ιδιοφυία!"
            elif self.score >= 10:
                message = "Τα πήγες αερκετά καλά! Είσαι περισσότερο εφυής από το μέσο όρο."
            elif self.score >= 5:
                message = "Όχι και άσχημα! Έχεις μια μέση εφυία."
            else:
                message = "Ουπς! Ίσως θα έπρεπε να διαβάζεις περισσότερο."
            result_window = tk.Toplevel(self.master)
            result_window.title("Αποτέλεσμα IQ τεστ")
            # Λήψη του πλάτους και του ύψους της οθόνης
            screen_width = result_window.winfo_screenwidth()
            screen_height = result_window.winfo_screenheight()

            # Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)

            
            # Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
            result_window.geometry(f"+{x}+{y}")

            tk.Label(result_window, text=final_score, font=("Helvetica", 16)).pack()
            tk.Label(result_window, text=message, font=("Helvetica", 16)).pack()

    def display_next_question(self):
        #Συνάρτηση παρουσίασης της επόμενης ερώτησης
        self.question_label.config(text="Eρώτηση {}: {}".format(self.question_index + 1, self.questions[self.question_index][0]), fg="black")
        self.submit_button.config(state=tk.ACTIVE)

    def display_final_score(self):
        # Συνάρτηση εμφάνησης του τελικού σκορ
        self.question_label.config(text="Τελείωσες το IQ τεστ!", fg="black")
        self.answer_entry.delete(0, tk.END)
        self.answer_entry.config(state=tk.DISABLED)
        self.submit_button.config(state=tk.DISABLED)
        self.master.after(1000, self.show_final_score)

    def show_final_score(self):
        final_message = "Πέτυχες {} στα {}!".format(self.score, 19)
        self.score_label.config(text=final_message)
        # Προγραμματισμός της καταστροφ΄ής του παραθύρου μετά από ενα λεπτό
        root.after(2000, root.destroy)


root = tk.Tk()
app = IQTestGUI(root)

# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Ορισμός του μεγέθους της ομάδας
window_width = 1050
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}") 
root.mainloop()

# Πέρασμα της μεταβλητης στο κύριο πρόγραμμα
print(score)
