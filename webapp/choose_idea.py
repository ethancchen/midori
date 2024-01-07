
import streamlit as st
import pandas as pd


def change_page():
    st.session_state["menu_selection"] = "Business Zone"

def handle_button_press_to_business_zone():

    if st.session_state['choice'] is not None:
        # st.success(f"You entered: {choice}")
        # handle_button_press_to_business_zone()
        change_page()

    else:
        st.warning("Please enter a value before clicking 'Next'.")
    # st.session_state["menu_selection"] = "Business Zone"

def page_choose_idea():
    st.write("Page Choose Idea")


    org_df = st.session_state["org_df"]
    ans_df = st.session_state['ans_df']

    ranked_df = st.session_state["ranked_df"]

    merged_df = pd.concat([org_df, ans_df], axis=1)

    #rank pairs
    x = 0.25 # filter to get only top x% of ranks
    num_top_pairs = int(x * len(merged_df))
    merged_df.sort_values(by="scores", ascending=False).head(num_top_pairs).head()

    if 'merged_df' not in st.session_state:
        st.session_state['merged_df'] = merged_df

    st.write(merged_df)
    choice = st.number_input("Enter your choice here")

    if 'choice' not in st.session_state:
        st.session_state['choice'] = choice


    row_by_index = merged_df.iloc[int(choice)]
    st.write(row_by_index)


    if 'lean_row' not in st.session_state:
        st.session_state['lean_row'] = row_by_index

    # # Add a button
    # if st.button("Next"):
    #     st.success(f"You entered: {choice}")

    
    # st.button("Next", on_click=handle_button_press_to_business_zone)

       # Next button to proceed to the evaluation page
    st.button("Next", on_click=handle_button_press_to_business_zone())
        
    

    
