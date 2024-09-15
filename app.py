import streamlit as st
import sqlite3
import google.generativeai as genai

# Configure API key
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])


# Function to load Gemini Model and provide SQL query as response
def get_gemini_response(prompt, question):
    # model = genai.GenerativeModel("gemini-1.5-flash")
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt, question])
    return response.text


# Function to retrieve query from the SQL database
def read_sql_query(sql, db):
    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()

    for row in rows:
        print(row)
    return rows


# Define prompt
prompt = """
    You are an expert in converting English questions to SQL query!
    The SQL database has 4 tables include STUDENT, LECTURER, COURSE, REGISTRATION FORM.
    STUDENT has the following columns - ID_STU(primary key), NAME_STU, BIRTHDAY_STU and BIRTHPLACE_STU.
    LECTURER has the following columns - ID_LEC(primary key), NAME_LEC, BIRTHDAY_LEC and BIRTHPLACE_LEC.
    COURSE has the following columns - ID_COU(primary key), NAME_COU, ID_LEC(foreign key references LECTURER(ID_LEC)).
    REGISTRATION_FORM has the following columns - ID_REG(primary key), ID_COU(foreign key references COURSE(ID_COU)), ID_STU(foreign key references STUDENT(ID_STU)).
    
    For example,
    Example 1 - How many entries of STUDENT table are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;
    Example 2 - Tell me all the students having birthplace Hải Phòng?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE BIRTHPLACE_STU = 'Hải Phòng';
    Example 3 - Tell me all the course lecturer Đặng Quốc Việt teaching?,
    the SQL command will be something like this SELECT B.NAME_COU FROM LECTURER A JOIN COURSE B ON A.ID_LEC = B.ID_LEC WHERE A.NAME_LEC = 'Đặng Quốc Việt';
    Example 4- Tell me all the students studying 2 or more classes?,
    the SQL command will be something like this SELECT A.NAME_STU FROM STUDENT A JOIN REGISTRATION_FORM B ON A.ID_STU = B.ID_STU GROUP BY A.NAME_STU HAVING COUNT(B.ID_COU) > 1;

    note that the SQL code must not start and end with ``` and must not contain the "sql" word in output.
"""

# Streamlit App
st.set_page_config(page_title="Text to SQL")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input", key="input")
submit = st.button("Ask the question")

# If submit is clicked
if submit:
    response = get_gemini_response(prompt, question)
    print(response)

    data = read_sql_query(response, "database/student.db")
    st.subheader("Result")
    for row in data:
        st.subheader(row)
