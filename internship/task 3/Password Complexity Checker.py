import re

def assess_password_strength(password):
    # Define criteria weights
    criteria_weights = {
        'length': 1,
        'uppercase': 1,
        'lowercase': 1,
        'digit': 1,
        'special_char': 1
    }

    # Define criteria checks
    length_criteria = len(password) >= 8
    uppercase_criteria = any(char.isupper() for char in password)
    lowercase_criteria = any(char.islower() for char in password)
    digit_criteria = any(char.isdigit() for char in password)
    special_char_criteria = any(char in "!@#$%^&*()_+-=[]{}|;':\",./<>?" for char in password)

    # Evaluate each criteria and calculate score
    criteria_scores = {
        'length': criteria_weights['length'] if length_criteria else 0,
        'uppercase': criteria_weights['uppercase'] if uppercase_criteria else 0,
        'lowercase': criteria_weights['lowercase'] if lowercase_criteria else 0,
        'digit': criteria_weights['digit'] if digit_criteria else 0,
        'special_char': criteria_weights['special_char'] if special_char_criteria else 0
    }

    # Calculate total score
    total_score = sum(criteria_scores.values())

    # Determine strength based on total score
    if total_score == 0:
        return "Very Weak"
    elif total_score <= 2:
        return "Weak"
    elif total_score == 3:
        return "Moderate"
    elif total_score == 4:
        return "Strong"
    elif total_score == 5:
        return "Very Strong"

# Example usage
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength = assess_password_strength(password)
    print(f"Password strength: {strength}")
