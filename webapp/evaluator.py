# evaluator.py
import streamlit as st
import pandas as pd
import api_calls as ac
import openai

def preprocess(df):
    """# Replace"""
    # file_path = 'sample2.csv'
    # df = pd.read_csv(file_path)
    # st.write("Preview of the uploaded data:")
    # st.write(df.head())
    # return processed df
    return df

def handle_button_press_to_business_zone():
    st.session_state["menu_selection"] = "Choose Idea"

def page_evaluator():
    st.title("Evaluator Page")
    if 'problem' not in st.session_state:
        return
    
    prob = st.session_state['problem']
    sol = st.session_state['solution']
    
    # Proceed with the if-else loop based on session state type
    if st.session_state['type'] == "manual":
        input_string = "Problem : " + prob + "\n" + "Solution : " + sol
        # st.write(input_string)
        ac.get_data_single(input_string)

    elif st.session_state['type'] == "csv":
        st.write("Data retrieved from Get Started page:")
        uploaded_file = st.session_state.get("uploaded_file")
        df = pd.read_csv(uploaded_file)
        st.write(df.head())
        ac.get_data(df)
    
    st.button("Next", on_click=handle_button_press_to_business_zone)
    

# def page_evaluator():
#     st.title("Evaluator Page")
    
#     # Take API Key input
#     api_key = st.text_input("Enter API Key:")
#     st.session_state['api_key'] = api_key
    
#     # Initialize session state variables if not present
#     if 'problem' not in st.session_state:
#         st.session_state['problem'] = ""
#     if 'solution' not in st.session_state:
#         st.session_state['solution'] = ""

#     prob = st.session_state['problem']
#     sol = st.session_state['solution']

#     st.write(prob)
#     st.write(sol)

#     if not api_key:
#         st.error("Please enter the API Key.")
#     else:
#         # Proceed with the if-else loop based on session state type
#         if st.session_state['type'] == "manual":
#             input_string = "Problem : " + prob + "\nSolution : " + sol
#             st.write(input_string)
#             ac.get_data(input_string)

#         elif st.session_state['type'] == "csv":
#             st.write("Data retrieved from Get Started page:")
#             uploaded_file = st.session_state.get("uploaded_file")
#             df = pd.read_csv(uploaded_file)
#             st.write(df.head())
