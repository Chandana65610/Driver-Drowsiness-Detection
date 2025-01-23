# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:13:03 2023

@author: Anwesha Sarangi
"""

import tkinter as tk
import webbrowser
import os


# Create a function that will be called when the hyperlink is clicked
def hyperlink_clicked():
    webbrowser.open("https://www.google.com")
# Define a dictionary to store the login credentials
login_data = {"admin": {"password": "password", "mobile": "9876543210", "sos": "911"}, 
              "user1": {"password": "1234", "mobile": "9876543211", "sos": "112"}}

# Create a function that will be called when the login button is clicked
def login_button_clicked():
    username = username_entry.get()
    password = password_entry.get()
    mobile_number = mobile_entry.get()
    sos_number = sos_entry.get()
    
    if username in login_data and login_data[username] == password:
        login_label.config(text="Login successful!", fg="green")
        
        # Create a "Start Application" button
        start_button = tk.Button(window, text="click next", command=start_application)
        start_button.pack()
    else:
        login_label.config(text="Login failed!", fg="red")

# Create a function that will be called when the "Start Application" button is clicked
def start_application():
    os.system("python 2page_app.py")

# Define a dictionary to store the login credentials
login_data = {"admin": "password", "user1": "1234"}

# Create a window
window = tk.Tk()

# Set the title of the window
window.title("My App")

# Set the size of the window
window.geometry("500x500")


# Create a label with some text and a hyperlink
label_text = "Welcome to my app! Click "
link_text = "here"
label = tk.Label(window, text=label_text)
label.pack()
link = tk.Label(window, text=link_text, fg="blue", cursor="hand2")
link.pack()
link.bind("<Button-1>", lambda e: hyperlink_clicked())

# Create a login frame with four entry widgets and a login button
login_frame = tk.Frame(window)
login_frame.pack()
username_label = tk.Label(login_frame, text="Username:")
username_label.grid(row=0, column=0)
username_entry = tk.Entry(login_frame)
username_entry.grid(row=0, column=1)
password_label = tk.Label(login_frame, text="Password:")
password_label.grid(row=1, column=0)
password_entry = tk.Entry(login_frame, show="*")
password_entry.grid(row=1, column=1)
mobile_label = tk.Label(login_frame, text="Mobile Number:")
mobile_label.grid(row=2, column=0)
mobile_entry = tk.Entry(login_frame)
mobile_entry.grid(row=2, column=1)
sos_label = tk.Label(login_frame, text="SOS Number:")
sos_label.grid(row=3, column=0)
sos_entry = tk.Entry(login_frame)
sos_entry.grid(row=3, column=1)
login_button = tk.Button(login_frame, text="Login", command=login_button_clicked)
login_button.grid(row=4, column=0, columnspan=2)
login_label = tk.Label(login_frame, text="")
login_label.grid(row=5, column=0, columnspan=2)

# Start the main event loop of the window
window.mainloop()