# 🔐 Password Manager - Simple Version

**Author:** Omar Khouja  & Juan,

**Course:** ReDI School Python Foundations  
**Date:** 17.November 2025

---

## 📖 What is this?

A simple password manager that helps you:
- Generate strong passwords
- Check password strength
- Store passwords securely (encrypted)

**All in ONE file! (200 lines of code)**

---

## 🚀 How to Run

```bash
python simple_password_manager.py
```

That's it! No installation needed.

---

## 💡 Features

### 1. Password Generator
```python
Generate strong random passwords with:
- Uppercase letters (A-Z)
- Lowercase letters (a-z)
- Digits (0-9)
- Special characters (!@#$%^&*)
```

### 2. Password Strength Checker
```python
Check how strong a password is:
- Weak (0-39 points)
- Medium (40-59 points)
- Strong (60-79 points)
- Very Strong (80-100 points)
```

### 3. Encrypted Storage
```python
All passwords are encrypted using:
- Master password as key
- Simple XOR + Base64 encoding
- Saved in passwords.txt (encrypted)
```

### 4. Password Management
```python
- Add new passwords
- View all passwords
- Search passwords
```

---

## 📋 Menu Options

```
1. Generate new password  → Create strong passwords
2. Check password strength → Test any password
3. Add password to vault  → Save a new password
4. View all passwords     → See everything
5. Search password        → Find specific entry
6. Exit                   → Close program
```

---

## 🔐 How Encryption Works

### Simple Explanation:
```python
1. Master Password → SHA-256 Hash → Encryption Key
2. Your Data + Key → XOR Encryption → Encrypted Data
3. Encrypted Data → Base64 Encoding → Save to File
```

### To decrypt:
```python
1. Read File → Base64 Decode → Encrypted Data
2. Encrypted Data + Key → XOR Decryption → Your Data
```

**Note:** This is educational encryption. For real use, consider libraries like `cryptography`.

---

## 📂 File Structure

```
.
├── simple_password_manager.py    ← The program (ONE file!)
└── passwords.txt                 ← Encrypted storage (created automatically)
```

---

## 📝 Code Structure

### Part 1: Password Generator (20 lines)
```python
def generate_password(length=16):
    # Generate random password with all character types
```

### Part 2: Strength Checker (30 lines)
```python
def check_password_strength(password):
    # Calculate score based on length, uppercase, digits, etc.
```

### Part 3: Encryption (40 lines)
```python
def simple_encrypt(text, master_password):
    # Encrypt using XOR + Base64

def simple_decrypt(encrypted_text, master_password):
    # Decrypt and return original text
```

### Part 4: Storage (40 lines)
```python
def save_passwords(passwords, master_password):
    # Save encrypted to file

def load_passwords(master_password):
    # Load and decrypt from file
```

### Part 5: Main Program (70 lines)
```python
def main():
    # Menu loop with 6 options
```

**Total: ~200 lines of clean, readable code**

---

## 🎓 What I Learned

### Python Concepts Used:
✅ **Functions** - Modular code organization  
✅ **Lists & Dictionaries** - Data storage  
✅ **Loops** - Menu and iteration  
✅ **File Handling** - Read/write encrypted data  
✅ **User Input** - Interactive program  
✅ **String Operations** - Password manipulation  
✅ **Random Module** - Password generation  
✅ **JSON** - Data serialization  
✅ **Hashing** - SHA-256 for key derivation  
✅ **Base64** - Encoding/decoding  

---

## 🧪 Example Usage

### Generate Password:
```
Choose (1-6): 1
Password length (default 16): 12

Generated passwords:
1. aB3!xY9@kL2m [Strong]
2. pQ7&mN4$wE5z [Strong]
3. hR6%cV8!tU3x [Strong]
```

### Check Strength:
```
Choose (1-6): 2
Enter password to check: MyPass123

Strength: Strong (Score: 75/100)
```

### Add Password:
```
Choose (1-6): 3
Website/App: gmail.com
Username: omar@gmail.com

1. Generate new password
2. Enter my own password
Choose (1/2): 1
Generated: kT8@mP3!xR5z

✓ Password added!
```

### View All:
```
Choose (1-6): 4

--- ALL PASSWORDS ---
1. gmail.com
   Username: omar@gmail.com
   Password: kT8@mP3!xR5z
```

---

## ⚠️ Important Notes

1. **Master Password:**
   - Choose a strong master password
   - Don't forget it! (cannot be recovered)
   - All passwords encrypted with it

2. **Security:**
   - This is educational code
   - For real use, consider professional tools
   - Keep passwords.txt safe

3. **Backup:**
   - Save passwords.txt regularly
   - Can't decrypt without master password

---

## 🎯 For Presentation

### Slide 1: Problem
"People use weak passwords like '123456'"

### Slide 2: Solution
"Program that generates, checks, and stores passwords securely"

### Slide 3: Demo
[Live demo showing all 5 features]

### Slide 4: Code Highlights
```python
# Simple but powerful
def generate_password(length):
    # Mix all character types
    # Shuffle for randomness
    # Return strong password
```

### Slide 5: What I Learned
"Functions, files, encryption basics, user input"

---

## 🚀 Future Ideas

After the course, I could add:
- Delete/Update passwords
- Password categories
- Export to CSV
- GUI interface
- Cloud sync (Supabase)
- Web version (Next.js)

But for now, this simple version is perfect for Python Foundations!

---

## 📞 Contact

**Omar Khouja**  
Hamburg, Germany  
GitHub: github.com/okhouja

---

## 📜 License

Educational project for ReDI School Python Foundations Course.

---

**Last Updated:** November 14, 2024  
**Version:** 1.0 (Simple & Clean!)