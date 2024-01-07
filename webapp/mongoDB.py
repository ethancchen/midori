import pymongo
import streamlit as st

client = pymongo.MongoClient("mongodb+srv://jiashuchen:" 
                            + st.secrets["mongo_password"] 
                            + "@cluster0.epj60wr.mongodb.net/?retryWrites=true&w=majority")

db = client.myDatabase

# use a collection named "users"
my_collection = db["users"]