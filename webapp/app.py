# app.py

import streamlit as st
import pandas as pd
import numpy as np
import get_started as gs
import mongoDB as mg


def page_welcome():
    st.markdown("<h1 style='text-align: left; color: #808000;'>MIDORI</h1>", unsafe_allow_html=True)
    st.write("Welcome to Midori. Circular economy idea evaluator tool.")

def page_get_started():
    gs.get_started_page()

def handle_rank_button(top_x_to_rank: int):
    def calculate_scores(llm_response: pd.Series, feature_weights: list) -> float:
        curr_score = 0
        if llm_response["relevance"] == True:
            # for now, exclude industry, ten_R, and area_focus
            for fw in feature_weights:
                curr_score += llm_response[fw] * feature_weights[fw]
        return curr_score
    value_mapping = {"Yes": 1, "No": -1, "Not Known": 0}
    df = st.session_state["df"]
    df_numeric = df.replace(value_mapping)
    feature_weights = {"applicable": 0.2, 
                       "heavy_investment": 0.2,
                       "monetary_benefits": 0.2,
                       "scalable": 0.2,
                       "payback_period": 0.2}
    assert(sum(feature_weights.values()) == 1)

    df_numeric.insert(loc = 0, column = 'scores', value = df_numeric.apply(lambda row: calculate_scores(row, feature_weights), axis = 1))

    # do not assert(x_prop) b/c the user can see this
    n = len(df_numeric)
    num_top_pairs = int(top_x_to_rank/100 * n)
    st.write(num_top_pairs)

    if (1/n * 100 < top_x_to_rank <= 100):
        st.write(f"Choosing the highest **{top_x_to_rank:.2f}**%, or **{num_top_pairs}**, of all problem : solution pairs ranked by weighted scores.")

        df_rank_filtered = df_numeric.sort_values(by="scores", ascending=False).iloc[:num_top_pairs]
        # TODO: how do we break ties? What if there aren't that many unique score values?
        df_rank_filtered.index = np.arange(1, len(df_rank_filtered) + 1)
        st.write(df_rank_filtered)
    else:
        st.write(f"Please choose a valid proportion between {int(1/n * 100)} and 100% of pairs to select.")

    # TODO: Add option to see and/or download full ranked, sorted, and unfiltered dataset.

def page_evaluator():
    st.title("Evaluator Page")

    df = pd.read_csv("../csv/random_response_data_frame.csv")
    df["relevance"] = np.random.rand(len(df)) < 0.7  # temporary
    st.session_state["df"] = df

    # allow option for integer (vs. just %) number of pairs
    top_x_to_rank = st.number_input(label = "% of desired top scores to rank and filter",
                                    min_value = 1.0/len(df) * 100,
                                    max_value = 100.0,
                                    value = 10.0,
                                    step = 0.01,
                                    )

    handle_rank_button(top_x_to_rank)

    st.button("Update database with these scores")

    # No button for now b/c we change dynamically based on input
    # st.button(f"Rank top {st.session_state['top_x_to_rank']}% of scores", on_click=handle_rank_button)

def page_business_zone():
    st.title("Business Zone Page")
    st.write("Lean Canvas Generated here")

def page_about():
    st.title("Meet the Team")

def main():
    correct_username = "user"
    correct_password = "password"
    
    db = mg.db_init()
    
    if 'authenticated' not in st.session_state:

        # TODO: Change it to false before deployment
        st.session_state["authenticated"] = False

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
        if st.button("Create User"):
            if mg.create_user(db, username, password):
                st.success("Creation Successful. Proceed to login.")
            else:
                error_message = "Try another username."
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
