# ---------- ⟡ Basic Password Generator ⟡ ---------- #

import string
import random

length = int(input("How many characters would you like your password to have?"))
char = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(char) for i in range(length))
print("Your new safe password is: " + password)

# --------------------------------------------------------- #

'''
Thank you so much for reading and testing. Let me know if there are some improvements I could do.
Byee~
⟡ Contact Info ⟡
Github - BeeluRiddle - https://github.com/BeeluRiddle
Linkedin - belenzapata6 - https://www.linkedin.com/in/belenzapata6/
'''