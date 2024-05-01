#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
print("Infinity Dice 🎲")
  
sides = int(input("How many sides?: "))
playGame = "yes"
  
def rollDice(sides):
  print("You rolled ", random.randint(1,sides))
while playGame == "yes":
    rollDice(sides)
    playGame = input("Roll again?")

