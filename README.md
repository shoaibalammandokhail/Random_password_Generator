# 🔐 Secure Random Password Generator

A secure password generator built in Python using the `secrets` module.

This project generates cryptographically secure passwords with uppercase letters, lowercase letters, digits, and special characters. It also estimates password entropy and strength.

---

## Features

- Cryptographically secure password generation
- Uses Python's `secrets` module
- Input validation
- Minimum password length enforcement
- Includes:
  - Uppercase letters
  - Lowercase letters
  - Numbers
  - Special characters
- Password entropy calculation
- Password strength evaluation

---

## Technologies

- Python 3
- secrets
- string
- math

---

## Project Structure

```
Random-Password-Generator/
│
├── random_password_generator.py
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Random-Password-Generator.git
```

Go to the project folder

```bash
cd Random-Password-Generator
```

Run the program

```bash
python random_password_generator.py
```

---

## Example Output

```
==================================================
DecodeLabs Secure Password Generator
==================================================

Enter desired password length (minimum 8): 12

Generated Password :
7LL|#5;Q\dlB

Estimated Entropy :
78.7 bits

Strength :
Reasonable
```

---

## How It Works

1. User enters the desired password length.
2. The program validates the input.
3. It guarantees at least one:
   - Uppercase letter
   - Lowercase letter
   - Digit
   - Special character
4. Remaining characters are randomly selected.
5. Password is securely shuffled.
6. Entropy is calculated.
7. Password strength is displayed.

---

## Concepts Used

- Functions
- Exception Handling
- Input Validation
- List Comprehension
- String Manipulation
- Cryptographic Security
- Entropy Calculation

---

## Author

**Shoaib Alam**

Software Engineering Student

Interested in:

- AI Automation
- Python Development
- Machine Learning
- Backend Development

---

⭐ If you like this project, give it a star.
