# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 18:29:36 2021

@author: Julio
"""

# I want to make a cash-machine so that it gives the correct change 
# depending on:

# what is being bought
# and how much money is being paid for



# First I make a dictionary of the 'things' that are being 
# sold and their value

# For the moment the money value is integers £1,2,3,... AND 0.50 pp 

warehouse = {
    "keyboard": 24.,
    "mouse": 11.5,
    "cup": 4.5,
    "notebook1": 5.,
    "notebook2": 6.5,
    "post-its": 4.,
    "calculator": 10.5,
    "speakers": 20.,
    "plant1": 13.,
    "plant2": 11.,
    "pen": 2.5,
    "lamp": 15.,
    "monitor": 37.,
    "clock": 13.
}



# type(warehouse["keyboard"])
# warehouse.items()

# # Lets start buying one thing at a time 

# tobuy = input("Type what you want to buy: ")
# basket = warehouse[tobuy]


# # Lets give change depending on what they buy and how much they pay

# print("Total will be: £", basket)

# paymt = float(input("You inserted: " ))

# change = paymt - basket

# print("Your change is: £", change)

#--------------------------------------------------------------------------

# Since this is a very user-oriented program, I am going to create a 'window'
# so that the client interacts with it. (Just like in Sainsbury's)

# To create a GUI we will use -tkinter-


import tkinter as tk
#import PyPDF2
from PIL import Image, ImageTk

print("Hopefully this works")

# Creating the windows (interface)

root = tk.Tk()  # The beginning of window

canvas = tk.Canvas(root, width=600, height=600)
canvas.grid(columnspan=4)


# A logo can be added


#instructions

instructions = tk.Label(root, text = "Choose items to buy",
                        font="Raleway")
instructions.grid(columnspan=4, column=0, row=0)







root.mainloop() # The end of the window






















