# 🤖 Gemini LLM SQL Chat & Data Summarization App
🔍 *Gemini API • Text-to-SQL • MySQL • Faker • Streamlit*

## 🚀 Tech Stack & Domains
![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LLM](https://img.shields.io/badge/LLM-Gemini%20API-brightgreen)
![Database](https://img.shields.io/badge/Database-MySQL-orange?logo=mysql)
![Faker](https://img.shields.io/badge/Data-Faker-purple)
![Streamlit](https://img.shields.io/badge/Framework-Streamlit-red?logo=streamlit)
![Domain](https://img.shields.io/badge/Domain-NLP%20%26%20Data%20Analytics-navy)

---

## 📘 Overview
This project allows users to interact with a **MySQL database using natural language** through a chat interface powered by the **Gemini API**.

The system converts user text into SQL queries, retrieves data, and summarizes the results in clear language. Users do not need SQL knowledge to explore structured data.

---

## 🎯 Problem Statement
Querying relational databases requires SQL skills, which blocks access for non-technical users and slows analysis.

This project enables:
- Natural language database queries  
- Automatic SQL generation using Gemini  
- Data retrieval and summarization in one flow  

---

## 💼 Use Cases
| Use Case | Description |
|--------|-------------|
| 🗣️ Text-based Queries | Ask database questions in plain English |
| 📊 Data Analysis | Explore student records quickly |
| 🧾 Reporting | Generate summaries from query results |
| 🎓 Education | Learn how text maps to SQL queries |

---

## 🗃️ Dataset Generation
- Synthetic data generated using **Python Faker**
- ~**10,000 records**
- Saved as CSV and imported into MySQL

### Data Fields
- Name  
- Gender  
- Department  
- Year  
- Batch year  
- Phone number  
- Country, State  
- Hostel  
- Sports student (Yes / No)  
- Sport type (Cricket, Football, Volleyball, Chess, etc.)  
- Arrear status  
- Arrear subjects  
- Fees paid  

---

## 🗺️ Project Workflow

### 🧾 1 — Data Creation
- Faker-based Python scripts
- CSV generation
- MySQL table setup and data import

### 🤖 2 — Text to SQL
- User submits query via Streamlit chat
- Gemini API generates SQL query
- SQL executed on MySQL

### 📊 3 — Retrieval
- Query results fetched from database

### 📝 4 — Summarization
- Gemini summarizes retrieved data
- User receives a clean response

### 🌐 5 — UI
- Streamlit chat interface
- Real-time interaction

---

<summary>📸 Click to view Streamlit UI screenshots</summary>

#### Home Page  
![Home Page](https://github.com/user-attachments/assets/2d851c95-910b-4efb-93e9-e75da8e3a062)


#### Results Page  1
![Result Page](https://github.com/user-attachments/assets/4d65c6e9-9e19-4e86-a091-a76f6fd2ade6)


#### Results Page  2
![Result Page](https://github.com/user-attachments/assets/b938c4b2-5916-4b63-8286-983766ab085)


---


## 📁 Project Structure
```
Text-to-MYSQL-Chat-Application/  
│  
├── ENV/  
│   └── .env 
│  
├── Main UI/  
│   └── app.py 
│  
├── requirements.txt  
└── README.md  

```
---

## 🛠️ Installation & Execution

Clone repository:
```
git clone git clone https://github.com/sarankumar74/Text-to-MYSQL-Chat-Application.git
cd Text-to-MYSQL-Chat-Application
```

Install dependencies:
```
pip install -r requirements.txt
```

Run Streamlit app:

---

## 🔒 Notes
- Requires a valid Gemini API key  
- MySQL must be running locally or remotely  
- Designed for text-to-SQL and data summarization workflows
