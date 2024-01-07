
import streamlit as st
from PIL import Image
import lean_canvas.draw as d

def page_business_zone():
    st.title("Business Zone Page")
    st.write("Lean Canvas Generated here")

    img = d.draw()
    st.image(img, caption='Uploaded Image.', use_column_width=True)

    lean_row = st.session_state['lean_row'] 
