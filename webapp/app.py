import streamlit as st
import pandas as pd
import numpy as np
import get_started as gs
import mongoDB as mg
import hashlib as hl

import evaluator as ev
import business_zone as bz
import choose_idea as ci

def page_welcome():
    st.markdown("<h1 style='text-align: left; color: #808000;'>MIDORI</h1>", unsafe_allow_html=True)
    st.write(f"Hello {st.session_state['current_user']}")
    st.write("Welcome to Midori. Circular economy idea evaluator tool.")

def page_get_started():
    gs.get_started_page()

def page_evaluator():
    ev.page_evaluator()

def page_choose_idea():
    st.title("Pick the idea you wish to create a business model of")
    ci.page_choose_idea()

def page_business_zone():
    # st.title("Business Zone Page")
    # st.write("Lean Canvas Generated here")
    bz.page_business_zone()


def page_about():
    st.title("Meet the Team")
    
def handle_user_change():
    st.session_state["authenticated"] = False
    st.session_state['current_user'] = None
    st.session_state['current_user_hash'] = None

    
def handle_login(db, username_hash, password_hash, username):
    if mg.authenticate_user(db, username_hash, password_hash):
        st.success("Logged in as {}".format(username))
        st.session_state['authenticated'] = True
        st.session_state['current_user'] = username
        st.session_state['current_user_hash'] = username_hash
    else:
        error_message = "Incorrect username or password"
        st.error(error_message)
    
def handle_user_creation(db, username, password):
    if mg.create_user(db, username, password):
        st.success("Creation Successful. Proceed to login.")
    else:
        error_message = "Try another username."
        st.error(error_message)
    
def page_change_user():
    st.button("Change User", on_click=handle_user_change)
    st.write("Once you click on the button above. You will be redirected to a new login page.")

def main():
    # Initialize mongDB.
    db = mg.db_init()

    if 'api_key' not in st.session_state:
        st.session_state["api_key"]= "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"
    
    if 'type' not in st.session_state:
        st.session_state["type"] = None

    if 'authenticated' not in st.session_state:
        st.session_state["authenticated"] = True # reset to False
        
    if 'session_initialized' not in st.session_state:
        st.session_state['current_user'] = None
        st.session_state['current_user_hash'] = None
        st.session_state['session_initialized'] = True

    # Check if user is authenticated
    if not st.session_state['authenticated']:
        # User input for login

        st.markdown("<h1 style='text-align: left; color: #808000;'>MIDORI</h1>", unsafe_allow_html=True)
        st.write("Login to use our awesome idea eval tool")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        
        userID_hash = hl.sha256(username.encode('utf-8')).hexdigest()
        pwd_hash = hl.sha256(password.encode('utf-8')).hexdigest()
        
        # Check for login.
        st.button("Login", on_click=handle_login, args=[db, userID_hash, pwd_hash, username])
            
        # Create a new user if permitted.
        st.button("Create User", on_click=handle_user_creation, args=[db, userID_hash, pwd_hash])
    else:
        # Clear the login elements
        if 'menu_selection' not in st.session_state:
            st.session_state['menu_selection'] = 'Welcome'  # Default page
            st.rerun()

        st.sidebar.title("Navigation")
        pages = ["Welcome", "Get started", "Evaluator", "Choose Idea", "Business Zone", "About", "Change User"]

        # Updating the menu selection and rerunning the script if the selection changes
        current_selection = st.session_state["menu_selection"]
        new_selection = st.sidebar.radio("Choose a page", pages, index=pages.index(current_selection))
        if new_selection != current_selection:
            st.session_state['menu_selection'] = new_selection
            st.rerun()

        # Load the selected page
        match st.session_state['menu_selection']:
            case "Welcome":
                page_welcome()
            case "Get started":
                page_get_started()
            case "Evaluator":
                page_evaluator()
            case "Choose Idea":
                page_choose_idea()
            case "Business Zone":
                page_business_zone()
            case "About":
                page_about()
            case "Change User":
                page_change_user()
            case _:
                st.write("Page not found")


if __name__ == "__main__":
    main()