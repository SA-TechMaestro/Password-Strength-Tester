# Password Strength Tester
# Author: Siraj Abdul-Shahid

#User Password Prompt
password = input("Please enter your password: ")

print("You entered:", password)


# Password Length Check
if len(password) >= 8:
    print("Password meets the minimum requirement. ", len(password),"of 8.")
else:
    print("Password must be 8 or more characters. Password length:", len(password),"of 8.")


# Capitalization and Punctuation Check
has_upper = False
has_lower = False
has_digit = False

import string
has_symbol = False

for char in password:
    if char.isupper():
        has_upper = True 
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in string.punctuation:
        has_symbol = True

print("Contains uppercase letter:", has_upper)
print("Contains lowercase letter:", has_lower)
print("Contains digit:", has_digit)
print("Contains Symbol:", has_symbol)


# Password Strength Scoring System
score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_symbol:
    score += 1

print("Password strength score:", score, "out of 5")

# Password Scores
if score <= 2:
    print("Strength: Weak - Do Better.")
elif score == 3 or score == 4:
    print("Strength: Moderate - Almost There..")
elif score >= 5:
    print("Strength: STRONG - Congratulations!")
    
