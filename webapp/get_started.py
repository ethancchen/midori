# get_started.py
import streamlit as st
import pandas as pd

def change_page_to_evaluator():
    # st.empty()
    st.session_state["menu_selection"] = "Evaluator"

def handle_button_press():
    uploaded_file = st.session_state.get("uploaded_file", None)
    problem = st.session_state.get("problem", "")
    solution = st.session_state.get("solution", "")

    if uploaded_file is not None:
        # Process the uploaded CSV file
        st.write("File Uploaded!")
        df = pd.read_csv(uploaded_file)
        st.write("Preview of the uploaded data:")
        st.write(df.head())
        # Additional logic for processing the CSV file
        change_page_to_evaluator()
    elif len(problem) >= 50 and len(solution) >= 250:
        # Process the manually entered fields
        # st.write("Proceeding to the Evaluation Page...")
        change_page_to_evaluator()
    else:
        if len(problem) < 50:
            st.warning("Problem should be at least 50 characters.")
        if len(solution) < 250:
            st.warning("Proposed Solution should be at least 250 characters.")


def get_started_page():
    st.title("Get Started Page")
    st.write("Upload a CSV file for multiple ideas evaluation or manually enter The Problem and Solution fields for a single idea.")

    # File uploader for CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file

    st.write("\n\n OR \n\n")

    # Manual entry for fields (required)
    problem = st.text_input("Problem", key="problem")
    solution = st.text_area("Proposed Solution", key="solution")

    # Next button to proceed to the evaluation page
    st.button("Next", on_click=handle_button_press)
