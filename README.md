# Text To SQL  

## Introduction  

Text To SQL is a Streamlit application that allows users to ask questions in English and generates corresponding SQL commands to retrieve data from a SQLite database. The application utilizes Google's Generative AI model to transform natural language questions into SQL commands, executing them to return the results.

## Features  

- Converts English questions into SQL commands.  
- Queries data from SQLite database with tables `STUDENT`, `LECTURER`, `COURSE`, and `REGISTRATION FORM`.  
- User-friendly interface, easy to use with Streamlit.  

## Database Structure  

The application interacts with the following tables in the SQLite database:  

- **STUDENT**  
  - ID_STU (primary key)  
  - NAME_STU  
  - BIRTHDAY_STU  
  - BIRTHPLACE_STU  

- **LECTURER**  
  - ID_LEC (primary key)  
  - NAME_LEC  
  - BIRTHDAY_LEC  
  - BIRTHPLACE_LEC  

- **COURSE**  
  - ID_COU (primary key)  
  - NAME_COU  
  - ID_LEC (foreign key referencing LECTURER)  

- **REGISTRATION_FORM**  
  - ID_REG (primary key)  
  - ID_COU (foreign key references COURSE)  
  - ID_STU (foreign key references STUDENT)  

## Deploying
- Text To SQL deployed website: [Text To SQL](https://alaindelong-text-to-sql.hf.space/)

## Installation  

### Requirements  

- Python 3.x  
- SQLite  
- Streamlit  
- google-generativeai  

### Installation Guide  

1. **Clone the Repository**  

   ```bash  
   git clone https://github.com/yourusername/yourrepository.git  
   cd yourrepository

2. **Install Required Libraries**
   Use pip to install the necessary libraries:
    ```bash
    pip install -r requirements.txt
3. **Configure API Key**
   Create a secrets.toml file in the root directory of the project and add your Google API key:
     ```bash
     [general]  
     GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
4. **Run the Application**
   Open the terminal and run the following command:
     ```bash
     streamlit run app.py
5. **Access the Application**
   Open your browser and navigate to http://localhost:8501 to use the application.

## How to Use
1. Enter your question in English into the input field.
2. Click the "Ask the question" button to receive the corresponding SQL command.
3. The query results will be displayed below.

## Testing and Maintenance
- Ensure that the SQLite database is properly set up with the required tables and data.
- Review and enhance the prompt in the AI model configuration to improve the accuracy of the SQL commands.
