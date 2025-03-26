import streamlit as st
import mysql.connector

# Function to create a new database connection
def get_db_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="2103",  # Ensure this is your actual password
        database="shubh1",
        charset="utf8mb4",
        collation="utf8mb4_general_ci"
    )

# Function to get list of tables
def get_tables():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SHOW TABLES;")
    tables = [table[0] for table in cursor.fetchall()]
    cursor.close()
    conn.close()
    return tables

# Function to fetch data from a table
def get_table_data(table_name):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM {table_name};")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data

# Streamlit UI
st.title("📊 Database Explorer")
st.title("UNIVERSITY Database")
# Initialize session state for tables if not already set
if "tables" not in st.session_state:
    st.session_state.tables = None

# When button is clicked, fetch tables and store them in session state
if st.button("Show Tables"):
    st.session_state.tables = get_tables()

# If tables are already fetched, show the dropdown
if st.session_state.tables:
    selected_table = st.selectbox("Select a table:", st.session_state.tables)

    if selected_table:
        st.write(f"📋 **Displaying Table: {selected_table}**")
        table_data = get_table_data(selected_table)
        st.dataframe(table_data)
