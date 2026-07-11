import string
import secrets
import math


def get_password_length():
    """Phase 1: Get and validate user input for password length."""
    while True:
        user_input = input("Enter desired password length (minimum 8): ")

        try:
            length = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")
            continue

        if length < 8:
            print("For security, password length must be at least 8 characters.\n")
            continue

        return length


def generate_password(length):
    """Phase 2: Generate a secure password."""

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    symbols = string.punctuation

    # Complete character pool
    character_pool = uppercase + lowercase + digits + symbols

    # Ensure at least one character from each category
    password_chars = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    # Fill remaining characters
    for _ in range(length - 4):
        password_chars.append(secrets.choice(character_pool))

    # Securely shuffle the password
    secrets.SystemRandom().shuffle(password_chars)

    # Convert list into string
    password = "".join(password_chars)

    return password


def calculate_entropy(length, pool_size):
    """Phase 3: Estimate password strength in bits."""
    return length * math.log2(pool_size)


def main():
    print("=" * 50)
    print("      DecodeLabs Secure Password Generator")
    print("=" * 50)

    length = get_password_length()

    password = generate_password(length)

    pool_size = len(
        string.ascii_uppercase +
        string.ascii_lowercase +
        string.digits +
        string.punctuation
    )

    entropy = calculate_entropy(length, pool_size)

    print("\nGenerated Password :", password)
    print(f"Estimated Entropy : {entropy:.1f} bits")

    if entropy < 60:
        print("Strength : Weak")
    elif entropy < 80:
        print("Strength : Reasonable")
    else:
        print("Strength : Strong")


if __name__ == "__main__":
    main()