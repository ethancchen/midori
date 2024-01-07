
import streamlit as st
from PIL import Image
import lean_canvas.draw as d
import lean_api_call as lac

def page_business_zone():
    st.title("Business Zone Page")
    st.write("Lean Canvas Generated here")

    st.write(st.session_state["choice"])

    lean_row = st.session_state['lean_row'] 


    prob = lean_row['Problem ']
    sol = lean_row['Solution']

    # st.write(prob)
    # st.write(sol)

    input_string = "Problem : " + prob + "\n" + "Solution : " + sol

    # st.write(input_string)



    problem_summary,solution_summary, uniq_val_prop, key_metrics, unfair_advtg, channels, customer_seg,cost_struct, revenue_streams = lac.get_data(input_string)
    

    img = d.draw(problem_summary,solution_summary, uniq_val_prop, key_metrics, unfair_advtg, channels, customer_seg,cost_struct, revenue_streams)
    st.image(img, caption='Uploaded Image.', use_column_width=True)
    
    































"""
Problem statement: [Insert the problem statement here, clearly explaining the issue being addressed.]
Potential solution: [Insert the potential solution here, describing how it aims to solve the problem.]

Generate a concise and informative lean canvas based on the following problem statement and potential solution. Provide responses within the specified character limits and formats.
make sure that you provide answer to each of these prompts on a new line

Specific prompts:

Problem summary: Summarize the problem in under 450 characters.
Solution summary: Summarize the solution in under 200 characters.
Unique value proposition: What's the unique value proposition for the provided solution? Answer in 1 sentence under 450 characters.
Key metrics: What are the key metrics for the provided solution? Answer in paragraph form under 200 characters.
Unfair advantages: What are some unfair advantages that other companies may have that could affect the effectiveness of the solution? Answer in paragraph form under 200 characters.
Channels: How can one provide this solution to customers? Answer in paragraph form under 200 characters.
Customer segments: Who are the target customers? Answer in one sentence under 450 characters.
Cost structure: What is the cost structure for this solution? Answer in one sentence under 470 characters.
Revenue streams: What are different types of revenue streams for this solution? Answer in paragraph form under 470 characters.

"""


