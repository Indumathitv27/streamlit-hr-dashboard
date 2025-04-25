import streamlit as st
import psycopg2
import pandas as pd
import os

# Page title
st.title("💼 HR Employee Attrition – SQL Query Runner")

# Query input box
st.markdown("Enter a SQL query below (e.g., `SELECT * FROM employees LIMIT 10`):")
query = st.text_area("SQL Query", height=150)

# Query execution
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
            st.success("Query executed successfully.")

    except Exception as e:
        st.error(f"Error: {e}")

    finally:
        # Safely close everything
        try:
            cursor.close()
            conn.close()
        except:
            pass