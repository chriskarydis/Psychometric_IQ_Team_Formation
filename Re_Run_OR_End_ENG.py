import tkinter as tk
from tkinter import messagebox

def re_run():
    messagebox.showinfo("Re-run", "You have chosen to re-run the tests.")
    print(1)
    root.destroy()

def close():
    messagebox.showinfo("Close", "You have chosen to close the tests.")
    print(0)
    root.destroy()

root = tk.Tk()
root.title("Re-run or Close")
# Get the screen width and height
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Set the window size
window_width = 300
window_height = 150
root.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
root.geometry(f"+{x}+{y}")  

label = tk.Label(root, text="Do you want to re-run the tests or close them?")
label.pack(pady=10)

re_run_button = tk.Button(root, text="Re-run", command=re_run)
re_run_button.pack(pady=5)

close_button = tk.Button(root, text="Close", command=close)
close_button.pack(pady=5)

root.mainloop()
