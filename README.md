# Safe Password Generator
* *A cybersecurity project.*

## Description 
Do you still use the same password for everything? Is it troublesome to always think of a new and safe password? 
Well look no further because the answer to those questions are right here!
Choose from one of my 3 password generators based on how much control you want to have on it, and stay safer online. 

## Set-up
For none of this generators you need to install anything besides a place to run python code. All the necessary libraries don't need to be imported. 

## What it looks like
* Basic
```python
import string
import random

length = int(input("How many characters would you like your password to have?"))
char = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(char) for i in range(length))
print("Your new safe password is: " + password)
```
* Advanced

## Roadmap
I have just finished this 3 versiones, and for future updates, I would like to work on a storage and encription system, as well as a graphic interface for better user experience. 

## Authors and acknowledgment
Big thanks to *Ciberu* for the inspiration. 

## Goodbyes
Thank you so much for testing my generators. 
Any feedback on inprovements is very much welcome. 

⟡ Contact Info ⟡ <br>
[Github](https://github.com/BeeluRiddle) - BeeluRiddle
[Linkedin](https://www.linkedin.com/in/belenzapata6/) - belenzapata6
