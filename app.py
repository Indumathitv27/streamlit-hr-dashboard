import streamlit as st
import psycopg2
import pandas as pd
import os

# Set up page configuration
st.set_page_config(page_title="HR Employee Attrition - SQL Runner", layout="wide")

# App Title
st.title("💼 HR Employee Attrition – Interactive SQL Query Runner")

# Sidebar for Inputs
st.sidebar.header("🔍 Query Options")

query_type = st.sidebar.selectbox(
    "Choose the type of query you want to run:",
    ("SELECT", "INSERT", "UPDATE", "DELETE")
)

st.sidebar.markdown("---")

st.sidebar.write("ℹ️ Paste your SQL query below and click Run:")

# Main Area
st.subheader(f"Query Type: {query_type}")
query = st.text_area("Write your SQL query here:", height=200)

# Database connection function
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"]
    )

# Execute query on button click
if st.button("▶️ Run Query"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        if query_type == "SELECT" and query.strip().lower().startswith("select"):
            df = pd.read_sql(query, conn)
            st.success("✅ Query executed successfully! Here's the result:")
            st.dataframe(df)
        else:
            cursor.execute(query)
            conn.commit()
            st.success("✅ Non-SELECT query executed successfully!")

    except Exception as e:
        st.error(f"❌ Error occurred while executing the query: {e}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass

st.sidebar.markdown("---")
st.sidebar.write("🛡️ **Tip:** Be cautious with DELETE/UPDATE commands.")
