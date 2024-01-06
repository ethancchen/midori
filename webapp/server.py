import streamlit as st
import pyodbc
# Initialize connection.
# Uses st.cache_resource to only run once.
@st.cache_resource
def init_connection():
    return pyodbc.connect(
      "DRIVER={ODBC Driver 18 for SQL Server};Server=tcp:midori.database.windows.net,1433;Database=streamlit;Uid=jsch;Pwd={Cjs_1990987};Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;",
      autocommit = True
      )

conn = init_connection()

cursor = conn.cursor()
@st.cache_data(ttl=None)
def create():
    cursor.execute('''
        CREATE TABLE PeopleInfo (
                PersonId INTEGER PRIMARY KEY,
                FirstName TEXT NOT NULL,
                LastName  TEXT NOT NULL,
                Age INTEGER NULL,
                CreatedAt TEXT DEFAULT CURRENT_TIMESTAMP NOT NULL
        
        );
        ''')
conn.commit()
@st.cache_data(ttl=None)
def insert():
    cursor.execute('''
                INSERT INTO PeopleInfo (PersonId, FirstName, LastName, Age)
                VALUES
                (1,'Bob','Smith', 55),
                (2, 'Jenny','Smith', 66)
                ''')
conn.commit()

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=1000)
def run_query(query):
    with init_connection().cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Run a SELECT query on the 'products' table
rows = run_query("SELECT * FROM PeopleInfo;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
