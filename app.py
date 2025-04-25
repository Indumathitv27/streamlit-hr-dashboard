import streamlit as st
import psycopg2
import pandas as pd
import os
import base64


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
         f"""
         <style>
         [data-testid="stAppViewContainer"] {{
             background-image: url("data:image/png;base64,{encoded_string.decode()}");
             background-size: cover;
             background-position: center;
             background-repeat: no-repeat;
         }}
         [data-testid="stSidebar"] {{
             background-color: rgba(255, 255, 255, 0.9);
         }}
         [data-testid="stAppViewContainer"] > .main {{
             background-color: rgba(255, 255, 255, 0.85);
             padding: 2rem;
             border-radius: 12px;
         }}
         h1, h2, h3, h4, h5, h6, p {{
             color: #111111;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

# Usage:
add_bg_from_local('image.jpg')


# -----------------------------
# Sidebar for Query Type
# -----------------------------
st.sidebar.header("🔍 Query Options")
query_type = st.sidebar.selectbox(
    "Choose the type of query you want to run:",
    ("SELECT", "INSERT", "UPDATE", "DELETE")
)

# Immediate warning if risky type selected
if query_type in ["DELETE", "UPDATE"]:
    st.sidebar.warning("⚠️ DELETE and UPDATE queries can modify records. Use WHERE clause carefully!")

st.sidebar.markdown("---")
st.sidebar.info("ℹ️ Paste your query below and click 'Run Query'")
st.sidebar.success("Developed for HR Analytics 📊")

# -----------------------------
# Main Area
# -----------------------------
# Page title
st.title("💼 HR Employee Attrition – SQL Query Runner")

# Show Query Type
st.subheader(f"Query Type Selected: {query_type}")

# Show Example Syntax based on selected query type
st.markdown("### 🛠️ Example Syntax")

if query_type == "SELECT":
    st.code("SELECT * FROM employees WHERE age > 30;")
elif query_type == "INSERT":
    st.code("INSERT INTO employees (employeeid, age, gender) VALUES (1001, 28, 'Male');")
elif query_type == "UPDATE":
    st.code("UPDATE employees SET age = 29 WHERE employeeid = 1001;")
elif query_type == "DELETE":
    st.code("DELETE FROM employees WHERE employeeid = 1001;")

# Query input box
st.markdown("Enter a SQL query below (e.g., `SELECT * FROM employees LIMIT 10`):")
query = st.text_area("SQL Query", height=150)

# -----------------------------
# Query execution
# -----------------------------
if st.button("Run Query"):
    try:
        # Reconnect on every query run
        conn = psycopg2.connect(
            dbname=os.environ["DB_NAME"],
            user=os.environ["DB_USER"],
            password=os.environ["DB_PASSWORD"],
            host=os.environ["DB_HOST"],
            port=os.environ["DB_PORT"]
        )
        cursor = conn.cursor()

        # If SELECT, use pandas to show result
        if query.strip().lower().startswith("select"):
            df = pd.read_sql(query, conn)
            st.dataframe(df)
        else:
            cursor.execute(query)
            conn.commit()
            st.success("✅ Query executed successfully.")

    except Exception as e:
        st.error(f"❌ Error: {e}")

    finally:
        # Safely close everything
        try:
            cursor.close()
            conn.close()
        except:
            pass
