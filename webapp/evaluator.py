# evaluator.py
import re
from io import BytesIO

import api_calls as ac
import pandas as pd
import streamlit as st


def preprocess(df):
    # Process the data, removing short problems and solutions.
    def process_row(row):
        solution_text = str(row["solution"]).encode("utf-8", errors="ignore").decode("utf-8")
        problem_text = str(row["problem"])

        return {
            "solution": solution_text,
            "r_sent_cnt": len(re.findall("[^.!?]+[.!?]", solution_text)),
            "r_char_cnt": len(solution_text),
            "p_char_cnt": len(problem_text),
        }

    processed_data = df.apply(process_row, axis=1, result_type="expand")

    filtered_data = processed_data[
        (processed_data["r_sent_cnt"] > 10)
        | (processed_data["r_char_cnt"] >= 250) & (processed_data["p_char_cnt"] > 42)
    ]

    return filtered_data[["problem", "id", "solution"]]


def handle_button_press_to_business_zone():
    st.session_state["menu_selection"] = "Choose Idea"


def page_evaluator():
    st.title("Evaluator Page")

    if st.session_state["type"] == "manual":
        prob = st.session_state["problem"]
        sol = st.session_state["solution"]
        input_string = "Problem : " + prob + "  \n  " + "Solution : " + sol
        st.write("**Problem - Solution Pair that you provided.**")
        st.write(input_string)
        ac.get_data_single(input_string)

    elif st.session_state["type"] == "csv":
        st.write("**Problem - Solution Pairs that you provided.**")
        uploaded_file = st.session_state["uploaded_file"]
        if uploaded_file is not None:
            file_buffer = BytesIO(uploaded_file.getvalue())
            df = pd.read_csv(file_buffer)
            st.write(df.head())
            preprocessed_df = preprocess(df)
            st.write("Dataset with preprocessing")
            st.write(preprocessed_df.head())
        ac.get_data(df)

    else:
        st.write("You have not provided any Problem : Solution pairs yet.")

    st.button("Next", on_click=handle_button_press_to_business_zone)
