# ---------- ⟡ Advanced Password Generator ⟡ ---------- #

import string
import random
import time

# ---------- Main Menu  ---------- #

print("Welcome to Beel's Password Generator.")
time.sleep(3)
print("I will ask you some questions to generate your password. To answer, simply type 'y' for yes, or 'n' for no.")
time.sleep(5)
print("Ready to start? (Y/N)")
begin = str(input("Ready to start?")) 

if begin == "y":
    print("Please run the code called 'password_gen' to begin!") 
else: 
    ask_questions = True
    while ask_questions: 
        print("Please write the corresponding letter to your question: ")
        time.sleep(3)
        print("a) What questions will I be asked?")
        print("b) Will my password be stored anywhere?")
        print("c) Where do I type the yes or no answer?")
        question = str(input("Please type a letter:"))
        
        if question == "a": 
            print("I will ask you whether or not you would like your password to have any of the following: ")
            time.sleep(3)
            print("-Lower Case characters")
            print("-Upper Case characters")
            print("-Numbers")
            print("-Special characters")
            time.sleep(3)
            
            print("Do you have any other questions?")
            menu = str(input("Y/N"))
            if menu == "n":
                ask_questions = False
        elif question == "b":
            print("As of today, the generated password will not be stored anywhere, therefore you will need to manually save it yourself if it will be used.")
            time.sleep(3)

            print("Do you have any other questions?")
            menu = str(input("Y/N"))
            if menu == "n": 
                ask_questions = False    
        else: 
            print("Simply type the letter in your keyboard and press Enter to submit your answer.")
            time.sleep(3)

            print("Do you have any other questions?")
            menu = str(input("Y/N"))
            if menu == "n":
                ask_questions = False
    
    print("Please run the code called 'password_gen' to begin!")

# ---------- Settings ---------- #

'''PERSONALIZATION'''
def include_upper_case():
    option = input("(Y/N)")
    return option.upper() == "Y"
def include_lower_case():
    option = input("(Y/N)")
    return option.upper() == "Y"
def include_numbers():
    option = input("(Y/N)")
    return option.upper() == "Y"
def include_special_characters():
    option = input("(Y/N)")
    return option.upper() == "Y"

'''PASSWORD RATING'''
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

# ---------- Generator ---------- #

def password_gen():
    number_of_imputs = 1
    while number_of_imputs <= 7:
        try:
            print("🟣 How many characters would you like your password to have?")
            length = int(input("Amount of characters"))
            print("Answer: " + str(length))
            break
        except ValueError:
            print("Error: Only numbers are valid imputs. Number of attempts left: " + str((7 - number_of_imputs)))
            number_of_imputs += 1
    else:
        print("Maximun amount of attempts achieved. Try again in a few minutes.")
        return

    char = ""
    
    print("🟣 Would you like any lower case characters?")
    lowercase = include_lower_case()
    if lowercase:
        char += string.ascii_lowercase
    print(lowercase)
    time.sleep(1)

    print("🟣 Would you like any upper case characters? ")
    uppercase = include_upper_case()
    if uppercase:
        char += string.ascii_uppercase
    print(uppercase)
    time.sleep(1)

    print("🟣 Would you like any numbers?")
    numbers = include_numbers()
    if numbers: 
        char += string.digits
    print(numbers)
    time.sleep(1)

    print("🟣 Would you like special characters? ")
    special_characters = include_special_characters()
    if special_characters:
        char += string.punctuation
    print(special_characters)
    time.sleep(1)

    #This is purely graphic user experience, this four lines don't change the final product.
    print("⌛~Generating your new password...")
    time.sleep(2)
    print("⭐~Scoring your new password...")
    time.sleep(2)

    #This is the generator itself.
    password = "".join(random.choice(char) for i in range(length))
    
    #Scoring.
    score = password_strength(password)
    if score == 0:
        final_score = "☆☆☆☆☆ 💀 Unusable 💀"
    elif score == 1:
        final_score = "★☆☆☆☆ 🔥 Weak 🔥"
    elif score == 2:
        final_score = "★★☆☆☆ 🚧 Decent 🚧"
    elif score == 3:
        final_score = "★★★☆☆ 🔒 Strong 🔒"
    elif score == 4:
        final_score = "★★★★☆ 🔐 Excellent 🔐"
    else:
        final_score = "★★★★★ 🔰 POWERFUL 🔰"
    
    #Final output.
    print("⟡ Your new safe password is: " + password + " ⟡")
    time.sleep(1)
    print("⟡ Password Strength: " + final_score)
    time.sleep(2)
    if score <=3:
        print("⚠️ Consider generating a new, stronger password to use, since this one is vulnerable. ⚠️")
        time.sleep(1)
        print("If you still want to use it, please remember that the password generated is not stored anywhere, so store it safely!")
    else: 
        print("⚠️ Please remember that the password generated is not stored anywhere, so store it safely!")
    time.sleep(3)

    #Goodbye message:
    print("Thank you for using Beel's Password Generator.")

# --------------------------------------------------------- #

'''
Thank you so much for reading and testing. Let me know if there are some improvements I could do.
Byee~
⟡ Contact Info ⟡
Github - BeeluRiddle - https://github.com/BeeluRiddle
Linkedin - belenzapata6 - https://www.linkedin.com/in/belenzapata6/
'''