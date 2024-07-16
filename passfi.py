#To generate Password
import random
import string

def generate_psswd(length):
    if __name__ == "__main__":
    # Ask user for the desired length of the password
        try:
            width = int(input("Enter the desired password length (default is 8): "))
        except ValueError:
            width = 8
            print("Invalid input. Using default length of 8.")

    # Define the possible characters in each category
    lowletters = string.ascii_lowercase
    upperletters = string.ascii_uppercase
    digit = string.digits
    punctuation = string.punctuation

    # Ensure the password has at least one character of each category
    psswd = [
        random.choice(lowletters),
        random.choice(upperletters),
        random.choice(digit),
        random.choice(punctuation)
    ]

    # Generate the rest of the password
    remaining_length = width - 4
    possible_characters = lowletters + upperletters + digit + punctuation
    psswd += [random.choice(possible_characters) for _ in range(remaining_length)]

    # Shuffle the characters to ensure randomness
    random.shuffle(psswd)

    # Convert the list of characters into a string
    return ''.join(psswd)

# Example usage:
psswd_length = 8  # You can change this to any length you want
new_psswd = generate_psswd(psswd_length)
print(f"Your new password is: {new_psswd}")