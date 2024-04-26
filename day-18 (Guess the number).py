#!/usr/bin/env python
# coding: utf-8

# In[19]:


print("Welcome to the game! Guess the number between 1-100. I'll tell you if it's low, high, or correct.")
attempt = 0
correct = 50

while True:
    number = int(input("Enter number between 1-100: "))
    if number < 0:
        print("I'm done with you bloody negative people!")
        break
    elif number > correct:
        print("It's too high.")
        attempt = attempt + 1
    elif number < correct:
        print("It's too low.")
        attempt = attempt + 1
    elif number == correct:
        print("That's correct!")
        attempt = attempt + 1
        break

print("You took", attempt, "attempts to win the game.")


# In[ ]:




