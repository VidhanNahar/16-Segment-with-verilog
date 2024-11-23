import tkinter as tk
from tkinter import messagebox
import subprocess

def send_to_verilog():
    # Get user input
    characters = character_entry.get().upper()
    
    if len(characters) != 6 or not characters.isalpha():
        messagebox.showerror("Invalid Input", "Please enter exactly six alphabet characters (A-Z).")
        return
    
    # Write the characters input to a file
    with open("character_input.txt", "w") as file:
        file.write(characters)
        
    try:
        subprocess.run(['vvp','project_temp_tb.vvp'],check=True)
    except subprocess.CalledProcessError as e:
        print("Connecting to Verilog", e)
                       
    
    # Display a success message
    messagebox.showinfo("Success", "The characters have been sent to the Verilog testbench.")
    
    # Close the program
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Alphabet to 16-Segment Display")

# Create and place the widgets
tk.Label(root, text="Enter Six Alphabet Characters (A-Z):").pack(pady=5)
character_entry = tk.Entry(root)
character_entry.pack(pady=5)
tk.Button(root, text="Send to Verilog", command=send_to_verilog).pack(pady=5)

# Run the main loop
root.mainloop()

pyPath = r"C:/Users/Dell/AppData/Local/Programs/Python/Python313/python.exe"
mainPath = r"C:\Users\Dell\Documents\GitHub\16-Segment-with-verilog"
subprocess.run([pyPath, "./temp_combined_gui.py"], check=True, cwd=mainPath)

