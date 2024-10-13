import streamlit as st
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from connect import getdb

def encrypt_password(password, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_password = pad(password.encode(), AES.block_size)
    encrypted_password = cipher.encrypt(padded_password)
    return encrypted_password


def adduser():
    db = getdb()
    users_collection = db['userdata']
    st.title("Registration Page")
    new_username = st.text_input("New Username")
    new_password = st.text_input("New Password", type="password")
    key = get_random_bytes(16)

    encrypted_password = encrypt_password(new_password, key)

    if st.button("Register"):
        new_user = {
            "username": new_username,
            "password": encrypted_password,
            "password_key": key
        }
        users_collection.insert_one(new_user)
        st.success("Registration successful!")

adduser()