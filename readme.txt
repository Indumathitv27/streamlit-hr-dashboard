README: HR Employee Attrition – Data Setup and Execution Guide

The initial dataset is downloaded from Kaggle which had around 1500 rows which are not sufficient. So we have used a python script to generate rows and then create a dataset which have now around 5000 records.
Kaggle Link for original source - https://www.kaggle.com/code/faressayah/ibm-hr-analytics-employee-attrition-performance/input
This file has only around 1000 records so we used Dataset_Generation.ipynb script to generate data.

1. Dataset Generation:
The file `Dataset_Generation.ipynb` contains the Python script used to generate synthetic HR employee data. The output is saved as `HR_Employee_Attrition.csv`.

2. Loading into Database:
The CSV file was loaded into a staging table (`hr_emp_staging`) created in the PostgreSQL database. From this table, data is split into 7 tables using SQL insert queries.

3. File Descriptions:
- create_phase1.sql: Contains all SQL commands to create tables in the database in phase1 before BCNF and decomposition.
- load.sql: Contains the insert statements to populate the 7 normalized tables from the staging table.
- HR_Employee_Attrition.csv: Raw synthetic data generated via the Python notebook along with the real data downloaded from the Kaggle source
- Dataset_Generation.ipynb: Script used to generate the data.
- create_insert_phase2.sql - create and insert commnads used for Task6 - BCNF and decomposed tables.
- image.jpg: Background image used in the Streamlit web app UI.
- app.py: Streamlit web interface to run SQL queries on the database.
- requirements.txt: Python package dependencies to run the app.

4. Execution Order:
   1. Run `create_phase1.sql` in pgAdmin or psql to create all tables.
   2. Use Import to load the CSV file obtained from python script into `hr_emp_staging`.
   3. Run `load.sql` to populate normalized tables from staging table.
   4. Launch the Streamlit app using `streamlit run app.py`.

5. hosted website to run SQL Query : https://hr-employee-attrition.streamlit.app/

