# Password Manager - Simple Version
# Author: Omar Khouja
# ReDI School Python Foundations - Final Project
# Description:
# This program helps users generate strong passwords, check password strength,
# and store passwords securely in an encrypted file.

import random
import string
import json
import hashlib
import getpass
from base64 import b64encode, b64decode

# -----------------------------
# Part 1: Password Generator
# -----------------------------

def generate_password(length=16):
    """Generate a strong random password"""
    # Character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*"
    
    # Combine all characters
    all_chars = lowercase + uppercase + digits + special
    
    # Make sure we have at least one of each type
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the rest randomly
    for i in range(length - 4):
        password.append(random.choice(all_chars))
    
    # Shuffle to avoid predictable pattern
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)


# -----------------------------
# Part 2: Password Strength Checker
# -----------------------------

def check_password_strength(password):
    """Check how strong a password is (returns score 0-100)"""
    score = 0
    
    # Check length
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 15
    
    # Check for uppercase
    if any(c.isupper() for c in password):
        score += 20
    
    # Check for lowercase
    if any(c.islower() for c in password):
        score += 20
    
    # Check for digits
    if any(c.isdigit() for c in password):
        score += 20
    
    # Check for special characters
    if any(c in "!@#$%^&*" for c in password):
        score += 15
    
    # Return score and rating
    if score >= 80:
        rating = "Very Strong"
    elif score >= 60:
        rating = "Strong"
    elif score >= 40:
        rating = "Medium"
    else:
        rating = "Weak"
    
    return score, rating


# -----------------------------
# Part 3: Simple Encryption (using password as key)
# -----------------------------

def simple_encrypt(text, master_password):
    """Encrypt text using master password"""
    # Create a key from password using hash
    key = hashlib.sha256(master_password.encode()).digest()
    
    # Simple XOR encryption
    encrypted = []
    for i, char in enumerate(text):
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ key_char)
        encrypted.append(encrypted_char)
    
    # Encode to base64 to make it printable
    encrypted_text = ''.join(encrypted)
    return b64encode(encrypted_text.encode()).decode()


def simple_decrypt(encrypted_text, master_password):
    """Decrypt text using master password"""
    try:
        # Decode from base64
        encrypted_text = b64decode(encrypted_text.encode()).decode()
        
        # Create same key from password
        key = hashlib.sha256(master_password.encode()).digest()
        
        # Decrypt using XOR
        decrypted = []
        for i, char in enumerate(encrypted_text):
            key_char = key[i % len(key)]
            decrypted_char = chr(ord(char) ^ key_char)
            decrypted.append(decrypted_char)
        
        return ''.join(decrypted)
    except:
        return None


# -----------------------------
# Part 4: Storage (save/load passwords)
# -----------------------------

def save_passwords(passwords, master_password):
    """Save passwords to file (encrypted)"""
    # Convert passwords list to JSON string
    json_text = json.dumps(passwords, indent=2)
    
    # Encrypt the JSON
    encrypted = simple_encrypt(json_text, master_password)
    
    # Save to file
    with open("passwords.txt", "w") as file:
        file.write(encrypted)
    
    print("✓ Passwords saved!")


def load_passwords(master_password):
    """Load passwords from file (decrypt)"""
    try:
        # Read encrypted file
        with open("passwords.txt", "r") as file:
            encrypted = file.read()
        
        # Decrypt
        json_text = simple_decrypt(encrypted, master_password)
        
        if json_text is None:
            print("✗ Wrong master password!")
            return None
        
        # Convert JSON back to list
        passwords = json.loads(json_text)
        return passwords
    
    except FileNotFoundError:
        # File doesn't exist yet - return empty list
        return []


# -----------------------------
# Part 5: Main Program (Menu)
# -----------------------------

def main():
    print("=" * 50)
    print("PASSWORD MANAGER - Simple Version")
    print("=" * 50)
    
    # Ask for master password
    master_password = getpass.getpass("\n🔑 Enter master password: ")
    
    # Load existing passwords
    passwords = load_passwords(master_password)
    
    if passwords is None:
        print("Exiting...")
        return
    
    print(f"\n✓ Loaded {len(passwords)} password(s)")
    
    # Main menu loop
    while True:
        print("\n" + "-" * 50)
        print("MENU")
        print("-" * 50)
        print("1. Generate new password")
        print("2. Check password strength")
        print("3. Add password to vault")
        print("4. View all passwords")
        print("5. Search password")
        print("6. Exit")
        print("-" * 50)
        
        choice = input("\nChoose (1-6): ")
        
        if choice == "1":
            # Generate password
            print("\n--- PASSWORD GENERATOR ---")
            length = input("Password length (default 16): ")
            length = int(length) if length.isdigit() else 16
            
            # Generate 5 options
            print(f"\nGenerated passwords:\n")
            for i in range(5):
                pwd = generate_password(length)
                score, rating = check_password_strength(pwd)
                print(f"{i+1}. {pwd} [{rating}]")
        
        elif choice == "2":
            # Check strength
            print("\n--- PASSWORD STRENGTH CHECKER ---")
            pwd = getpass.getpass("Enter password to check: ")
            score, rating = check_password_strength(pwd)
            print(f"\nStrength: {rating} (Score: {score}/100)")
        
        elif choice == "3":
            # Add password
            print("\n--- ADD PASSWORD ---")
            website = input("Website/App: ")
            username = input("Username: ")
            
            print("\n1. Generate new password")
            print("2. Enter my own password")
            opt = input("Choose (1/2): ")
            
            if opt == "1":
                password = generate_password()
                print(f"Generated: {password}")
            else:
                password = getpass.getpass("Password: ")
            
            # Add to list
            passwords.append({
                "website": website,
                "username": username,
                "password": password
            })
            
            # Save
            save_passwords(passwords, master_password)
            print("✓ Password added!")
        
        elif choice == "4":
            # View all
            print("\n--- ALL PASSWORDS ---")
            if len(passwords) == 0:
                print("No passwords saved yet.")
            else:
                for i, p in enumerate(passwords, 1):
                    print(f"\n{i}. {p['website']}")
                    print(f"   Username: {p['username']}")
                    print(f"   Password: {p['password']}")
        
        elif choice == "5":
            # Search
            print("\n--- SEARCH ---")
            query = input("Search website/username: ").lower()
            found = False
            
            for p in passwords:
                if query in p['website'].lower() or query in p['username'].lower():
                    print(f"\nWebsite: {p['website']}")
                    print(f"Username: {p['username']}")
                    print(f"Password: {p['password']}")
                    found = True
            
            if not found:
                print("No matching passwords found.")
        
        elif choice == "6":
            # Exit
            print("\nGoodbye! Your passwords are safe.")
            break
        
        else:
            print("Invalid choice!")


# -----------------------------
# Run the program
# -----------------------------

if __name__ == "__main__":
    main()
