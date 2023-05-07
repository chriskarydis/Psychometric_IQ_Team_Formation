import tkinter as tk
import sys

# Create a new Tkinter window
window = tk.Tk()

# Set the window title
window.title("PSYCHOMETRIC Test")

# Get the screen width and height
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Set the window size
window_width = 350
window_height = 150
window.geometry(f"{window_width}x{window_height}")

# Calculate the x and y coordinates for the top-left corner of the window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# Set the position of the window to the center of the screen
window.geometry(f"+{x}+{y}") 

# Create a label with the welcome message
welcome_label = tk.Label(window, text="Welcome to Psychometric Test!", font=("Arial", 16))
welcome_label.pack(pady=20)

# Create a bigger start button
start_button = tk.Button(window, text="Start", font=("Arial", 16), command=sys.exit)
start_button.pack(pady=10)

# Run the Tkinter event loop
window.mainloop()
