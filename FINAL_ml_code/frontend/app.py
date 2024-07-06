import streamlit as st
import requests

backend_url = "http://backend:8000"

def signup():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Sign Up"):
        response = requests.post(f"{backend_url}/signup", json={"email": email, "password": password})
        st.write(response.json())

def login():
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        response = requests.post(f"{backend_url}/login", json={"email": email, "password": password})
        st.write(response.json())

def main():
    st.title("User Authentication")
    option = st.selectbox("Choose an option", ["Sign Up", "Login"])
    if option == "Sign Up":
        signup()
    elif option == "Login":
        login()

if __name__ == "__main__":
    main()
