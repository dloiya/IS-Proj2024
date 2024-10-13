import base64
import binascii
import streamlit as st
from Crypto.Cipher import AES
import hashlib
from Crypto.Util.Padding import pad, unpad
from connect import getdb

def decrypt_password(encrypted_password, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted_password = unpad(cipher.decrypt(encrypted_password), AES.block_size)
    return decrypted_password.decode()

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login():
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    db = getdb()
    users_collection = db["userdata"]

    if st.button("Login"):
        user_data = users_collection.find_one({"username": username})
        if user_data:
            stored_password = user_data["password"]
            stored_key = user_data["password_key"]
            st.success(stored_key)
            st.success(decrypt_password(stored_password, stored_key))
            try:
                decrypted_password = decrypt_password(stored_password, stored_key)
                if password == decrypted_password:
                    st.success("Login successful!")
                    st.session_state.user = user_data
                    return True
                else:
                    st.error("Invalid username or password.")
                    return False
            except (ValueError, UnicodeDecodeError):
                st.error("Invalid username or password.")
                return False
        else:
            st.error("User not found.")
            return None

if login():
    st.switch_page("pages/dashboard.py")
