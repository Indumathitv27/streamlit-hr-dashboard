import streamlit as st
import pandas as pd
import psycopg2
import os

# Set up custom page configuration
st.set_page_config(page_title="HR Employee Attrition – SQL Explorer", layout="wide")

# Set background image using CSS
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1581090700227-1c065cfc8bc2?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

[data-testid="stSidebar"] {
    background-color: rgba(255, 255, 255, 0.7);
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# Title and description
st.title("💼 HR Employee Attrition – SQL Query Runner")
st.caption("🔹 Analyze attrition trends, salaries, and employee performance in real-time")

# Sidebar for Query Type
st.sidebar.header("🔍 Query Options")
query_type = st.sidebar.selectbox(
    "Select your query type:",
    ("SELECT", "INSERT", "UPDATE", "DELETE")
)

st.sidebar.info("ℹ️ Paste your query below and click 'Run Query'!")

# Text area for SQL input
query = st.text_area("📝 Write your SQL Query here:", height=200)

# Database Connection
@st.cache_resource
def get_connection():
    return psycopg2.connect(
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        host=os.environ["DB_HOST"],
        port=os.environ["DB_PORT"]
    )

# Query Execution
if st.button("▶️ Run Query"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        st.markdown("---")
        st.subheader("📄 SQL Query You Submitted:")
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

st.sidebar.markdown("---")
st.sidebar.success("Developed for HR Analytics 📈")
