import tkinter as tk
from tkinter import messagebox

def re_run():
    # Συνάρτηση επανάληψης του πργράμματος
    messagebox.showinfo("Επανάληψη", "Επιλέξατε την επανάληψη των τεστ.")
    print(1)
    root.destroy()

def close():
    # Συνάρτηση τερματισμού του προγράμματος
    messagebox.showinfo("Τερματισμός", "Επιλέξατε τον τερματισμό των τεστ.")
    print(0)
    root.destroy()

root = tk.Tk()
root.title("Επανάληψη ή Τερματισμός")
# Λήψη του πλάτους και του ύψους της οθόνης
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

label = tk.Label(root, text="Θα θέλατε να ξανά τρέξετε τα τεστ ή να τα τερματίσετε;")
label.pack(pady=10)

re_run_button = tk.Button(root, text="Επανάληψη", command=re_run)
re_run_button.pack(pady=5)

close_button = tk.Button(root, text="Τερματισμός", command=close)
close_button.pack(pady=5)

root.mainloop()
