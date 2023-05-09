import tkinter as tk
import sys

class App:
    def __init__(self, master):
        self.questions = {
            1: {
                "text": "Σε ποιό χώρο αποδίδετε καλύτερα στην δουλεία σας;",
                "options": {
                    1: "Ακατάστατο γραφείο.",
                    2: "Γραφείο συνελεύσεων.",
                    3: "Χαλαρή καφετέρια.",
                    4: "Τακτοποιημένο γραφείο."
                },
                "score": 0,
                "score1": 0
            },
            2: {
                "text": "Πώς θα περιέγραφες τις ώρες που δουλεύεις?",
                "options": {
                    1: "Οι ώρες μου αλλάζουν με το πως νιώθω.",
                    2: "Δεν έχω σταθερές ώρες δουλείάς, αλλα πάντα δουλεύω.",
                    3: "Δουλεύω σταθερά και τις ίδιες ώρες συνέχεια.",
                    4: "Δουλεύω συνέχεια αρκετές ώρες, ειδικά όταν υπάρχει όριο προθεσμίας."
                },
                "score": 0,
                "score1": 1
            },
            3: {
                "text": "Ποιά είναι η αντίδραση σου οταν κάποιος απο την ομάδα καλέσει συνάντηση?",
                "options": {
                    1:"Δεν έχει σημασία αφού δεν θα πάω.",
                    2:"Έχω αρκετή δουλεία για να πάω στην συνάντηση.",
                    3:"Τέλεια, θα μπορέσω να τους πω την καινούργια μου ιδέα!",
                    4:"Εμμ... Λογικά εγώ την κάλεσα."
                },
                "score": 0,
                "score1": 2     
            },
            4: {
                "text": "Πως αντιδράς στις ομαδικές εργασίες;",
                "options": {
                    1:"Κάθε δικαιολογία για να τις αποφύγω!",
                    2:"Δεν μου αρέσει η κοινωνικοποίηση!",
                    3:"Δεν με ενθουσιάζουν αλλά οταν συμμετάσχω το απολαμβάνω.",
                    4:"Τις αγαπώ, είναι πολύ σημαντικές για την ομάδα."
                },
                "score": 0,
                "score1": 3     
            },
            5: {
                "text": "Ποια λένε για εσένα, οι συνάδελφοι σου, ότι είναι η μεγαλύτερη σου δύναμη;",
                "options": {
                    1:"Να λύνω δύσκολα προβλήματα.",
                    2:"Να βρίσκω καλές ιδεές.",
                    3:"Να μπορώ να πείσω τους άλλους να υποστηρίξουν την ομάδα.",
                    4:"Να βάζω την ομάδα στο σωστό δρόμο και να την καθοδηγώ."
                },
                "score": 0,
                "score1": 4     
            },
            6: {
                "text": "Τι σε εκνευρίζει περισσότερο στην δουλειά:",
                "options": {
                    1:"Άτομα που δεν ακολουθούν το πρόγραμμα.",
                    2:"Ανθρώποι που κάνουν μονότονη δουλειά.",
                    3:"Άτομα που τρέχουν πολύ μπροστά στην δουλεία χωρίς να την έχουν καταλάβει.",
                    4:"Όταν ξεκινάνε νέες δουλείες χωρίς να τελειώσουν τις προηγουμενες."
                },
                "score": 0,
                "score1": 5     
            },
            7: {
                "text": "Οταν αντιμετωπίζετε ένα πρόβλημα στην ομάδα, τι κάνεις:",
                "options": {
                    1:"Δεν υπάρχει περίπτωση να εκνευριστώ.",
                    2:"Θα εκνευριστώ και θα υποστηρίξω την άποψη μου έντονα.",
                    3:"Θα ενοχλειθώ και απλώς θα πάω πίσω στην δουλεία μου.",
                    4:"Θα καλέσω συνάντηση με τα άτομα της ομάδας και θα λύσουμε το θέμα."
                },
                "score": 0,
                "score1": 6    
            },
            8: {
                "text": "Τι θα έκανες αν η ομάδα σου δεν δεχόταν την ιδέα σου;",
                "options": {
                    1:"Τιποτα.",
                    2:"Θα άλλαζα την ιδέα ή θα πρόσθετα περισσότερα.",
                    3:"Θα εκνευριζόμουν.",
                    4:"Θα ξανά μιλούσα με την ομάδα μου ξανά για την ιδέα μου."
                },
                "score": 0,
                "score1": 7     
            },
            9: {
                "text": "Τι σε παθίαζει περισσότερο;",
                "options": {
                    1:"Επέκταση των δικτύων φίλων μου και της εμπειρίας μου.",
                    2:"Να σκέφτομαι νέες και δημιουργικές ιδέες.",
                    3:"Να λύνω δύσκολα προβλήματα.",
                    4:"Να διευθύνω μια παραγωγική και καλοφτιαγμένη ομάδα."
                },
                "score": 0,
                "score1": 8     
            },
            10: {
                "text": "Τι θα έκανες αν ενα άτομο απο την ομάδα σου δεν δούλευε;",
                "options": {
                    1:"Τίποτα δεν ειναι το πρόβλημα μου.",
                    2:"Θα μιλούσα με το άτομο της ομάδας μου.",
                    3:"Θα ρωτούσα το άτομο της ομάδας μου αν θέλει βοήθεια.",
                    4:"Θα έκανα εγώ την δουλειά."
                },
                "score": 0,
                "score1": 9     
            },
            # Add more questions as needed
        }

        self.current_question = 1

        self.question_label = tk.Label(master, text="")
        self.question_label.pack()

        self.line_label = tk.Label(master, text="______________________")
        self.line_label.pack()

        self.option_labels = {}
        for i in range(1, 5):#den to pirazoume
            self.option_labels[i] = tk.Label(master, text="")
            self.option_labels[i].pack()

        self.answer = tk.Entry(master)
        self.answer.pack()

        self.submit = tk.Button(master, text="Υποβολή", command=self.submit_answer)
        self.submit.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

        self.update_question()

    def update_question(self):# Poses epiloges tha dixni
        question_data = self.questions[self.current_question]
        self.question_label.config(text="Ερώτηση {}: {}".format(self.current_question, question_data["text"]))

        for i in range(1, 5):
            self.option_labels[i].config(text="{}. {}".format(i, question_data["options"][i]))

    def submit_answer(self):
        try:
            answer = int(self.answer.get())
        except ValueError:
            self.result_label.config(text="Εισαγάγετε μια έγκυρη απάντηση (1-4).")
            return

        if answer < 1 or answer >= 5:
            self.result_label.config(text="Εισαγάγετε μια έγκυρη απάντηση (1-4).")
            return

        question_data = self.questions[self.current_question]
        question_data["score"] += answer

        question_data = self.questions[self.current_question]
        question_data["score1"] += 1#To counter ton erotiseon pou apantithikan

        self.result_label.config(text="Το συνολικό σκορ σου {} είναι: {}".format(self.current_question, question_data["score"]))
        self.result_label.config(text="Το συνολικό σκορ των απαντήσεων: {}".format( question_data["score1"]))# Oi sinolikes erotisis pou apantithikan

        self.current_question += 1

        if self.current_question > len(self.questions): #elegxei an apomenoun alles ervthseis gia na rvthsei alliws stamataei
            self.show_final_score()
        else:
            self.update_question()

        self.answer.delete(0, tk.END)

    def show_final_score(self):
        # Αφαίρεση της τελευταίας ερώτησης
        self.question_label.pack_forget()
        self.line_label.pack_forget()
        for i in range(1, 5):
            self.option_labels[i].pack_forget()
        self.answer.pack_forget()
        self.submit.pack_forget()

        total_score = sum([question_data["score"] for question_data in self.questions.values()])
        
        global team_role
        team_role = ""

         if 10 <= total_score and total_score <= 15:
            self.result_label.config(text="Το συνολικό σκορ σου: {}\nΣυγχαριτήρια! Ο ρόλος σου είναι μέλος\nΈνα μέλος(Member) της ομάδας έχει ως σκοπό του να κάνει την δουλεία που του δόθηκε,\n να παραβρεθεί σε κάθε συνάντηση και να προσπαθεί να βρει ιδέες και λύσεις σε ένα πρόβλημα που μπορεί να υπάρξει στη υλοποίηση της δουλείας του.\n".format(total_score))   
            team_role = "Member"
        elif 15 < total_score and total_score <= 25:
            self.result_label.config(text="Το συνολικό σκορ σου: {}\nΣυγχαριτήρια! Ο ρόλος σου είναι δημιουργός!\nΟι δημιουργοί (Creative) έχουν την τάση να εγκλωβίζονται στον κόσμο της φαντασίας, της επίλυσης προβλημάτων και της σύλληψης.\n Μπορεί να μην είναι πάντα οι πιο ξεκάθαροι επικοινωνιολόγοι, διπλωμάτες ή διορθωτές, αλλά συνδυάστε τους με έναν έμπειρο αρχηγό και θα μπορούσαν σχεδόν να γίνουν θαύματα!\n Κάθε ομάδα επωφελείται από έναν δημιουργικό στοχαστή, κάποιον που μπορεί να προσφέρει νέες ιδέες και λύσεις που κάνουν τη δουλειά της ομάδας να ξεχωρίζει από το πλήθος.\n".format(total_score))
            team_role = "Creative"
        elif 25 < total_score and total_score <= 35:
            self.result_label.config(text="Το συνολικό σκορ σου: {}\nΣυγχαριτήρια! Ο ρόλος σου είναι ερευνητής!\nΟ ερευνητής (Researcher) έχει την ικανότητα να απαντά σε δύσκολες και ποικίλες ερωτήσεις με την έρευνα που κάνει.\n Με αυτό καταφέρνει να έχει παραπάνω πληροφορίες για το έργο της ομάδας και είναι το άτομο που μπορεί να βασιστεί κάποιος για την επίλυση προβλημάτων και την απάντηση δύσκολων ερωτήσεων.\n Τέλος ,έχει το φυσικό ταλέντο να ξέρει τις καλύτερες πηγές για την εύρεση πληροφοριών που συνεισφέρουν στην αντιμετώπιση του προβλήματος.\n".format(total_score))
            team_role = "Reashercher"
        else:
            self.result_label.config(text="Το συνολικό σκορ σου: {}\nΣυγχαριτήρια! Ο ρόλος σου είναι αρχηγός!\nO ρόλος αρχηγός(Leader) είναι ο ποιος σημαντικός ρόλος σε μια ομάδα, έχει ως σκοπό τον προσανατολισμό της ομάδας και την διατήρηση των κανόνων συνεργασίας των μελών.\n Ακόμη έχει τον έλεγχο της αναφοράς κάθε μέλους για το πως προχωρά το κομμάτι του.\n Επίσης, αναθέτει τους στόχους της ομάδας και βοηθά στην επιτύχια του κάθε μέλους αλλά και την ομάδα για την ολοκλήρωση των στόχων που έχουν θέσει.\n Πρέπει να είναι παρών σε όλα και συγκεντρωμένος στην ομάδα. Βοηθά επίσης στην επίλυση προβλημάτων και στο να λάβουν αποφάσεις.\n".format(total_score))
            team_role = "Leader"
        
        print(team_role)
        # Προγραμμάτησε την καταστροφή του παραθύρου σε 5 δευτερόλεπτα
        #root.after(5000, root.destroy)
        end_button = tk.Button(root, text="Κλείσιμο", font=("Arial", 12), command=sys.exit)
        end_button.pack(pady=10)

root = tk.Tk()
root.title("Ψυχομετρικό Τεστ")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 1100
window_height = 200
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}")
app = App(root)
root.mainloop()
