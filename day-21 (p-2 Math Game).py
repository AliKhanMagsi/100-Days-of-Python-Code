#!/usr/bin/env python
# coding: utf-8

# In[40]:


print("Welcome to my math Game")
print()
mult = int(input("Enter your favourite multiple: "))
print()
attempt = 0

for i in range(1, 11):
    rightAnswer = i * mult
    print(i, "x", mult)
    userAnswer = int(input(">"))  # <--- Highlighted indentation

    if userAnswer == rightAnswer:  # <--- Highlighted indentation
        print("You are genius")  # <--- Highlighted indentation
        attempt += 1  # <--- Highlighted indentation
    else:  # <--- Highlighted indentation
        print("NOOO! The right Answer is", rightAnswer)
        break# <--- Highlighted indentation
    
if attempt == 10:  # <--- Highlighted indentation
    print("Congratulations you won the Game")  # <--- Highlighted indentation
else:  # <--- Highlighted indentation
    print("Better Luck Next Time, Your score is", attempt)  # <--- Highlighted indentation


# In[ ]:





# In[ ]:




