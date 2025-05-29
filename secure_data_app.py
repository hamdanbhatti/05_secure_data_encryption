import streamlit as st
from cryptography.fernet import Fernet, InvalidToken
import hashlib
import base64

st.set_page_config(page_title="Secure Data App", page_icon="🔐")

# ----------------- Session State -----------------
if 'page' not in st.session_state:
    st.session_state.page = 'login'
if 'attempts' not in st.session_state:
    st.session_state.attempts = 0
if 'data_store' not in st.session_state:
    st.session_state.data_store = []

# ----------------- Utility Functions -----------------
def generate_key_from_passkey(passkey: str):
    key = base64.urlsafe_b64encode(passkey.ljust(32)[:32].encode())
    return Fernet(key)

def hash_passkey(passkey: str):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(data: str, passkey: str):
    fernet = generate_key_from_passkey(passkey)
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(encrypted: str, passkey: str):
    try:
        fernet = generate_key_from_passkey(passkey)
        return fernet.decrypt(encrypted.encode()).decode()
    except InvalidToken:
        return None

# ----------------- Page: Login -----------------
def login_page():
    st.title("🔐 Secure Data App - Master Login")
    master = st.text_input("Enter master password", type="password")
    if st.button("Login"):
        if master == "admin123":
            st.session_state.page = "home"
            st.session_state.attempts = 0
            st.rerun()
        else:
            st.error("Incorrect master password.")

# ----------------- Page: Home -----------------
def home_page():
    st.sidebar.title("🔒 Secure Data Menu")
    nav = st.sidebar.radio("Go to", ["Encrypt", "Decrypt", "Logout"])

    st.title("🔐 Secure Data Encryption App")

    if nav == "Encrypt":
        st.subheader("📝 Encrypt & Store Data")
        data = st.text_area("Enter data to encrypt:")
        passkey = st.text_input("Enter a passkey:", type="password")

        if st.button("Encrypt & Save"):
            if data and passkey:
                encrypted = encrypt_data(data, passkey)
                hashed_key = hash_passkey(passkey)
                st.session_state.data_store.append({
                    'encrypted': encrypted,
                    'passkey_hash': hashed_key
                })
                st.success("✅ Data encrypted and stored!")
                st.code(encrypted)
            else:
                st.error("Please enter both data and passkey.")

    elif nav == "Decrypt":
        st.subheader("🔍 Decrypt Data")
        encrypted = st.text_area("Paste encrypted data:")
        passkey = st.text_input("Enter passkey used for encryption:", type="password")

        if st.button("Decrypt"):
            if encrypted and passkey:
                hashed_input = hash_passkey(passkey)
                matched = next((item for item in st.session_state.data_store 
                                if item['encrypted'] == encrypted and item['passkey_hash'] == hashed_input), None)
                if matched:
                    result = decrypt_data(encrypted, passkey)
                    if result:
                        st.success("✅ Decryption Successful!")
                        st.code(result)
                        st.session_state.attempts = 0
                    else:
                        st.warning("❌ Invalid encryption or key mismatch.")
                else:
                    st.session_state.attempts += 1
                    attempts_left = 3 - st.session_state.attempts
                    st.error(f"Wrong passkey or data! Attempts left: {attempts_left}")
                    if st.session_state.attempts >= 3:
                        st.warning("🚫 3 wrong attempts! Redirecting to login.")
                        st.session_state.page = "login"
                        st.session_state.attempts = 0
                        st.rerun()
            else:
                st.error("Enter both encrypted data and passkey.")

    elif nav == "Logout":
        st.session_state.page = "login"
        st.rerun()

# ----------------- Router -----------------
if st.session_state.page == "login":
    login_page()
else:
    home_page()
