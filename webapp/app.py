# app.py

import streamlit as st
import pandas as pd
import get_started as gs


def page_welcome():
    st.markdown("<h1 style='text-align: left; color: #808000;'>MIDORI</h1>", unsafe_allow_html=True)
    st.write("Welcome to Midori. Circular economy idea evaluator tool.")

def page_get_started():
    gs.get_started_page()

def page_evaluator():
    st.title("Evaluator Page")
    st.write("Calculate scores here")

def page_business_zone():
    st.title("Business Zone Page")
    st.write("Lean Canvas Generated here")

def page_about():
    st.title("Meet the authors")

def main():
    correct_username = "user"
    correct_password = "password"

    if 'authenticated' not in st.session_state:

        # Change it to false before deployment
        st.session_state["authenticated"] = True

    # Check if user is authenticated
    if not st.session_state['authenticated']:
        # User input for login

        st.markdown("<h1 style='text-align: left; color: #808000;'>MIDORI</h1>", unsafe_allow_html=True)
        st.write("Login to use our awesome idea eval tool")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Check for login
        if st.button("Login"):
            if username == correct_username and password == correct_password:
                st.success("Logged in as {}".format(username))
                st.session_state['authenticated'] = True
            else:
                error_message = "Incorrect username or password"
                st.error(error_message)
    else:
        # Clear the login elements
        st.empty()

        

        st.sidebar.title("Navigation")
        pages = ["Welcome", "Get started", "Evaluator", "Business Zone", "About"]
        selected_page = st.sidebar.radio(" ", pages)

        if selected_page == "Welcome":
            page_welcome()
        elif selected_page == "Get started":
            page_get_started()
        elif selected_page == "Evaluator":
            page_evaluator()
        elif selected_page == "Business Zone":
            page_business_zone()
        elif selected_page == "About":
            page_about()

if __name__ == "__main__":
    main()
