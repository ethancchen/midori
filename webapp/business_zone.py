
import streamlit as st
from PIL import Image
import lean_canvas.draw as d
import lean_api_call as lac

def page_business_zone():
    st.title("Business Zone Page")
    st.write("Lean Canvas Generated here")

    st.write(st.session_state["choice"])

    lean_row = st.session_state['lean_row'] 


    prob = lean_row['problem']
    sol = lean_row['solution']

    # st.write(prob)
    # st.write(sol)

    input_string = "Problem : " + prob + "\n" + "Solution : " + sol

    # st.write(input_string)

    problem_summary,solution_summary, uniq_val_prop, key_metrics, unfair_advtg, channels, customer_seg,cost_struct, revenue_streams = lac.get_data(input_string)
    

    img = d.draw(problem_summary,solution_summary, uniq_val_prop, key_metrics, unfair_advtg, channels, customer_seg,cost_struct, revenue_streams)
    st.image(img, caption='Uploaded Image.', use_column_width=True)