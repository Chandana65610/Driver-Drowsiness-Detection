# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:21:43 2023

@author: Anwesha Sarangi
"""

import tkinter as tk
from tkinter import messagebox

# Create the main window of the app
root = tk.Tk()

# Function that will be called when the "Quit" button is clicked
def quit_app():
    # Display a message box to confirm if the user wants to exit the app
    if messagebox.askyesno("Quit", "Do you want to close the application?"):
        # Close the main window and exit the application
        root.destroy()
        quit()

# Create the "Quit" button
quit_button = tk.Button(root, text="Quit", command=quit_app)

# Add the "Quit" button to the main window
quit_button.pack()

root.mainloop()