



# 🔐Secure Data Encryption App

A secure data encryption and decryption web application built using **Python** and **Streamlit**. This tool allows users to safely encrypt and decrypt text using a custom passkey, protected by a master password login system.

---

## 🚀Features

- 🔑 Master password authentication (`admin123`)
- 🧾 Encrypt any text data using a custom passkey
- 🔐 Decrypt only with the correct passkey
- 🔄 Passkey verification using SHA-256 hashing
- 🧠 Built-in brute-force protection (3 wrong attempts = logout)
- 📋 In-memory session storage of encrypted entries
- 📱 Fully interactive Streamlit web interface

---

## 🛠️ Technologies Used

- **Python 3.9+**
- [**Streamlit**](https://streamlit.io/)
- [**cryptography**](https://cryptography.io/)
- **hashlib**, **base64**

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone [https://github.com/hamdanbhatti/05_secure_data_encryption.git]
cd secure-data-encryption-app
````

### 2. Install Dependencies


```bash
pip install streamlit cryptography
```

---

## ▶️ Run the App

```bash
streamlit run secure_data_app.py
```

---

## 🔒 Default Master Password

```
admin123
```

You can change it in the `login_page()` function in the source code.

---



## 📁 Folder Structure

```
secure-data-encryption-app/
│
├── secure_data_app.py       # Main Streamlit app
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚠️ Limitations

* Data is stored only **in memory (session)** and will be lost after app reload.
* No database or persistent storage is currently implemented.
* Decryption only works if passkey and encrypted data both match stored entries.

---

## 📌 Future Improvements

* ✅ Export to CSV / PDF
* ✅ Add database or local file storage
* ✅ Hide/show encrypted data history
* ✅ User-based login & session management

---

## 👨‍💻 Author

**Hamdan**
Web Developer | Python & Streamlit Enthusiast

---

## 🛡️ License

This project is open-source and free to use under the [MIT License](LICENSE).

````

