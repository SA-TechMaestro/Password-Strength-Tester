# 🔐 Password Strength Tester

This is a beginner-level Python script that tests the strength of a password based on common best practices. It evaluates length, variety, and includes a basic scoring system to rate the password as **Weak**, **Moderate**, or **Strong**.

---

## 🧠 What It Does

- Prompts the user to enter a password
- Checks if the password:
  - Is at least 8 characters long
  - Contains uppercase letters
  - Contains lowercase letters
  - Contains digits
  - Contains symbols (e.g. `!@#$%^&*`)
- Assigns a score from 0 to 5
- Prints a strength rating based on that score

---

## 🛠️ Skills Practiced

- User input handling
- String methods (`isupper()`, `islower()`, `isdigit()`)
- Iteration and conditional logic
- Boolean flags
- Basic scoring system
- Clean and readable code structure

---

## 📄 Example Output

Please enter your password: Google'$#1ITTeam  
You entered: Google'$#1ITTeam  
Password meets the minimum requirement. 16 of 8.  
Contains uppercase letter: True  
Contains lowercase letter: True  
Contains digit: True  
Contains Symbol: True  
Password strength score: 5 out of 5  
Strength: STRONG - Congratulations!

---

## 📁 File

- `password_strength_tester.py` — the main script

---

## 🚀 Future Enhancement Ideas

- Hide password input using `getpass`
- Add GUI using Tkinter or Flask
- Compare password against a common password blacklist
- Store or validate multiple passwords

---

## 🧑‍💻 Created By

Siraj Abdul-Shahid — [GitHub](https://github.com/SA-TechMaestro)
