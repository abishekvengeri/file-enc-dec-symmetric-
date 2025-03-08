# 🔐 File Encryption & Decryption (Symmetric & Asymmetric)

This Python project provides **secure file encryption and decryption** using:
- **Symmetric Encryption** (Fernet)
- **Asymmetric Encryption** (RSA)

---

## 📦 Installation

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/yourusername/encryption-tool.git
cd encryption-tool
```

### 2️⃣ **Create a Virtual Environment**
```bash
python3 -m venv myenv
source myenv/bin/activate  # Activate on Linux/macOS
myenv\Scripts\activate     # Activate on Windows (Command Prompt)
```

### 3️⃣ **Install Required Libraries**
```bash
pip install cryptography
```

---

## 🔑 **Symmetric Encryption (Fernet)**

### ▶️ **How It Works**
1. **Generates a secret key** (`secret.key`).
2. **Encrypts** and **decrypts** files using this key.
3. **Stores encrypted files** with `.enc` extension.

### 🛠 **Usage**
Run the script:
```bash
python3 symmetric.py
```

Choose an option:
```
1. Encrypt a file
2. Decrypt a file
3. Exit
```

---

## 🔑 **Asymmetric Encryption (RSA)**

### ▶️ **How It Works**
1. **Generates a key pair** (private & public keys).
2. **Encrypts files** using the public key.
3. **Decrypts files** using the private key.

### 🛠 **Usage**
Run the script:
```bash
python3 asymmetric.py
```

Choose an option:
```
1. Encrypt a file
2. Decrypt a file
3. Exit
```


---

## 🤝 Contributing
✔ Fork this repo  
✔ Create a feature branch  
✔ Submit a **Pull Request** 🚀  

---

### 🌟 Show Your Support!  
Give a ⭐ on GitHub if you find this useful! 😊

