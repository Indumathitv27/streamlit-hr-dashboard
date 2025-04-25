import streamlit as st
import psycopg2
import pandas as pd
import os
import base64

# -----------------------------
# Function: Add background image and style
# -----------------------------
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
        <style>
        /* Background image */
        [data-testid="stAppViewContainer"] {{
            background-image: url("data:image/jpeg;base64,{encoded_string.decode()}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        /* White overlay for better visibility */
        [data-testid="stAppViewContainer"] > .main {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 12px;
        }}

        /* Sidebar transparency */
        [data-testid="stSidebar"] {{
            background-color: rgba(255, 255, 255, 0.9);
        }}

        /* Font and input styling */
        .stTextInput, .stTextArea, .stSelectbox, .stButton, .stMarkdown {{
            color: #111111 !important;
            font-size: 16px !important;
        }}

        h1, h2, h3 {{
            color: #222222 !important;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Page configuration and layout
# -----------------------------
st.set_page_config(page_title="HR Employee Attrition - SQL Runner", layout="wide")
add_bg_from_local("background.jpg")  # Make sure this file exists in the same directory

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.header("🔍 Query Options")
query_type = st.sidebar.selectbox(
    "Choose the type of query you want to run:",
    ("SELECT", "INSERT", "UPDATE", "DELETE")
)
st.sidebar.markdown("---")
st.sidebar.info("ℹ️ Paste your query below and click 'Run Query'")
st.sidebar.success("Developed for HR Analytics 📊")

# -----------------------------
# Main Area
# -----------------------------
st.title("💼 HR Employee Attrition – SQL Query Runner")
st.caption("🔹 Analyze attrition trends, salaries, and performance using live queries")

st.subheader(f"Query Type: {query_type}")
query = st.text_area("📝 Write your SQL Query here:", height=200)

# -----------------------------
# Database connection
# -----------------------------
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"]
    )

# -----------------------------
# Run Query Button
# -----------------------------
if st.button("▶️ Run Query"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        st.markdown("---")
        st.subheader("📄 SQL Query Submitted")
        st.code(query, language='sql')

        if query_type == "SELECT" and query.strip().lower().startswith("select"):
            df = pd.read_sql(query, conn)
            with st.expander("🔽 View Query Results", expanded=True):
                st.dataframe(df)
            st.success("✅ SELECT query executed successfully!")
        else:
            cursor.execute(query)
            conn.commit()
            st.success(f"✅ {query_type} query executed successfully!")

    except Exception as e:
        st.error(f"❌ Error executing query: {e}")

    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
