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

# Pass a table as string, records is a list of recoreds in string.
@st.cache_data(ttl=None)
def create_table(cmd):
    cursor.execute(cmd)
    conn.commit()
    
# Pass a table as a string.    
@st.cache_data(ttl=None)
def remove_table(table):
    cmd = "DROP TABLE " + table
    cursor.execute(cmd)
    conn.commit()
    
# Pass a table as a string, records is a list of records in string.
@st.cache_data(ttl=None)
def insert_record(table, columns, records):
    cmd = "INSERT INTO " + table + " ("
    cmd = cmd + columns[0]
    
    for i in range(1, len(columns)):
        cmd = cmd + ", " + columns[i]
    cmd = cmd + ") VALUES "
    
    for row in records:
        cmd = cmd + "(" + row + ") "
    
    cmd = cmd + ";"
    cursor.execute(cmd)
    conn.commit()
    
#remove_table("PeopleInfo")
insert_record("Test", ["userId", "pwd_hash"], ["'user7', '5671732671536725187658675483625143'"])
insert_record("Test", ["userId", "pwd_hash"], ["'user8', '1321345356425432543254325'"])
# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=None)
def run_query(query):
    with init_connection().cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

# Run a SELECT query on the 'products' table
rows = run_query("SELECT * FROM Test;")

for row in rows:
    st.write(row)