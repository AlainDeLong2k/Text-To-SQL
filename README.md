# Gemini App to Retrieve SQL Data  

## Introduction  

Gemini App is a Streamlit application that allows users to ask questions in English and receive the corresponding SQL commands to query data from a SQLite database. The application utilizes Google's Generative AI model to transform natural language questions into SQL statements.  

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
  - ID_COU (foreign key referencing COURSE)  
  - ID_STU (foreign key referencing STUDENT)  

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
