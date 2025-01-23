# -*- coding: utf-8 -*-
"""
Created on Mon May  8 07:18:11 2023

@author: Anwesha Sarangi
"""

import tkinter as tk
import webbrowser
from datetime import datetime, timedelta
import time
import subprocess


class MyApp(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.dest_label = tk.Label(self, text="Destination Location:")
        self.dest_label.pack()
        self.dest_entry = tk.Entry(self)
        self.dest_entry.pack()

        self.time_label = tk.Label(self, text="Estimated Time to Arrival (in minutes):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self)
        self.time_entry.pack()

        self.submit_button = tk.Button(self, text="Submit", command=self.calculate_arrival_time)
        self.submit_button.pack()

        self.result_label = tk.Label(self, text="")
        self.result_label.pack()

        self.run_button = tk.Button(self, text="START THE APPLICATION", command=self.run_next_file)
        self.run_button.pack()

    def calculate_arrival_time(self):
        destination = self.dest_entry.get()
        time_estimate = int(self.time_entry.get())
        current_time = datetime.now()
        arrival_time = current_time + timedelta(minutes=time_estimate)
        arrival_time_str = arrival_time.strftime("%m/%d/%Y %I:%M %p")
        self.result_label.config(text=f"You will arrive at {destination} at {arrival_time_str}.")

    def run_next_file(self):
        subprocess.run(['python', '3page_app.py'])
        time.sleep(5)
        self.master.destroy()
        subprocess.run(['python', '4page_app.py'])
        time.sleep(5)  # Wait for 5 seconds
        self.master.destroy()


root = tk.Tk()
root.geometry("500x500")
app = MyApp(master=root)
app.mainloop()