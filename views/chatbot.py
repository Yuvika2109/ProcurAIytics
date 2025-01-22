import streamlit as st
from streamlit_lottie import st_lottie
import json
from dotenv import load_dotenv
import os
import mysql.connector
import google.generativeai as genai
import re

def load_lottiefile(filepath: str):
    """Load a Lottie animation file."""
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)

# Load Lottie animation for display
lottie_coding = load_lottiefile("coding.json")


col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<h1 style='text-align: left; line-height: 1.5;'>Chatbot</h1>", unsafe_allow_html=True)
with col2:
    st_lottie(lottie_coding, height=200, width=600, loop=True, speed=1, quality="low")

load_dotenv()  


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(question, prompt):
    try:
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content([prompt[0], question])
        return response.text
    except Exception as e:
        st.error(f"Error in generating response: {e}")
        return None


def read_sql_query(sql, db):
    try:
        # Connect to MySQL database
        connection = mysql.connector.connect(
            host="localhost",    
            user="root",          
            password="yuvika@1234",  
            database=db,           
        )
        cursor = connection.cursor()

   
        cursor.execute(sql)
        rows = cursor.fetchall()

        connection.commit()
        connection.close()

        return rows
    except mysql.connector.Error as err:
        st.error(f"Database error: {err}")
        return []
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")
        return []


prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name tsdpl and contains a table named details with the following columns: 
    id, doc_no, material, text, location, quantity, price, validity, doc_type, grp, supplier, net_value.

    Examples:
    

Example 1: "How many items are there in the database?"
SQL Query: SELECT COUNT(*) FROM details;

Example 2: "How much did we buy against material number 102?"
SQL Query: SELECT SUM(quantity) FROM details WHERE material = 102;

Example 3: "How much was spent on material group or code 101?"
SQL Query: SELECT SUM(net_value) FROM details WHERE grp = '101';

Example 4: "What is the total spend for a keyword I enter, such as 'ACP'?"
SQL Query: SELECT 
    SUM(net_value) AS total_spend
FROM 
    details
WHERE 
    text LIKE CONCAT('%', 'ACP', '%');

Example 5: "How much was spent on purchasing group ZCS?"
SQL Query: SELECT SUM(net_value) FROM details WHERE doc_type = 'ZCS';

Example 6: "How many items did we buy over one lakh?"
SQL Query: SELECT COUNT(*) FROM details WHERE net_value > 100000;

Example 7: "What was the location code-wise breakdown of VCR1?"
SQL Query: SELECT location, SUM(quantity) FROM details WHERE location = 'VCR1' GROUP BY location;

Example 8: "What items were bought against purchase order number 4500424576?"
SQL Query: SELECT * FROM details WHERE doc_no = 4500424576;

Example 9: "How much value was ordered on supplier no TISC04?"
SQL Query: SELECT SUM(net_value) FROM details WHERE supplier = 'TISC04 TATA STEEL LTD';

Example 10: "What is the total spending grouped by each supplier?"SQL Query: SELECT supplier, SUM(net_value) AS total_spent FROM details GROUP BY supplier;

Example 11: "What is the average cost per material?"
SQL Query: SELECT material, AVG(price) AS average_cost FROM details GROUP BY material;

Example 12: "What is the top 5 materials by total quantity purchased?"
SQL Query: SELECT material, SUM(quantity) AS total_quantity FROM details GROUP BY material ORDER BY total_quantity DESC LIMIT 5;

Example 13: "What is the total quantity purchased by each location?"
SQL Query: SELECT location, SUM(quantity) AS total_quantity FROM details GROUP BY location;

Example 14: "What is the total quantity purchased by each supplier?"
SQL Query: SELECT supplier, SUM(quantity) AS total_quantity FROM details GROUP BY supplier;

Example 15: "What is the total quantity purchased by each validity?"
SQL Query: SELECT validity, SUM(quantity) AS total_quantity FROM details GROUP BY validity;

Example 16: "What is the total quantity purchased by each document type?"
SQL Query: SELECT doc_type, SUM(quantity) AS total_quantity FROM details GROUP BY doc_type;

Example 18: "Which suppliers contribute most to overspending?"
SQL Query: SELECT supplier, SUM(net_value) AS total_spent FROM details GROUP BY supplier HAVING total_spent > 1000000 ORDER BY total_spent DESC;

Example 19: "What are the top 3 locations by total spending?"
SQL Query: SELECT location, SUM(net_value) AS total_spent FROM details GROUP BY location ORDER BY total_spent DESC LIMIT 3;

Example 20: "What is the projected spending for next quarter if we reduce costs by 15%?"
SQL Query: SELECT SUM(net_value) * 0.85 AS projected_spending FROM details;

Example 21: "What materials have the highest unit price?"
SQL Query: SELECT material, price FROM details ORDER BY price DESC LIMIT 5;

Example 22: "Which purchase groups have the highest average spending?"
SQL Query: SELECT doc_type, AVG(net_value) AS avg_spent FROM details GROUP BY doc_type ORDER BY avg_spent DESC;

Example 23: "Which suppliers have higher average costs compared to others in the same material group?"
SQL Query: SELECT supplier, grp, AVG(price) AS avg_cost FROM details GROUP BY supplier, grp ORDER BY avg_cost DESC;

Example 24: "What is the total spend for a supplier named 'apex'?"
SQL Query: SELECT 
    SUM(net_value) AS total_spend
FROM 
    details
WHERE 
    supplier LIKE CONCAT('%', 'apex', '%');



   Do not include sql or code formatting (` ``` `) in the output.
    """
]


question = st.text_input("Input your question: ", key="input")

submit = st.button("Ask the question")


if submit:
    response = get_gemini_response(question, prompt)

    if response:
        if "details" in response.lower():
            response_data = read_sql_query(response, "tsdpl")

            st.subheader("Answer:")
            if response_data:
                for row in response_data:
                    formatted_output = " | ".join(
                        f"{x:,.2f} Rs." if isinstance(x, (int, float)) and "net_value" in response.lower() else str(x)
                        for x in row
                    )
                    st.markdown(
                        f"<h5>{formatted_output}</h5>",
                        unsafe_allow_html=True,
                    )
            else:
                st.markdown("<h5>No relevant data found. Showing Rs.0 for spending-related queries.</h5>", unsafe_allow_html=True)
        else:
            st.error("Invalid SQL query. Ensure it references the correct table (details).")

                       
   


