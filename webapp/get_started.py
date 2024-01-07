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
        # st.write("File Uploaded!")
        # df = pd.read_csv(uploaded_file)
        # st.write("Preview of the uploaded data:")
        # st.write(df.head())
        # Additional logic for processing the CSV file

        st.session_state['type'] = 'csv'
        change_page_to_evaluator()
    elif len(problem) >= 50 and len(solution) >= 250:
        # Process the manually entered fields
        # st.write("Proceeding to the Evaluation Page...")

        st.session_state['type'] = 'manual'
        change_page_to_evaluator()
    else:
        if len(problem) < 50:
            st.warning("Problem should be at least 50 characters.")
        if len(solution) < 250:
            st.warning("Proposed Solution should be at least 250 characters.")


def get_started_page():
    st.title("Get Started Page")
    st.write("Upload a CSV file for multiple ideas evaluation or manually enter The Problem and Solution fields for a single idea.")



    # change these default values to none

    # # Initialization
    # if 'problem' not in st.session_state:
    #     st.session_state['problem'] = 'The construction industry is indubitably one of the significant contributors to global waste, contributing approximately 1.3 billion tons of waste annually, exerting significant pressure on our landfills and natural resources. Traditional construction methods entail single-use designs that require frequent demolitions, leading to resource depletion and wastage.'   

    # # Initialization
    # if 'solution' not in st.session_state:
    #     st.session_state['solution'] = "Herein, we propose an innovative approach to mitigate this problem: Modular Construction. This method embraces recycling and reuse, taking a significant stride towards a circular economy.   Modular construction involves utilizing engineered components in a manufacturing facility that are later assembled on-site. These components are designed for easy disassembling, enabling them to be reused in diverse projects, thus significantly reducing waste and conserving resources.  Not only does this method decrease construction waste by up to 90%, but it also decreases construction time by 30-50%, optimizing both environmental and financial efficiency. This reduction in time corresponds to substantial financial savings for businesses. Moreover, the modular approach allows greater flexibility, adapting to changing needs over time.  We believe, by adopting modular construction, the industry can transit from a 'take, make and dispose' model to a more sustainable 'reduce, reuse, and recycle' model, driving the industry towards a more circular and sustainable future. The feasibility of this concept is already being proven in markets around the globe, indicating its potential for scalability and real-world application."
    


    if 'type' not in st.session_state:
        st.session_state['type'] = 'None'

    # File uploader for CSV
    uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])
    if uploaded_file is not None:
        st.session_state["uploaded_file"] = uploaded_file

    st.write("\n\n OR \n\n")

    # Manual entry for fields (required)
    problem = st.text_input("Problem", key="problem")
    solution = st.text_area("Proposed Solution", key="solution")

    # Coment this out if not using defaul
    # st.session_state['problem'] = problem
    # st.session_state['solution'] = solution


    

    # Next button to proceed to the evaluation page
    st.button("Next", on_click=handle_button_press)
