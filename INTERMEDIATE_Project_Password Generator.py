# ---------- ⟡ Intermediate Password Generator ⟡ ---------- #

import string
import random

def password_strength(password):
    points = 0
    if len(password) >= 8:
        points += 1
    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        points += 1
    if any(c.isdigit() for c in password):
        points += 1
    if any(c for c in password if c in string.punctuation):
        points += 1
    if len(password) >= 12:
        points += 1
    return points

def password_gen():
    number_of_inputs = 1 
    while number_of_inputs <=7 : 
        try:
            length = int(input("How many characters would you like your password to have?"))
            break 
        except ValueError:
            print("Error: Only numbers are valid imputs. Number of attempts left: " + str((7 - number_of_inputs)))
            number_of_inputs += 1 
    else:
        print("Maximun amount of attempts achieved. Try again in a few minutes.")
        return

    char = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(char) for i in range(length))


    score = password_strength(password)    
    if score == 0:
        final_score = "☆☆☆☆☆ (Unusable)"
    elif score == 1:
        final_score = "★☆☆☆☆ (Weak)"
    elif score == 2:
        final_score = "★★☆☆☆ (Decent)"
    elif score == 3:
        final_score = "★★★☆☆ (Strong)"
    elif score == 4:
        final_score = "★★★★☆ (Excellent)"
    else:
        final_score = "★★★★★ (POWERFUL)"
    
    print("Your new safe password is: " + password)
    print("Password Strength: " + final_score)

# --------------------------------------------------------- #

'''
Thank you so much for reading and testing. Let me know if there are some improvements I could do.
Byee~
⟡ Contact Info ⟡
Github - BeeluRiddle - https://github.com/BeeluRiddle
Linkedin - belenzapata6 - https://www.linkedin.com/in/belenzapata6/
'''