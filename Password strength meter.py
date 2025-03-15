import os
import re
import math
import string


COMMON_PASSWORDS = {"123456", "password", "123456789", "qwerty", "abc123", "password1", "123123", "admin", "welcome"}

def calculate_entropy(password):
    
    charset_size = 0
    if any(c.islower() for c in password):
        charset_size += 26
    if any(c.isupper() for c in password):
        charset_size += 26
    if any(c.isdigit() for c in password):
        charset_size += 10
    if any(c in string.punctuation for c in password):
        charset_size += len(string.punctuation)
    
    entropy = len(password) * math.log2(charset_size) if charset_size > 0 else 0
    return entropy

def evaluate_password(password):

    length = len(password)
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"\d", password))
    has_special = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    entropy = calculate_entropy(password)

    
    score = 0
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    if has_upper and has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1
    if entropy >= 50:
        score += 1
    if entropy >= 75:
        score += 1

    
    if password.lower() in COMMON_PASSWORDS:
        return "Very Weak (Common Password Detected)", entropy
    
    
    if score <= 2:
        return "Very Weak", entropy
    elif score <= 4:
        return "Weak", entropy
    elif score <= 6:
        return "Moderate", entropy
    elif score <= 7:
        return "Strong", entropy
    else:
        return "Very Strong", entropy


def suggest_improvements(password):
    
    suggestions = []
    if len(password) < 12:
        suggestions.append("Make your password at least 12 characters long.")
    if not re.search(r"[A-Z]", password):
        suggestions.append("Include at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        suggestions.append("Include at least one lowercase letter.")
    if not re.search(r"\d", password):
        suggestions.append("Include at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        suggestions.append("Include at least one special character (e.g., @, #, !, $).")
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid using common passwords.")
    
    return suggestions


def main():
    os.system('cls')
    print(" Password Strength Checker \n")
    password = input("Enter your password: ")

    strength, entropy = evaluate_password(password)
    print(f"\nPassword Strength: {strength}")
    print(f"Entropy Score: {entropy:.2f} bits")

    if "Weak" in strength:
        print("\nSuggestions to Improve Your Password:")
        for suggestion in suggest_improvements(password):
            print("- " + suggestion)

if __name__ == "__main__":
    main()


