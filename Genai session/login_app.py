import streamlit as st

### Login page

USERNAME = "samar"
PASSWORD = "Sam@648254"

def check_login(username, password):
    return username == USERNAME and password == PASSWORD

st.title("Aparichit Login Page")

username = st.text_input("Username")
password = st.text_input("Password", type="password")

login_button = st.button("Login")

if login_button:
    if check_login(username, password):
        st.success("Login successful!")
        st.write("Welcome to the application!")
    else:
        st.error("Invalid username or password")
