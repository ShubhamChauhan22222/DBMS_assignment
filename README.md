# 📌 Database Management System (DBMS) Project

## 📖 Project Overview
This project is designed to demonstrate a **relational database model** using **MySQL**, including appropriate **primary keys, foreign keys, constraints, views, indexing**, and execution of **basic and advanced SQL queries**. Additionally, a **Streamlit web app** has been created to interact with the database and display the tables dynamically.

## 📂 Repository Structure
- **ER-Diagram.png** → Entity-Relationship diagram representing the database schema
- **README.md** → Documentation for project details and usage instructions
- **app.py** → Python-based **Streamlit web app** for database interaction
- **queries** → SQL queries used for database creation and data manipulation

---

## 📊 Database Design & Requirements
### ✅ Completed Tasks
✔ Designed a **relational database model** with a minimum of **5 tables** with proper **foreign keys**  
✔ Created and implemented the **MySQL database**  
✔ Defined **primary keys, foreign keys, and additional constraints**  
✔ Created **views** for better accessibility of data  
✔ Indexed appropriate tables for **query optimization**  
✔ Executed basic queries: **INSERT, UPDATE, DELETE**  
✔ Ran **aggregate functions** along with **GROUP BY & HAVING** clauses  
✔ Implemented **subqueries** and used **various SQL operators**  
✔ Developed a **GUI-based Streamlit app** to interact with the database  

---

## ⚙ How to Run the Streamlit Web App (`app.py`)
Follow these steps to set up and run the **Streamlit web app** to visualize the database tables:

### 1️⃣ Prerequisites
Ensure you have the following installed:
- **Python (3.x recommended)**
- **MySQL Server**
- **MySQL Connector for Python** (`mysql-connector-python`)
- **Streamlit** (`pip install streamlit`)

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt  # If a requirements file exists
pip install streamlit mysql-connector-python  # Install manually if needed
```

### 4️⃣ Configure Database Connection
Ensure **MySQL is running** and update the connection details in **app.py** if necessary:
```python
conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="yourpassword",  # Update with your MySQL password
    database="shubh1"  # Ensure the correct database name
)
```

### 5️⃣ Run the App
```sh
streamlit run app.py
```
This will launch the web application in your browser where you can explore the database dynamically!

---

## 📌 Features of the Streamlit Web App
- Displays **available databases** from MySQL
- Lists all **tables** when clicking on the "Show Tables" button
- Dynamically displays **table content** when a specific table is selected

---

## 🎯 Additional Information
This project was completed as per the **DBMS assignment requirements**, covering all necessary SQL operations and additional features like **GUI interaction** for better visualization.

🚀 *Happy Coding!*


