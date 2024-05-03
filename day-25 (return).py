#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_6_and_8():
  roll_6_sided_dice = rollDice(6)
  roll_8_sided_dice = rollDice(8)
  health = roll_6_sided_dice * roll_8_sided_dice
  return health

print("⚔️Character stats generator⚔️")
  

haveACharacter = "yes"

while haveACharacter == "yes":
  character = input("Name your warrior: ")
  health = str(roll_6_and_8())
  print("Their health is ", health,"hp" ) 
  haveACharacter = input("Want to create another character?")


# In[ ]:




