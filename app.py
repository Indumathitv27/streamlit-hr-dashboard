import streamlit as st
 import pandas as pd
 import psycopg2
 
 st.title("💼 HR Employee Attrition – SQL Query Runner")
 
 # SQL input
 st.markdown("Enter a SQL query below (e.g., `SELECT * FROM employees LIMIT 10`):")
 query = st.text_area("SQL Query", height=150)
 
 # DB connection
 @st.cache_resource
 def get_connection():
     return psycopg2.connect(
         dbname="HR_Employee_Attrition",
         user="postgres",
         password="SRelajdu%27", 
         host="127.0.0.1",
         port="5432"
     )
 
 # Query execution
 if st.button("Run Query"):
     conn = get_connection()
     cursor = conn.cursor()
     try:
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
         cursor.close()
         conn.close()