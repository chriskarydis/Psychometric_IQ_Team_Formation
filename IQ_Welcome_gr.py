import tkinter as tk
import sys

# Δημιουργία νέου Tkinter παραθύρου
window = tk.Tk()

# Ορισμός τίτλου του παραθύρου
window.title("IQ Τεστ")

# Λήψη του πλάτους και του ύψους της οθόνης
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Καθορισμός του μεγέθους του παραθύρου
window_width = 350
window_height = 150
window.geometry(f"{window_width}x{window_height}")

# Υπολογισμός των Χ και Ψ συντεταγμένων για την πάνω αριστερή γωνία του παραθύρου
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Καθορισμός της θέσης του παραθύρου στο κέντρο της οθόνης
window.geometry(f"+{x}+{y}")

# Δημιούργησε ένα label με το μήνυμα καλωσορίσματος
welcome_label = tk.Label(window, text="Καλώς ορίσατε στο IQ τεστ!", font=("Arial", 16))
welcome_label.pack(pady=20)

# Δημουργία κουμπιού εκκίνησης
start_button = tk.Button(window, text="Ας ξεκινήσουμε", font=("Arial", 16), command=sys.exit)
start_button.pack(pady=10)

# Εκτελέστε τον βρόχο του Tkinter
window.mainloop()
