
import streamlit as st
import pandas as pd


def change_page():
    st.session_state["menu_selection"] = "Business Zone"

def handle_button_press_to_business_zone():
    if st.session_state['choice'] is not None:
        change_page()

    else:
        st.warning("Please enter a value before clicking 'Next'.")
    

def page_choose_idea():
    st.write("Page Choose Idea")

    org_df = st.session_state["org_df"]
    ans_df = st.session_state['ans_df']

    merged_df = pd.concat([org_df, ans_df], axis=1)

    # rank pairs
    x = 0.25 # filter to get only top x% of ranks
    num_top_pairs = int(x * len(merged_df))
    merged_df.sort_values(by="scores", ascending=False).head(num_top_pairs).head()

    if 'merged_df' not in st.session_state:
        st.session_state['merged_df'] = merged_df

    st.write(merged_df)
    
    if 'choice' not in st.session_state:
        st.session_state['choice'] = 0

    if 'lean_row' not in st.session_state:
        st.session_state['lean_row'] = None
    
    choice = st.number_input("Enter an integer:", min_value=None, max_value=None, value=0, step=1, format="%d")
 
    row_by_index = merged_df.iloc[int(choice)]
    
    st.session_state['choice'] = choice
    st.session_state['lean_row'] = row_by_index

    st.button("Next", on_click=handle_button_press_to_business_zone)
