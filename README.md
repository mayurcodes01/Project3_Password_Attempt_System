# Project 3: Password Attempt System

##  Description

This project is a simple **Password Attempt System** implemented in Python. It prompts the user to enter a password with a maximum of 3 attempts allowed. If the correct password is entered within these attempts, the system confirms the success. Otherwise, it locks out the user after 3 failed tries.

---

##  Technologies Used

- Python (Standard Library)
- Input/Output operations
- Looping and Conditional statements

---

##  How It Works

- The system has a predefined password (`123`).
- The user is asked to input the password.
- If the input matches the actual password:
  - The system displays a success message and exits.
- If the input does not match:
  - The system notifies the user and decreases the remaining attempts.
- After 3 failed attempts:
  - The system terminates with a lockout message.

---

##  Features

- Limits login attempts to a maximum of 3.
- Displays remaining attempts after each failure.
- Provides clear success or lockout feedback to the user.

---

##  Sample Output

