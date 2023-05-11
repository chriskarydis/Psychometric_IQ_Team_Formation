import tkinter as tk
from tkinter import messagebox
from tkinter import *
import hashlib
import re
import sqlite3
import subprocess

#loop program variable / βρόγχος που εξαρτάται από την μεταβλτητή run
run = 1

while run == 1:
    # Δημιουργία νέου παράθυρο Tkinter
    window = tk.Tk()

    # Καθορισμός τίτλου του παραθύρου

    # Λήψη του πλάτους και του ύψους της οθόνης
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Ορισμός του μεγέθους
    window_width = 500
    window_height = 200
    window.geometry(f"{window_width}x{window_height}")
    # Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
    x = (screen_width // 2) - (window_width // 2)
    y = (screen_height // 2) - (window_height // 2)

    # Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
    window.geometry(f"+{x}+{y}")

    # Δημιουρ΄γστε ένα label με το μύνημα καλοσορίσματος
    welcome_label = tk.Label(window, text="Welcome to our App! / \n Καλωσήρθατε στην εφαρμογή μας!", font=("Arial", 16))
    welcome_label.pack(pady=20)

    #Ορισμός συναρτήσεων
    def close_window():
        window.destroy()

    # Create a bigger start button
    start_button = tk.Button(window, text="Let's Begin! / Ας ξεκινήσουμε!", font=("Arial", 16), command=close_window)
    start_button.pack(pady=10)

    # Run the Tkinter event loop
    window.mainloop()

    #______________________________________WELCOME / ΚΑΛΩΣΟΡΙΣΜΑ____________________________________________________

    class Preferences:
        def __init__(self, master):
            self.master = master
            self.master.title("Team Formation")

            # Get the screen width and height
            screen_width = self.master.winfo_screenwidth()
            screen_height = self.master.winfo_screenheight()

            # Set the window size
            window_width = 450
            window_height = 200
            self.master.geometry(f"{window_width}x{window_height}")

            # Calculate the x and y coordinates for the top-left corner of the window
            x = (screen_width // 2) - (window_width // 2)
            y = (screen_height // 2) - (window_height // 2)

            # Set the position of the window to the center of the screen
            self.master.geometry(f"+{x}+{y}")
            
            self.order = tk.IntVar()
            self.stud_count = tk.IntVar()
            self.team_count = tk.IntVar()
            self.team_size = tk.IntVar()
            
            self.create_widgets()
            
        def create_widgets(self):
            # Language selection/Επιλογή γλώσσας
            tk.Label(self.master, text="Select your preferred language / Επιλέξτε την γλώσσα που προτιμάτε:").pack()
            
            self.language = tk.StringVar(value="English")
            tk.Radiobutton(self.master, text="English / Αγγλικά", variable=self.language, value="English").pack()
            tk.Radiobutton(self.master, text="Greek / Ελληνικά", variable=self.language, value="Greek").pack()
            
            # Test selection/Επιλογή τεστ
            tk.Label(self.master, text="Which test would you like to take first? / Ποιό τεστ θα θέλατε να κάνετε πρώτα;").pack()
            
            tk.Radiobutton(self.master, text="IQ", variable=self.order, value=0).pack()
            tk.Radiobutton(self.master, text="Psychometric / Ψυχομετρικό", variable=self.order, value=1).pack()
            
            # Submit button/Κουμπί υποβολής
            tk.Button(self.master, text="Submit / Υποβολή", command=self.submit).pack()
            
        def submit(self):
            # Retrieve values/Εκχώρηση τιμών από τον χρήστη
            global lang, order
            lang = self.language.get()
            order = "IQ" if self.order.get() == 0 else "Psychometric"
                 
            # Display results/Παρουσίαση αποτελεσμάτων
            result = f"Language / Γλώσσα: {lang}\nTest / Τεστ: {order}\n"
            tk.messagebox.showinfo("Results", result)
            self.master.destroy()  # close the program/Κλείσιμο προγράμματος

    root = tk.Tk()
    app = Preferences(root)
    root.mainloop()

    #______________________________________UPDATE USER / ΑΝΑΝΕΩΣΗ ΧΡΗΣΤΗ____________________________________________________

    def update_user_eng(username, value, field_to_update):
        # Funtion the days lke before
        try:
            conn = sqlite3.connect("users.db")
            c = conn.cursor()
            c.execute("UPDATE users SET " + field_to_update + "=? WHERE username=?", (value, username))
            conn.commit()
            conn.close()
            print("Update successful")
        except sqlite3.Error as e:
            print("An error occurred:", e)
            messagebox.showerror("Error!", "Failed to update user.")


    def update_user_gr(username, value, field_to_update):
            # Συνάρτηση για αλλαγη του ονόματος και κάποιο εμαιλ
            try:
                conn = sqlite3.connect("users.db")
                c = conn.cursor()
                c.execute("UPDATE users SET " + field_to_update + "=? WHERE username=?", (value, username))
                conn.commit()
                conn.close()
                print("Επιτυχής Αλλαγή")
            except sqlite3.Error as e:
                print("Ένα σφάλμα προέκυψε:", e)
                messagebox.showerror("Σφάλμα!", "Αποτυχία ανανέωσης του χρήστη.")

    if lang == "English":
        #______________________________________LOGIN AND REGISTER____________________________________________________

        class LoginWindow:
            def __init__(self, master):
                self.master = master
                master.title("Login")
                
                # Get the screen width and height
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()

                # Set the window size
                window_width = 200
                window_height = 120
                self.master.geometry(f"{window_width}x{window_height}")

                # Calculate the x and y coordinates for the top-left corner of the window
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)

                # Set the position of the window to the center of the screen
                self.master.geometry(f"+{x}+{y}")

                # create login form
                self.label_username = Label(master, text="Username")
                self.label_password = Label(master, text="Password")

                self.entry_username = Entry(master)
                self.entry_password = Entry(master, show="*")

                self.label_username.grid(row=0, column=0)
                self.label_password.grid(row=1, column=0)
                self.entry_username.grid(row=0, column=1)
                self.entry_password.grid(row=1, column=1)

                # create login and register buttons
                self.login_button = Button(master, text="Login", command=self.login)
                self.login_button.grid(row=2, column=0, columnspan=2, pady=5)

                self.register_button = Button(master, text="Register", command=self.register)
                self.register_button.grid(row=3, column=0, columnspan=2, pady=5)

                # create a connection to the SQLite database
                self.connection = sqlite3.connect("users.db")

                # create the users table if it doesn't exist
                self.cursor = self.connection.cursor()
                self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, team_role TEXT, score INTEGER, language_preference TEXT)")
                self.connection.commit()




            # Define a function to show a message about the password criteria
            def show_password_criteria_message(self):
                message = "Your password must meet the following requirments:\n\n"
                message += "- Minimum length: 8 characters\n"
                message += "- At least one lowercase letter\n"
                message += "- At least one uppercase letter\n"
                message += "- At least one digit\n"
                message += "- At least one special character: @$!%*?&\n"
                message += "\nPlease try again with a valid password."
                messagebox.showerror("Invalid Password", message)

            # Define functions to validate the password and the username
            def is_valid_username(self, username):
                pattern = r'^inf\d{7}$'
                return re.match(pattern, username) is not None

            def validate_password(self,password):
                """Validate that a password meets the requirements"""
                if len(password) < 8:
                    my_window.show_password_criteria_message()
                    # clear the entry widgets
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[A-Z]", password):
                    my_window.show_password_criteria_message()
                    # clear the entry widgets
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[a-z]", password):
                    my_window.show_password_criteria_message()
                    # clear the entry widgets
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[0-9]", password):
                    my_window.show_password_criteria_message()
                    # clear the entry widgets
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[!@#$%^&*()_+-=]", password):
                    my_window.show_password_criteria_message()
                    # clear the entry widgets
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                return True

            def hash_password(self, password):
                """Hashes a password using the SHA-256 algorithm"""
                salt = b'mysalt'  # add a salt for extra security
                password = password.encode('utf-8') + salt
                hashed_password = hashlib.sha256(password).hexdigest()
                return hashed_password



            def login(self):
                global username
                username = self.entry_username.get()
                password = self.entry_password.get()

                # hash the password
                hashed_password = my_window.hash_password(password)

                # check if the username and hashed password are in the database
                self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
                user = self.cursor.fetchone()

                if user:
                    # login successful
                    messagebox.showinfo("Success!", "Login successful.")
                    update_user_eng(username, lang, 'language_preference')
                    self.master.destroy()  # close the program
                else:
                    # login failed
                    messagebox.showerror("Error!", "Invalid username or password.")

            def register(self):
                # create a new registration window and store it as an instance variable
                self.registration_window = Toplevel(self.master)
                self.registration_window.title("Register")


                # Get the screen width and height
                screen_width = self.registration_window.winfo_screenwidth()
                screen_height = self.registration_window.winfo_screenheight()

                # Set the window size
                window_width = 250
                window_height = 120
                self.registration_window.geometry(f"{window_width}x{window_height}")

                # Calculate the x and y coordinates for the top-left corner of the window
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)

                # Set the position of the window to the center of the screen
                self.registration_window.geometry(f"+{x}+{y}")    

                # create registration form
                self.label_new_username = Label(self.registration_window, text="New Username")
                self.label_new_password = Label(self.registration_window, text="New Password")
                self.label_confirm_password = Label(self.registration_window, text="Confirm Password")

                self.entry_new_username = Entry(self.registration_window)
                self.entry_new_password = Entry(self.registration_window)
                self.entry_confirm_password = Entry(self.registration_window, show="*")

                self.label_new_username.grid(row=0, column=0)
                self.label_new_password.grid(row=1, column=0)
                self.label_confirm_password.grid(row=2, column=0)

                self.entry_new_username.grid(row=0, column=1)
                self.entry_new_password.grid(row=1, column=1)
                self.entry_confirm_password.grid(row=2, column=1)

                # create a submit button
                self.submit_button = Button(self.registration_window, text="Submit", command=self.submit_registration)
                self.submit_button.grid(row=3, column=0, columnspan=2, pady=5)

                #information about the username
                messagebox.showinfo("Be Careful!", "Your username must be like the following: inf2023987.")

                self.registration_window.tkraise()


            def submit_registration(self):
                # get the username and password from the entry widgets
                new_username = self.entry_new_username.get()
                new_password = self.entry_new_password.get()
                confirm_password = self.entry_confirm_password.get()

                # validate the username and password
                if not self.is_valid_username(new_username):
                    messagebox.showerror("Invalid Username!", "The username must be in the format inf followed by 7 digits.")
                    return
                elif not self.validate_password(new_password):
                    return
                elif new_password != confirm_password:
                    messagebox.showerror("Passwords do not match!", "The new password and confirm password fields must match.")
                    return

                # hash the password
                hashed_password = self.hash_password(new_password)

                # check if the username already exists
                self.cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
                existing_user = self.cursor.fetchone()
                if existing_user:
                    messagebox.showerror("Username already exists!", "The username already exists, please choose a different one.")
                    return

                # add the new user to the database
                self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, hashed_password))
                self.connection.commit()

                # show a success message and close the registration window
                messagebox.showinfo("Success!", "Registration successful.")
                update_user_eng(new_username, lang, 'language_preference')
                # clear the entry widgets
                self.entry_new_username.delete(0, END)
                self.entry_new_password.delete(0, END)
                self.entry_confirm_password.delete(0, END)
                self.registration_window.destroy()
            
            # database connection close
            def __del__(self):
                self.connection.close()


        root = Tk()
        my_window = LoginWindow(root)
        root.mainloop()

    elif lang == "Greek":
        #______________________________________ΣΥΝΔΕΣΗ ΚΑΙ ΕΓΓΡΑΦΗ____________________________________________________

        class LoginWindow:
            def __init__(self, master):
                self.master = master
                master.title("Σύνδεση")

                # Λήψη του πλάτους και του ύψους της οθόνης
                screen_width = self.master.winfo_screenwidth()
                screen_height = self.master.winfo_screenheight()

                # Καθορισμός του μεγέθους του παραθύρου
                window_width = 200
                window_height = 120
                self.master.geometry(f"{window_width}x{window_height}")

                # Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)

                # Θέσε την θέση του συνεδρίου στο κέντρο της οθόονης
                self.master.geometry(f"+{x}+{y}")
                
                # Δημιουργία της φόρμας σύνδεσης
                self.label_username = Label(master, text="Όνομα")
                self.label_password = Label(master, text="Κωδικός")

                self.entry_username = Entry(master)
                self.entry_password = Entry(master, show="*")

                self.label_username.grid(row=0, column=0)
                self.label_password.grid(row=1, column=0)
                self.entry_username.grid(row=0, column=1)
                self.entry_password.grid(row=1, column=1)

                # Δημιουργία κουμπιών σύνδεσης και εγγραφής
                self.login_button = Button(master, text="Σύνδεση", command=self.login)
                self.login_button.grid(row=2, column=0, columnspan=2, pady=5)

                self.register_button = Button(master, text="Εγγραφή", command=self.register)
                self.register_button.grid(row=3, column=0, columnspan=2, pady=5)

                # Δημιουργία σύνδεσης με την SQLite database
                self.connection = sqlite3.connect("users.db")

                # Δημιουργία του πίνακα των χρηστών αν δεν υπάρχει ήδη
                self.cursor = self.connection.cursor()
                self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username TEXT, password TEXT, team_role TEXT, score INTEGER, language_preference TEXT)")
                self.connection.commit()




            # Ορισμός συνάρτησης για την παρουσίαση των προαπαιτήσεων του κωδικού
            def show_password_criteria_message(self):
                message = "Ο κωδικός σου πρέπει να ακολουθεί τα επόμενα κριτήρια:\n\n"
                message += "- Ελάχιστο μήκος 8 χαρακτήρες\n"
                message += "- Τουλάχιστον ένας πεζός χαρακτήρας\n"
                message += "- Τουλάχιστον ένας κεφαλαίος χαρακτήρας\n"
                message += "- Τουλάχιστον ένας αριθμός\n"
                message += "- Τουλάχιστον ένας ειδικός χαρακτήρας: @$!%*?&\n"
                message += "\nΠαρακαλώ προσπαθήστε ξανά με έναν έγκυρο κωδικό."
                messagebox.showerror("Μη έγκυρος κωδικός!", message)

            # Ορισμός συνάρτησης για την εγκυρότητα του ονόματος
            def is_valid_username(self, username):
                pattern = r'^inf\d{7}$'
                return re.match(pattern, username) is not None
            
            # Ορισμός συνάρτησης για την εγκυρότητα του κωδικού
            def validate_password(self,password):
                """Validate that a password meets the requirements"""
                if len(password) < 8:
                    my_window.show_password_criteria_message()
                    #Καθαρισμός των υποδοχών
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[A-Z]", password):
                    my_window.show_password_criteria_message()
                    #Καθαρισμός των υποδοχών
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[a-z]", password):
                    my_window.show_password_criteria_message()
                    #Καθαρισμός των υποδοχών
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[0-9]", password):
                    my_window.show_password_criteria_message()
                    #Καθαρισμός των υποδοχών
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                elif not re.search(r"[!@#$%^&*()_+-=]", password):
                    my_window.show_password_criteria_message()
                    #Καθαρισμός των υποδοχών
                    self.entry_new_username.delete(0, END)
                    self.entry_new_password.delete(0, END)
                    self.entry_confirm_password.delete(0, END)
                    return False
                return True

            def hash_password(self, password):
                """Κωδικοποίηση κωδικού με χρήση SHA-256 αλγόριθμου"""
                salt = b'mysalt'  # Προσθέση salt για έξτρα ασφάλεια
                password = password.encode('utf-8') + salt
                hashed_password = hashlib.sha256(password).hexdigest()
                return hashed_password



            def login(self):
                global username
                username = self.entry_username.get()
                password = self.entry_password.get()

                # Κωδικοποίηση κωδικού
                hashed_password = my_window.hash_password(password)

                # Έλεγχος αν το όνομα και ο κωδικοποιημένος κωδικός είναι στο database
                self.cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_password))
                user = self.cursor.fetchone()

                if user:
                    # Επιτυχής σύνδεση
                    messagebox.showinfo("Επιτυχία!", "Συνδεθήκατε επιτυχώς.")
                    update_user_gr(username, lang, 'language_preference')
                    self.master.destroy()  # Κλείσιμο προγράμματος
                    self.__del__()
                else:
                    # Η σύνδεση απέτυχε
                    messagebox.showerror("Σφάλμα!", "Μη έγκυρο όνομα ή κωδικός.")

            def register(self):
                # Δημιουργία παραθύρου εγγραφής και αποθήκευση ως μια μεταβλητή παράδειγμα
                self.registration_window = Toplevel(self.master)
                self.registration_window.title("Εγγραφή")

                self.registration_window.lift()

                # Get the screen width and height
                screen_width = self.registration_window.winfo_screenwidth()
                screen_height = self.registration_window.winfo_screenheight()

                # Set the window size
                window_width = 250
                window_height = 120
                self.registration_window.geometry(f"{window_width}x{window_height}")

                # Calculate the x and y coordinates for the top-left corner of the window
                x = (screen_width // 2) - (window_width // 2)
                y = (screen_height // 2) - (window_height // 2)

                # Set the position of the window to the center of the screen
                self.registration_window.geometry(f"+{x}+{y}")

                # Δημιουργία φόρμας εγγραφής
                self.label_new_username = Label(self.registration_window, text="Νέο όνομα")
                self.label_new_password = Label(self.registration_window, text="Νέος κωδικός")
                self.label_confirm_password = Label(self.registration_window, text="Επιβεβαίωση κωδικού")

                self.entry_new_username = Entry(self.registration_window)
                self.entry_new_password = Entry(self.registration_window)
                self.entry_confirm_password = Entry(self.registration_window, show="*")

                self.label_new_username.grid(row=0, column=0)
                self.label_new_password.grid(row=1, column=0)
                self.label_confirm_password.grid(row=2, column=0)

                self.entry_new_username.grid(row=0, column=1)
                self.entry_new_password.grid(row=1, column=1)
                self.entry_confirm_password.grid(row=2, column=1)

                # Δημιουργία κουμπιού επιλογής
                self.submit_button = Button(self.registration_window, text="Υποβολή", command=self.submit_registration)
                self.submit_button.grid(row=3, column=0, columnspan=2, pady=5)

                # Πληροφορίες σχετικά με το όνομα
                messagebox.showinfo("Προσοχή!", "Το όνομα σας θα πρέπει να είναι σαν το ακόλουθο: inf2023987.")

                self.registration_window.tkraise()


            def submit_registration(self):
                # Πάρε το όνομα και τον κωδικό από τις υποδοχές
                new_username = self.entry_new_username.get()
                new_password = self.entry_new_password.get()
                confirm_password = self.entry_confirm_password.get()

                # Έλεγξε για εγκυρότητα το όνομα και τον κωδικό
                if not self.is_valid_username(new_username):
                    messagebox.showerror("Μη έγκυρο όνομα!", "Το όνομα πρέπει να είναι: 'inf' και 7 αριθμοί.")
                    return
                elif not self.validate_password(new_password):
                    return
                elif new_password != confirm_password:
                    messagebox.showerror("Οι κωδικοί δεν ταιριάζουν!", "Ο νέος κωδικός και η επιβεβαίωσή του πρέπει να ταιρίαζουν.")
                    return

                # Κωδικοποίηση κωδικού
                hashed_password = self.hash_password(new_password)

                # Έλεγξε αν το όνομα υπάρχει ήδη
                self.cursor.execute("SELECT * FROM users WHERE username=?", (new_username,))
                existing_user = self.cursor.fetchone()
                if existing_user:
                    messagebox.showerror("Το όνομα υπάρχει ήδη!", "Το όνομα που επιλέξατε υπάρχει ήδη. Παρακαλώ εισάγετε ένα άλλο.")
                    return

                # Πρόσθεσε τον νέο χρήστη στο database
                self.cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (new_username, hashed_password))
                self.connection.commit()

                # Δείξε ένα μήνυμα και κλείσε το παράθυρο 
                messagebox.showinfo("Επιτυχία!", "Επιτυχής εγγραφή.")
                update_user_gr(new_username, lang, 'language_preference')
                # Καθάρισε τις υποδοχές
                self.entry_new_username.delete(0, END)
                self.entry_new_password.delete(0, END)
                self.entry_confirm_password.delete(0, END)
                self.registration_window.destroy()
            
            # Τερματισμός σύνδεσης με το database
            def __del__(self):
                self.connection.close()


        root = Tk()
        my_window = LoginWindow(root)
        root.mainloop()

    #______________________________________IQ AND PSYCHOMETRIC____________________________________________________

    # Define lists of scripts to run/Ορισμός λιστών των προγραμμάτων που θα τρέξουν
    scripts_eng_iq = ['IQ_Welcome_eng.py', 'IQ_eng.py','Psychometric_Welcome_eng.py','Gui_Psychometric_test_EngVersion.py','Re_Run_OR_End_ENG.py']
    scripts_gr_iq = ['IQ_Welcome_gr.py', 'IQ_gr.py','Psychometric_Welcome_gr.py','Gui_Psychometric_test_GrVersion.py','Re_Run_OR_End_GR.py']
    scripts_eng_psych = ['Psychometric_Welcome_eng.py', 'Gui_Psychometric_test_EngVersion.py','IQ_Welcome_eng.py','IQ_eng.py','Re_Run_OR_End_ENG.py']
    scripts_gr_psych = ['Psychometric_Welcome_gr.py', 'Gui_Psychometric_test_GrVersion.py','IQ_Welcome_gr.py','IQ_gr.py','Re_Run_OR_End_GR.py']

    global score, team_role

    if order == "Psychometric":
        if lang == "English":
            # Loop through the scripts and launch each one as a separate process
            for script in scripts_eng_psych:
                # Launch the script as a subprocess
                if script == 'Gui_Psychometric_test_EngVersion.py':
                    result = subprocess.check_output(['python', script]) 
                    team_role = result.decode()
                elif script == 'IQ_eng.py':
                    result = subprocess.check_output(['python', script])
                    score = result.decode()
                elif script == 'Re_Run_OR_End_ENG.py':
                    result = subprocess.check_output(['python', script])
                    run = int(result.decode())
                else:
                    process = subprocess.Popen(['python', script])
                    # Wait for the script to finish running and close its window
                    process.wait()
        elif lang == "Greek":
            # Επανέλαβε τα προγράμματα, το καθένα ως ξεχωριστή διαδικασία
            for script in scripts_gr_psych:
                # Ξεκίνα το πρόγραμμα ως υποπρόγραμμα
                if script == 'Gui_Psychometric_test_GrVersion.py':
                    result = subprocess.check_output(['python', script])
                    team_role = result.decode()
                elif script == 'IQ_gr.py':
                    result = subprocess.check_output(['python', script])
                    score = result.decode()
                elif script == 'Re_Run_OR_End_GR.py':
                    result = subprocess.check_output(['python', script])
                    run = int(result.decode())
                else:
                    process = subprocess.Popen(['python', script])
                    # Πέριμε το πρόγραμμα να τελείωσει και κλείσε το παράθυρο
                    process.wait()
    elif order == "IQ":
        if lang == "English":
            # Loop through the scripts and launch each one as a separate process
            for script in scripts_eng_iq:
                # Launch the script as a subprocess
                if script == 'IQ_eng.py':
                    result = subprocess.check_output(['python', script])
                    score = result.decode()
                elif script == 'Gui_Psychometric_test_EngVersion.py':
                    result = subprocess.check_output(['python', script])
                    team_role = result.decode()
                elif script == 'Re_Run_OR_End_ENG.py':
                    result = subprocess.check_output(['python', script])
                    run = int(result.decode())
                else:
                    process = subprocess.Popen(['python', script])
                    # Wait for the script to finish running and close its window
                    process.wait()
        elif lang == "Greek":
            # Επανέλαβε τα προγράμματα, το καθένα ως ξεχωριστή διαδικασία
            for script in scripts_gr_iq:
            # Ξεκίνα το πρόγραμμα ως υποπρόγραμμα
                if script == 'IQ_gr.py':
                    result = subprocess.check_output(['python', script])
                    score = result.decode()
                elif script == 'Gui_Psychometric_test_GrVersion.py':
                    result = subprocess.check_output(['python', script])
                    team_role = result.decode()
                elif script == 'Re_Run_OR_End_GR.py':
                    result = subprocess.check_output(['python', script])
                    run = int(result.decode())
                else:
                    process = subprocess.Popen(['python', script])
                    # Πέριμε το πρόγραμμα να τελείωσει και κλείσε το παράθυρο
                    process.wait()

    #______________________________________UPDATE TEAM ROLE/ΕΝΗΜΕΡΩΣΗ ΡΟΛΟΥ____________________________________________________

    if lang == "Greek":
        update_user_gr(username,team_role,'team_role')
        update_user_gr(username,score,'score')
    elif lang == "English":
        update_user_eng(username,team_role,'team_role')
        update_user_eng(username,score,'score')

#______________________________________CREATE TEAMS/ΔΗΜΙΟΥΡΓΙΑ ΟΜΑΔΩΝ____________________________________________________

def create_teams(team_size):
    conn = sqlite3.connect('users.db')
    c = conn.cursor()

    c.execute("SELECT username, team_role, score FROM users")
    roles = c.fetchall()

    leaders = []
    members = []
    creatives = []
    researchers = []

    for user in roles:
        if user[1] == 'Leader\r\n':
            leaders.append(user[0])
        elif user[1] == 'Member\r\n':
            members.append(user[0])
        elif user[1] == 'Creative\r\n':
            creatives.append(user[0])
        elif user[1] == 'Researcher\r\n':
            researchers.append(user[0])

    if team_size == 3:
        # create teams of 3 with at least one leader and one creative/researcher
        # Δημιυργία ομάδων 3 χρηστών με τουλάχιστον ένα Αρχηγό, ένα μέλος και έναν ερευνητή ή δημιουργικό
        teams = []
        while (leaders and (creatives or researchers) and members) or (len(leaders) + len(creatives) + len(researchers) + len(members) >= 3):
            # The way the teams are formmed based on the limitations
            # Διαδικασία δημιουργίας ομάδων με τους περιορισμούς
            if leaders:
                leader = leaders.pop(0)
                if members:
                    member = members.pop(0)
                    if len(creatives) >= len(researchers):
                        creative = creatives.pop(0)
                    else :
                        creative = researchers.pop(0)
                else:
                    creative = creatives.pop(0)
                    member = researchers.pop(0)
            else:
                if members:
                    member = members.pop(0)
                    if len(creatives) >= len(researchers):
                        creative = creatives.pop(0)
                    else:
                        creative = researchers.pop(0)
                else:
                    if creatives and researchers:
                        if len(creatives) >= 2:
                            leader = creatives.pop(0) 
                        elif len(researchers) >= 2:
                            leader = researchers.pop(0)
                        creative = creatives.pop(0)
                        member = researchers.pop(0)
                    elif researchers:
                        leader = researchers.pop(0)
                        creative = researchers.pop(0)
                        member = researchers.pop(0)
                    elif creatives:
                        leader = creatives.pop(0)
                        creative = creatives.pop(0)
                        member = creatives.pop(0)
            team = [leader, creative, member]
            teams.append(team)
        remaining_users = leaders + members + creatives + researchers
        if remaining_users:
            if len(remaining_users) == 2:
                team = remaining_users
                teams.append(team)
            elif len(remaining_users) == 1:
                team = remaining_users
                teams.append(team)
                team_text = "\n"
                for i, team in enumerate(teams):
                    if lang == "English":
                        team_text += f"Team {i+1}:\n"
                    elif lang == "Greek":
                        team_text += f"Ομάδα {i+1}:\n"
                    # loop over each user in the team and add their username and team_role to team_text
                    # Επανέλαβε για κάθε χρήστη στην ομάδα την εισαγωγή του ονόματος και του ρόλου στο κείμενο της ομάδας
                    for user in team:
                        c.execute("SELECT team_role, score FROM users WHERE username = ?", (user,))
                        team_role, score = c.fetchone()
                        team_text += f"{user} ({team_role.strip()}), score: {score}\n"
                    team_text += "\n"  # add a newline character after each team / Προσθήκη νέας γραμμής μετά από κάθε ο΄μαδα

                if lang == "English":
                    messagebox.showinfo("Teams created", team_text)
                elif lang == "Greek":
                    messagebox.showinfo("Δημιουργία ομάδων", team_text)
                c.close()
                return
    else:
        teams = []
        # create teams of 4 with one of each role
        # Δημιουργία ομάδων 4 χρηστών με ένα χρήστη από κάθε ρόλο
        while (leaders and creatives and researchers and members) or (len(leaders) + len(creatives) + len(researchers) + len(members) >= 4):
            # The way the teams are formmed based on the limitations
            # Διαδικασία δημιουργίας ομάδων με τους περιορισμούς
            if leaders:
                leader = leaders.pop(0)
                if members:
                    member = members.pop(0)
                    if creatives:
                        creative = creatives.pop(0)
                        if researchers:
                            researcher = researchers.pop(0)
                        else:
                            print("We have problem")
                    elif researchers:
                        if len(researchers) >= 2:
                            researcher = researchers.pop(0)
                            creative = researchers.pop(0)
                        else:
                            print("We have problem")
                else:    
                    if len(creatives) >= 3:
                        member = creatives.pop(0)
                        creative = creatives.pop(0)
                        researcher = creatives.pop(0)
                    elif len(researchers) >= 3:
                        member = researchers.pop(0)
                        researcher = researchers.pop(0)
                        creative = researchers.pop(0)
                    elif len(creatives) >= 2:
                        member = creatives.pop(0)
                        creative = creatives.pop(0)
                        if researchers:
                            researcher = researchers.pop(0)
                        else:
                            print("We have problem")
                    elif len(researchers) >= 2:
                        member = researchers.pop(0)
                        researcher = researchers.pop(0)
                        if creatives:
                            creative = creatives.pop(0)
                        else:
                            print("We have problem")
                    else:
                        print("We have problem")
            else:
                if members:
                    member = members.pop(0)
                    if len(creatives) >=3:
                        researcher = creatives.pop(0)
                        creative = creatives.pop(0)
                        leader = creatives.pop(0)
                    elif len(researchers) >= 3:
                        researcher = researchers.pop(0)
                        creative = researchers.pop(0)
                        leader = researchers.pop(0)
                    elif len(creatives) >= 2:
                        leader = creatives.pop(0)
                        creative = creatives.pop(0)
                        if researchers:
                            researcher = researchers.pop(0)
                        else:
                            print("We have problem")
                    elif len(researchers)>=2:
                        leader = researchers.pop(0)
                        researcher = researchers.pop(0)
                        if creatives:
                            creative = creatives.pop(0)
                        else:
                            print("We have problem")
                    else:
                        print("We have problem")
                else:
                    if len(researchers) >= 4:
                        member = researchers.pop(0)
                        researcher = researchers.pop(0)
                        leader = researchers.pop(0)
                        creative = researchers.pop(0)
                    elif len(creatives) >= 4:
                        member = creatives.pop(0)
                        creative = creatives.pop(0)
                        leader = creatives.pop(0)
                        researcher = creatives.pop(0)
                    elif len(researchers) >= 3:
                        leader = researchers.pop(0)
                        member = researchers.pop(0)
                        researcher = researchers.pop(0)
                        if creatives:
                            creative = creatives.pop(0)
                        else:
                            print("We have problem")
                    elif len(creatives) >= 3:
                        leader = creatives.pop(0)
                        member = creatives.pop(0)
                        creative = creatives.pop(0)
                        if researchers:
                            researcher = researchers.pop(0)
                        else:
                            print("We have problem")
                    elif len(researchers) >=2:
                        member = researchers.pop(0)
                        researcher = researchers.pop(0)
                        if len(creatives) >= 2:
                            leader = creatives.pop(0)
                            creative = creatives.pop(0)
                        else:
                            print("We have problem")
                    elif len(creatives) >= 2:
                        member = creatives.pop(0)
                        creative = creatives.pop(0)
                        if len(researchers) >= 2:
                            researcher = researchers.pop(0)
                            leader = creatives.pop(0)
                        else:
                            print("We have problem")
                    else:
                        print("We have problem")

            team = [leader, researcher, creative, member]
            teams.append(team)
        remaining_users = leaders + members + creatives + researchers
        if remaining_users:
            if len(remaining_users) == 3:
                team = remaining_users
                teams.append(team)
            elif len(remaining_users) == 2:
                team = remaining_users
                teams.append(team)
            elif len(remaining_users) == 1:
                team = remaining_users
                teams.append(team)

    # initialize team_text / Αρχικοπποίηση του κειμένου ομάδας
    team_text = "\n"

    for i, team in enumerate(teams):
        if lang == "English":
            team_text += f"Team {i+1}:\n"
        elif lang == "Greek":
            team_text += f"Ομάδα {i+1}:\n"
        # loop over each user in the team and add their username and team_role to team_text
        # Επανέλαβε για κάθε χρήστη στην ομάδα την εισαγωγή του ονόματος και του ρόλου στο κείμενο της ομάδας
        for user in team:
            c.execute("SELECT team_role, score FROM users WHERE username = ?", (user,))
            team_role, score = c.fetchone()
            team_text += f"{user} ({team_role.strip()}), score: {score}\n"
        team_text += "\n"  # add a newline character after each team / Προσθήκη νέας γραμμής μετά από κάθε ο΄μαδα

    if lang == "English":
        messagebox.showinfo("Teams created", team_text)
    elif lang == "Greek":
        messagebox.showinfo("Δημιουργία ομάδων", team_text)

    c.close()


def close_window_eng():
    # Function to close the team formmation in English
    messagebox.showinfo("Close Team Formation", "You select to close the team formation app!")
    window.destroy()

def close_window_gr():
    # Συνάρτηση για τον τερματισμό του σχηματισμού ομάδων στα Ελληνικά
    messagebox.showinfo("Τερματισμός", "Επιλέξατε να τερματίσετε την διαδικασία σχηματισμού ομάδων!")
    window.destroy()

window = tk.Tk()
window.title("Team Creator")

# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 450
window_height = 200
window.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
window.geometry(f"+{x}+{y}") 

# add / Προσθήκη label
if lang == "English":
    label = tk.Label(window, text="Press the 'Create teams' button to form the teams")
elif lang == "Greek":
    label = tk.Label(window, text="Πατήστε το κουμπί 'Σχηματισμός ομάδων' για να δημιουργηθούν οι ομάδες")
label.pack()

# add radio buttons for team size / Προσθήκη κουμπιών για το μέγεθος των ομάδων
team_size_var = tk.StringVar(value="3")
team_size_frame = tk.Frame(window)
if lang == "English":
    team_size_label = tk.Label(team_size_frame, text="Team size:")
elif lang == "Greek":
    team_size_label = tk.Label(team_size_frame, text="Μέγεθος ομάδας:")
team_size_label.pack(side=tk.LEFT)
if lang == "English":
    team_size_3 = tk.Radiobutton(team_size_frame, text="3 users", variable=team_size_var, value="3")
elif lang == "Greek":
    team_size_3 = tk.Radiobutton(team_size_frame, text="3 χρήστες", variable=team_size_var, value="3")
team_size_3.pack(side=tk.LEFT)
if lang == "English":
    team_size_4 = tk.Radiobutton(team_size_frame, text="4 users", variable=team_size_var, value="4")
elif lang == "Greek":
    team_size_4 = tk.Radiobutton(team_size_frame, text="4 χρήστες", variable=team_size_var, value="4")
team_size_4.pack(side=tk.LEFT)

team_size_frame.pack()
if lang == "English":
    end_button = tk.Button(window, text="Close", font=("Arial"), command=close_window_eng)
    create_teams_button = tk.Button(window, text="Create teams", command=lambda: create_teams(int(team_size_var.get())))
elif lang == "Greek":
    end_button = tk.Button(window, text="Τερματισμός", font=("Arial"), command=close_window_gr)
    create_teams_button = tk.Button(window, text="Σχηματισμός ομάδων", command=lambda: create_teams(int(team_size_var.get())))
create_teams_button.pack()
end_button.pack(pady=10)

window.mainloop()

#_________________________________________DISPLAY DATA/ΠΑΡΟΥΣΙΑΣΗ ΔΕΔΟΜΕΝΩΝ______________________________________
# Create a connection to the database / Δημιουργία σύνδεσης με το database
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Define a function to retrieve data from the database and display it in the GUI 
def display_scores_eng():
    # Execute a SELECT statement to retrieve the data
    c.execute("SELECT username, team_role, score FROM users ORDER BY score DESC")
    data = c.fetchall()

    # Create a new window for displaying the data
    scores_window = tk.Toplevel(root)
    scores_window.title("Display Data")

    # Set the position of the window to the right of the main window
    scores_window.geometry(f"+{x + window_width + 10}+{y}")

    # Create a canvas to hold the table
    canvas = tk.Canvas(scores_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(scores_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a table to display the data
    table = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor='nw')

    # Create labels for the table headers
    headers = ("Username", "Team Role", "Score")
    for j, header in enumerate(headers):
        tk.Label(table, text=header, padx=10, pady=5, font=("TkDefaultFont", 12, "bold")).grid(row=0, column=j)

    # Create labels for the data
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            # If the current column is team_role and it's not the first row, add a newline character before the text
            if j == 1 and i >= 0:
                val = "\n\n" + val
            tk.Label(table, text=val, padx=10, pady=5).grid(row=i+1, column=j)

    # Update the canvas to show the table
    table.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    close_button = tk.Button(scores_window, text="Close", command=scores_window.destroy)
    close_button.pack(pady=5)

# Ορισμός συνάρτησης για ανάκτηση δεδομένων απο την βάση δεδομένων ανδ απεικόνισή τους στο GUI
def display_scores_gr():
    # Εκτέλεσε ένα SELECT statement για να ανακτήσεις τα δεδομένα
    c.execute("SELECT username, team_role, score FROM users ORDER BY score DESC")
    data = c.fetchall()

    # Δημιουργία νέου παραθύρου για την παρουσίαση των δεδομένων
    scores_window = tk.Toplevel(root)
    scores_window.title("Παρουσίαση χρηστών")

    # Τοποθέτησε το παράθυρο στα δεξία του κύριου παραθύρου
    scores_window.geometry(f"+{x + window_width + 10}+{y}")

    # Δημιούργησε ένα κανβά για την κράτηση του πίνακα
    canvas = tk.Canvas(scores_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Προσθήκη scrollbar στον κανβα
    scrollbar = tk.Scrollbar(scores_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Δημιουργία πίνακα για παρουσίαση δεδομένων
    table = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor='nw')

    # Δημιουργία labels για τους τίτλους του πίνακα
    headers = ("Username", "Ρόλος στην Ομάδα", "Σκορ")
    for j, header in enumerate(headers):
        tk.Label(table, text=header, padx=10, pady=5, font=("TkDefaultFont", 12, "bold")).grid(row=0, column=j)

    # Δημιούργησε labels για τα δεδομένα
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            # Αν η τρέχουσα στήλη είναι η team_role και δεν είναι η πρώτη γραμμή, πρόσθεσε ένα χαραλτήρα νέας γραμμής πριν το κείμενο
            if j == 1 and i >= 0:
                val = "\n\n" + val
            tk.Label(table, text=val, padx=10, pady=5).grid(row=i+1, column=j)

    # Αννανέωσε τον κανβά για να δείξει τα επόμενα
    table.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    close_button = tk.Button(scores_window, text="Τερματισμός", command=scores_window.destroy)
    close_button.pack(pady=5)


def display_highest_score_eng():
    # Execute a SELECT statement to retrieve the data
    c.execute("SELECT username, score FROM users WHERE score = (SELECT MAX(score) FROM users)")
    data = c.fetchall()

    # Create a new window for displaying the data
    highest_score_window = tk.Toplevel(root)
    highest_score_window.title("Display Highest Scores")

    # Set the position of the window to the left of the main window
    highest_score_window.geometry(f"+{x - window_width - 150}+{y}")

    # Create a canvas to hold the table
    canvas = tk.Canvas(highest_score_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Add a scrollbar to the canvas
    scrollbar = tk.Scrollbar(highest_score_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a table to display the data
    table = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor='nw')

    # Add table headers
    tk.Label(table, text='Username', padx=10, pady=5).grid(row=0, column=0)
    tk.Label(table, text='Score', padx=10, pady=5).grid(row=0, column=1)

    # Add data to the table
    for i, row in enumerate(data):
        tk.Label(table, text=row[0], padx=10, pady=5).grid(row=i+1, column=0)
        tk.Label(table, text=row[1], padx=10, pady=5).grid(row=i+1, column=1)

    # Update the canvas to show the table
    table.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    close_button = tk.Button(highest_score_window, text="Close", command=highest_score_window.destroy)
    close_button.pack(pady=5)

def display_highest_score_gr():
    # Εκτέλεσε ένα SELECT statement για να ανακτήσεις τα δεδομένα
    c.execute("SELECT username, score FROM users WHERE score = (SELECT MAX(score) FROM users)")
    data = c.fetchall()

    # Δημιουργία νέου παραθύρου για την παρουσίαση των δεδομένων
    highest_score_window = tk.Toplevel(root)
    highest_score_window.title("Κορυφαία σκορ")

    # Τοποθέτησε το παράθυρο στα αριστερά του κύριου παραθύρου
    highest_score_window.geometry(f"+{x - window_width - 150}+{y}")

    # Δημιούργησε ένα κανβά για την κράτηση του πίνακα
    canvas = tk.Canvas(highest_score_window)
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Προσθήκη scrollbar στον κανβα
    scrollbar = tk.Scrollbar(highest_score_window, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    canvas.configure(yscrollcommand=scrollbar.set)

    # Δημιουργία πίνακα για παρουσίαση δεδομένων
    table = tk.Frame(canvas)
    canvas.create_window((0, 0), window=table, anchor='nw')

    # Προσθήκη τίτλων
    tk.Label(table, text='Username', padx=10, pady=5).grid(row=0, column=0)
    tk.Label(table, text='Σκορ', padx=10, pady=5).grid(row=0, column=1)

    # Προσθήκη δεδομένων στον πίνακα
    for i, row in enumerate(data):
        tk.Label(table, text=row[0], padx=10, pady=5).grid(row=i+1, column=0)
        tk.Label(table, text=row[1], padx=10, pady=5).grid(row=i+1, column=1)

    # Αννανέωσε τον κανβα για να παρουσιαστούν τα δεδομένα
    table.update_idletasks()
    canvas.configure(scrollregion=canvas.bbox('all'))

    close_button = tk.Button(highest_score_window, text="Τερματισμός", command=highest_score_window.destroy)
    close_button.pack(pady=5)

# Create the main window / Δημιουργία παραθύρου
root = tk.Tk()

# Get the screen width and height / Λήψη του πλάτους και του ύψους της οθόνης
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size / Καθορισμός του μεγέθους του παραθύρου
window_width = 300
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window / Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen / Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
root.geometry(f"+{x}+{y}")

# Create a button to display the scores / Δημιυργία κουμπιών για την παρουσίαση των σκορ
if lang == "English":
    scores_button = tk.Button(root, text="Display Scores", command=display_scores_eng)
elif lang == "Greek":
    scores_button = tk.Button(root, text="Παρουσίαση δεδομένων", command=display_scores_gr)
scores_button.pack()

def close_eng():
    messagebox.showinfo("Close", "Thank you for using our app! Goodbye!")
    root.destroy()

def close_gr():
    messagebox.showinfo("Τερματισμός", "Σας ευχαριστούμε που χρησιμοποιήσατε την εφαρμογή μας! Αντίο!")
    root.destroy()
if lang == "English":
    highest_score_button = tk.Button(root, text="Highest Score", command=display_highest_score_eng)
elif lang == "Greek":
    highest_score_button = tk.Button(root, text="Κορυφαία σκορ", command=display_highest_score_gr)
highest_score_button.pack(pady=5)

if lang == "English":
    close_button = tk.Button(root, text="Close", command=close_eng)
elif lang == "Greek":
    close_button = tk.Button(root, text="Τερματισμός", command=close_gr)
close_button.pack(pady=5)

# Run the main loop / έναρξη του κύριου βρόγχου επανάληψης
root.mainloop()

# Close the connection to the database / Τερματισμός σύνδεσης με το database
conn.close()
