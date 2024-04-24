#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

# Function to determine the winner
def determine_winner(user_choice):
    options = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(options)
    
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or \
         (user_choice == 'Paper' and computer_choice == 'Rock') or \
         (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "Computer wins!"
    
    messagebox.showinfo("Result", f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

# Create main application window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Set background color
root.configure(bg='#ffcc66')

# Function to handle button clicks
def button_click(choice):
    determine_winner(choice)

# Create buttons for Rock, Paper, and Scissors
rock_button = ttk.Button(root, text="Rock", command=lambda: button_click('Rock'))
rock_button.grid(row=0, column=0, padx=10, pady=10)

paper_button = ttk.Button(root, text="Paper", command=lambda: button_click('Paper'))
paper_button.grid(row=0, column=1, padx=10, pady=10)

scissors_button = ttk.Button(root, text="Scissors", command=lambda: button_click('Scissors'))
scissors_button.grid(row=0, column=2, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()


# In[ ]:





# In[ ]:


get_ipython().run_line_magic('run', 'demo_GUI.py')



# In[ ]:




