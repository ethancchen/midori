# evaluator.py
import streamlit as st
import pandas as pd
import api_calls as ac
from io import BytesIO
import re

def preprocess(df):
    # Process the data, removing short problems and solutions.
    df['solution'] = df['solution'].str.encode('utf-8', errors='ignore').str.decode('utf-8')
    df['r_sent_cnt'] = df['solution'].apply(lambda x: len(re.findall('[^.!?]+[.!?]', str(x))))
    df['r_char_cnt'] = df['solution'].apply(lambda x: len(str(x)))
    df['p_char_cnt'] = df['problem'].apply(lambda x: len(str(x)))

    result_data = df[(df['r_sent_cnt'] > 10 | (df['r_char_cnt'] >= 250)) & (df['p_char_cnt'] > 42)]
    # Keep only 'problem' and 'solution' columns
    df = result_data[['problem', 'id', 'solution']]
    return df

def handle_button_press_to_business_zone():
    st.session_state["menu_selection"] = "Choose Idea"

def page_evaluator():
    st.title("Evaluator Page")
    
    # Proceed with the if-else loop based on session state type
    if st.session_state['type'] == "manual":
        prob = st.session_state['problem']
        sol = st.session_state['solution']
        input_string = "Problem : " + prob + "  \n  " + "Solution : " + sol
        st.write("**Problem - Solution Pair that you provided.**")
        st.write(input_string)
        ac.get_data_single(input_string)

    elif st.session_state['type'] == "csv":
        st.write("**Problem - Solution Pairs that you provided.**")
        uploaded_file = st.session_state["uploaded_file"]
        if uploaded_file is not None:
            file_buffer = BytesIO(uploaded_file.getvalue())
            df = pd.read_csv(file_buffer)
            st.write(df.head())

        ac.get_data(df)
    
    else:
        st.write("You have not provided any Problem : Solution pairs yet.")

    st.button("Next", on_click=handle_button_press_to_business_zone)