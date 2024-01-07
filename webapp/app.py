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
    st.title("Meet the Team")

def main():
    correct_username = "user"
    correct_password = "password"

    if 'authenticated' not in st.session_state:

        # TODO: Change it to false before deployment
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
        if 'menu_selection' not in st.session_state:
            st.session_state['menu_selection'] = 'Welcome'  # Default page
            st.experimental_rerun()

        st.sidebar.title("Navigation")
        pages = ["Welcome", "Get started", "Evaluator", "Business Zone", "About"]

        # Updating the menu selection and rerunning the script if the selection changes
        current_selection = st.session_state["menu_selection"]
        new_selection = st.sidebar.radio("Choose a page", pages, index=pages.index(current_selection))
        if new_selection != current_selection:
            st.session_state['menu_selection'] = new_selection
            st.experimental_rerun()

        # Load the selected page
        match st.session_state['menu_selection']:
            case "Welcome":
                page_welcome()
            case "Get started":
                page_get_started()
            case "Evaluator":
                page_evaluator()
            case "Business Zone":
                page_business_zone()
            case "About":
                page_about()
            case _:
                st.write("Page not found")


if __name__ == "__main__":
    main()
