from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import mysql.connector
import google.generativeai as genai


# 1. Configure Gemini

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))



# 2. TEXT-TO-SQL GENERATOR

def generate_sql_query(question):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
    You are an advanced MySQL Text-to-SQL generator designed for highly accurate, 
    schema-aligned SQL query generation. Your job is to convert the user's natural 
    language question into the most precise SQL SELECT query possible.


    Columns:
    id,
    full_name,
    gender,
    academic_year,
    year_of_study,
    roll_number_with_degree,
    address,
    phone_number,
    state,
    pincode,
    department,
    hostel,
    day_scholar,
    bus_traveller,
    sports_participation,
    paid_semesters,
    unpaid_semesters,
    arrear_status,
    arrear_paper_names


    1. Output ONLY valid, executable MySQL SQL.
    2. NEVER return markdown formatting (no ``` blocks).
    3. NEVER explain your reasoning.
    4. NEVER invent new table names or columns.
    5. ALWAYS use existing column names exactly as written.
    6. Assume user queries refer to this table unless stated otherwise.
    7. Generate the BEST SQL for retrieval — prefer SELECT columns explicitly when possible.
    8. If user asks for summaries (count, group, filter, sort), produce optimized SQL:
   - Use COUNT(), GROUP BY, ORDER BY, LIKE, AND/OR when appropriate.
    9. If user asks vague queries ("students in hostel"), infer the best column
       and produce the correct SQL: 
       hostel = 'Hostel'
    10. When user input is incomplete, still produce the MOST reasonable SQL.
    11. NEVER modify the user's intent.
    12. ALWAYS ensure final output is a single clean SQL query.


    User: "how many boys are in second year?"
    → gender = 'Male', year_of_study = '2nd Year'
    → SQL: SELECT COUNT(*) FROM students WHERE gender = 'Male' AND year_of_study = '2nd Year';

    User: "show hostel girls in BCA"
    → SQL: SELECT full_name, department, hostel FROM students 
        WHERE gender = 'Female' AND department = 'BCA' AND hostel = 'Hostel';

    User: "students who have unpaid semesters"
    → SQL: SELECT * FROM students WHERE unpaid_semesters IS NOT NULL;


    Return ONLY the SQL query and nothing else.

    User question: {question}
    """

    response = model.generate_content(prompt)
    return response.text.strip()


# 3. SQL CLEANER

def clean_sql(sql):
    sql = sql.replace("```sql", "").replace("```", "").strip()
    if sql.endswith(";"):
        sql = sql[:-1]
    return sql


# 4. SQL EXECUTION

def execute_sql(query):
    conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Pass",
            database="student data management"
        )
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# 5. AUTO-CORRECTION ENGINE

def fix_sql_error(bad_sql, error_message, question):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
Fix this SQL query.

BAD SQL:
{bad_sql}

ERROR:
{error_message}

USER QUESTION:
{question}

Return only corrected SQL without markdown.
"""

    response = model.generate_content(prompt)
    return response.text.strip()


# 6. SQL RESULT SUMMARIZER

def summarize_results(rows, sql_query):
    model = genai.GenerativeModel("models/gemini-2.5-flash")

    prompt = f"""
Summaries this SQL output in simple English:

SQL:
{sql_query}

RESULTS:
{rows}

Rules:
- Be clear, simple.
- No invented data.
"""

    response = model.generate_content(prompt)
    return response.text.strip()


# 7. Streamlit CHAT UI 

st.set_page_config(page_title="Text-to-SQL Chat", layout="wide")

st.title("😎 AI Chat — Text to SQL for MySQL Students DB")

st.sidebar.title("📄 Students Table Schema")
st.sidebar.markdown("""
- id  
- full_name  
- gender  
- academic_year  
- year_of_study  
- roll_number_with_degree  
- address  
- phone_number  
- state  
- pincode  
- department  
- hostel  
- day_scholar  
- bus_traveller  
- sports_participation  
- paid_semesters  
- unpaid_semesters  
- arrear_status  
- arrear_paper_names  
""")


# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []


# Display previous messages

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


# User Input Box 

user_input = st.chat_input("Ask anything about your students database...")


# When user sends a message

if user_input:

    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Generating SQL..."):
            ai_sql = generate_sql_query(user_input)
            sql_query = clean_sql(ai_sql)
            st.write("📝 **Generated SQL:**")
            st.code(sql_query)

    try:
        rows = execute_sql(sql_query)
        final_sql = sql_query
    except Exception as e:
        with st.chat_message("assistant"):
            with st.spinner("SQL error detected — fixing..."):
                corrected = fix_sql_error(sql_query, str(e), user_input)
                final_sql = corrected
                rows = execute_sql(corrected)
                st.write("🔧 **Corrected SQL:**")
                st.code(final_sql)


    with st.chat_message("assistant"):
        if len(rows) == 0:
            st.warning("No matching records found.")
        else:
            st.write("📊 **Query Results:**")
            st.table(rows)

            with st.spinner("Summarizing results..."):
                summary = summarize_results(rows, final_sql)

            st.write("🧠 **Summary:**")
            st.write(summary)

    st.session_state.messages.append({
        "role": "assistant",
        "content": f"Generated SQL:\n{final_sql}\n\nSummary:\n{summary}"
    })
