import tkinter as tk
from tkinter import messagebox

def send_to_verilog():
    # Get user input
    character = character_entry.get().upper()
    
    if len(character) != 1 or not character.isalpha():
        messagebox.showerror("Invalid Input", "Please enter a single alphabet character (A-Z).")
        return
    
    # Write the character input to a file
    with open("character_input.txt", "w") as file:
        file.write(character)
    
    # Display a success message
    messagebox.showinfo("Success", "The character has been sent to the Verilog testbench.")

# Create the main window
root = tk.Tk()
root.title("Alphabet to 16-Segment Display")

# Create and place the widgets
tk.Label(root, text="Enter Alphabet Character (A-Z):").pack(pady=5)
character_entry = tk.Entry(root)
character_entry.pack(pady=5)
tk.Button(root, text="Send to Verilog", command=send_to_verilog).pack(pady=5)

# Run the main loop
root.mainloop()
