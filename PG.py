import random
import string

def generate_password(length=12 , include_uppercase=True , include_numbers=True , include_special_chars=True):

    char_pool = string.ascii_lowercase #lowercase

    #Add uppercase if selected
    if include_uppercase:
        char_pool += string.ascii_uppercase
    # Add digits if selected
    if include_numbers:
        char_pool += string.digits
    # Add special characters if selected
    if include_special_chars:
        char_pool += string.punctuation
    # Ensure at least one of each type is included
    password = []
    if include_uppercase:
        password.append(random.choice(string.ascii_uppercase))
    if include_numbers:
        password.append(random.choice(string.digits))
    if include_special_chars:
        password.append(random.choice(string.punctuation))
    # Fill the rest of the password length with random choices
    password += random.choices(char_pool, k=length - len(password))
    # Shuffle to ensure randomness
    random.shuffle(password)
    
    # Convert list to string
    return ''.join(password)

# Example usage
password = generate_password(length=16, include_uppercase=True, include_numbers=True, include_special_chars=True)
print(f"Generated Password: {password}")