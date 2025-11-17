# 🔐 SecurePass - Password Manager

**A Simple Python Password Manager with Encryption**

**Authors:** Omar Khouja & Juan Carlos Lazo  
**Course:** ReDI School Python Foundations - Hamburg  
**Date:** November 2025  


---

## 👥 Team Members

| Name | Role | Contributions |
|------|------|---------------|
| **Omar Khouja** | Lead Developer | Password generator, encryption logic, file handling |
| **Juan Carlos Lazo** | Co-Developer | Strength checker, menu design, testing & documentation |

---

## 📖 Project Overview

SecurePass is a command-line password manager that helps users:
- Generate strong, random passwords
- Check password strength (scoring 0-100)
- Store passwords securely with encryption
- Manage passwords (add, view, search)

**All in ONE simple file - perfect for Python Foundations!**

---

## 🎯 Problem & Solution

### The Problem:
- People use weak passwords like "123456" or "password"
- Hard to remember unique passwords for each account
- No secure place to store them
- Risk of account breaches

### Our Solution:
SecurePass helps users:
- ✅ Generate strong passwords automatically
- ✅ Check if their passwords are secure
- ✅ Store passwords encrypted with a master password
- ✅ Easily find passwords when needed

---

## 🚀 How to Run

```bash
# No installation needed! Just run:
python simple_password_manager.py
```

**Requirements:**
- Python 3.8 or higher
- No external libraries needed (uses only Python standard library)

---

## 💡 Key Features

### 1. Password Generator 🎲
Generate strong random passwords with:
- Customizable length (8-128 characters)
- Mix of uppercase, lowercase, digits, and special characters
- Guaranteed to include at least one of each character type

**Example:**
```
Generated: kT8@mP3!xR5z [Strong]
```

### 2. Password Strength Checker 💪
Evaluates password security based on:
- Length (longer is better)
- Character variety (uppercase, lowercase, digits, special)
- Common patterns (detects weak passwords)

**Scoring System:**
- 0-39: Weak
- 40-59: Medium
- 60-79: Strong
- 80-100: Very Strong

### 3. Secure Storage 🔐
- All passwords encrypted before saving
- Uses master password for encryption
- XOR encryption with SHA-256 key derivation
- Base64 encoding for safe file storage

### 4. Password Management 📝
- Add new passwords with website/username
- View all stored passwords
- Search by website or username
- Simple, intuitive menu interface

---

## 🔐 How It Works

### Encryption Process:
```
1. Master Password → SHA-256 Hash → Encryption Key
2. Password Data → XOR Encryption → Encrypted Data
3. Encrypted Data → Base64 Encoding → Save to File
```

### Decryption Process:
```
1. Read File → Base64 Decode → Encrypted Data
2. Master Password → SHA-256 Hash → Decryption Key
3. Encrypted Data + Key → XOR Decryption → Original Data
```

**Security Note:** This is educational-level encryption. For production use, consider professional tools like Bitwarden or 1Password.

---

## 📂 Project Structure

```
SecurePass/
├── simple_password_manager.py    ← Main program (200 lines)
└── passwords.txt                 ← Encrypted storage (auto-created)
```

**That's it! Just ONE file - simple and effective.**

---

## 📋 Menu Options

```
MENU:
1. Generate new password      → Create strong random passwords
2. Check password strength    → Test any password's security
3. Add password to vault      → Store a new password
4. View all passwords         → Display all saved passwords
5. Search password            → Find specific entry
6. Exit                       → Close program securely
```

---

## 🧪 Example Usage

### Generating a Password:
```
Choose (1-6): 1
Password length (default 16): 12

Generated passwords:
1. aB3!xY9@kL2m [Strong - 85/100]
2. pQ7&mN4$wE5z [Strong - 80/100]
3. hR6%cV8!tU3x [Very Strong - 90/100]
4. kF5@tM2!pX9r [Strong - 80/100]
5. wN8#qL4$vC6z [Very Strong - 95/100]
```

### Checking Password Strength:
```
Choose (1-6): 2
Enter password to check: MyPass123

Strength: Strong (Score: 75/100)
Feedback:
- Good length (9 characters)
- Contains uppercase ✓
- Contains lowercase ✓
- Contains digits ✓
- Missing: special characters
```

### Adding a Password:
```
Choose (1-6): 3
Website/App: gmail.com
Username: someone@gmail.com

1. Generate new password
2. Enter my own password
Choose (1/2): 1

Generated: kT8@mP3!xR5z
Strength: Very Strong (95/100)

✓ Password saved successfully!
```

### Viewing All Passwords:
```
Choose (1-6): 4

--- ALL PASSWORDS ---

1. gmail.com
   Username: someone@gmail.com
   Password: kT8@mP3!xR5z
   
2. github.com
   Username: omar987x
   Password: Xp9#kR5@mT2z

Total: 2 passwords stored
```

---

## 🎓 What We Learned

### Python Concepts Applied:

**Omar's Focus:**
- ✅ Functions & Modular Design
- ✅ File I/O (reading/writing)
- ✅ Encryption Basics (hashing, XOR)
- ✅ Random Module
- ✅ String Manipulation

**Juan Carlos's Focus:**
- ✅ Conditional Logic
- ✅ Loops (while, for)
- ✅ Data Structures (lists, dictionaries)
- ✅ User Input/Output
- ✅ Testing & Validation

**Together We Learned:**
- 📚 Working as a team
- 📚 Code organization
- 📚 Problem-solving
- 📚 Security best practices
- 📚 User experience design

---

## 💻 Code Structure

### Part 1: Password Generator (20 lines)
```python
def generate_password(length=16):
    """Generate strong random password"""
    # Mix character types
    # Ensure at least one of each
    # Shuffle for randomness
```

### Part 2: Strength Checker (30 lines)
```python
def check_password_strength(password):
    """Calculate password strength score"""
    # Check length, variety, patterns
    # Return score and rating
```

### Part 3: Encryption (40 lines)
```python
def simple_encrypt(text, master_password):
    """Encrypt data with master password"""
    # SHA-256 key derivation
    # XOR encryption
    # Base64 encoding
```

### Part 4: Storage (40 lines)
```python
def save_passwords(passwords, master_password):
def load_passwords(master_password):
    """Handle encrypted file storage"""
```

### Part 5: Main Program (70 lines)
```python
def main():
    """Interactive menu system"""
    # Load passwords
    # Display menu
    # Handle user choices
```

**Total: ~200 lines of clean, well-commented code**

---

## 🔒 Security Features

✅ **Master Password Protection**
- All data encrypted with user's master password
- Password never stored (only hash used for verification)

✅ **Encrypted Storage**
- XOR encryption with SHA-256 key derivation
- Base64 encoding for safe file storage
- Cannot read passwords.txt without master password

✅ **Password Input Masking**
- Uses `getpass` module to hide password input
- Prevents shoulder surfing

✅ **No Plain Text Storage**
- All passwords encrypted before saving
- Decrypted only in memory when accessed

---

## ⚠️ Important Notes

### Master Password:
- **Choose a strong master password** (at least 12 characters)
- **Never forget it!** Cannot be recovered if lost
- All your passwords depend on it

### Backup:
- Regularly backup `passwords.txt` file
- Keep backup secure (it's encrypted)
- Without master password, backup is useless

### Security Disclaimer:
This is an **educational project** demonstrating:
- Python programming concepts
- Basic encryption principles
- File handling and data structures

For **real-world use**, we recommend professional password managers like:
- Bitwarden (open source)
- 1Password
- LastPass
- KeePass

---

## 🚀 Future Enhancements

Ideas for improvement (post-course):
- [ ] Delete/Update password functionality
- [ ] Password categories/tags
- [ ] Export to CSV
- [ ] Password expiry reminders
- [ ] Strength requirements customization
- [ ] GUI interface (Tkinter)
- [ ] Cloud sync (Supabase)
- [ ] Browser extension
- [ ] Mobile app

---

## 🧪 Testing

We tested the program with:
- ✅ Various password lengths (8-64 characters)
- ✅ Different character combinations
- ✅ Empty/invalid inputs
- ✅ Wrong master passwords
- ✅ Multiple save/load cycles
- ✅ Large password databases (50+ entries)

**All tests passed successfully!**

---

## 📊 Project Stats

| Metric | Value |
|--------|-------|
| **Lines of Code** | ~200 |
| **Functions** | 5 main functions |
| **Development Time** | 2 weeks |
| **Team Size** | 2 people |
| **Python Version** | 3.8+ |
| **Dependencies** | 0 (standard library only) |

---

## 🎤 Presentation

We presented this project at ReDI School Hamburg on December 8, 2024.

**Presentation Structure:**
1. **Introduction** (Omar) - Problem statement
2. **Demo** (Both) - Live demonstration
3. **Code Explanation** (Juan Carlos) - Key functions
4. **Learning Outcomes** (Omar) - What we learned
5. **Q&A** (Both) - Answer questions

**Duration:** 5 minutes  
**Tools Used:** Gamma.ai for slides

---

## 👨‍💻 About the Authors

### Omar Khouja
- **Location:** Hamburg, Germany
- **Background:** Full Stack Development
- **GitHub:** [github.com/okhouja](https://github.com/okhouja)
- **LinkedIn:** [omar-khouja](https://linkedin.com/in/omar-khouja)
- **Focus:** Backend development, security, DevOps

### Juan Carlos Lazo
- **Location:** Hamburg, Germany
- **Background:** Data Analytics
- **Focus:** Python programming, testing, documentation

---

## 🙏 Acknowledgments

- **ReDI School Hamburg** - For the Python Foundations course
- **Our Instructors** - For guidance and support
- **Our Classmates** - For feedback and collaboration
- **Open Source Community** - For inspiration and learning resources

---

## 📜 License

This project is created for educational purposes as part of the ReDI School Python Foundations final project.

Feel free to use, modify, and learn from this code!

---

## 📞 Contact

For questions or feedback:
- Email: omar0940@gmail.com
- GitHub Issues: [Report here](https://github.com/okhouja/securepass/issues)

---

**Built with ❤️ in Hamburg**  
**ReDI School Python Foundations - November 2024**

---

## 🎯 Quick Start Guide

1. Download `simple_password_manager.py`
2. Run: `python simple_password_manager.py`
3. Enter a master password (remember it!)
4. Start managing your passwords securely!

**That's it! Simple, secure, and effective.**

---

**Last Updated:** November 14, 2025  
**Version:** 1.0  
**Status:** ✅ Ready for submission