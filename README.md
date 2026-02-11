💰 FinTrack Pro – CLI Finance Manager

FinTrack Pro is a command-line based personal finance management system developed using Python, SQLite, and SQLAlchemy ORM.
The application allows users to manage daily expenses, categorize spending, set monthly budgets, and generate simple analytics reports — all through a terminal interface.

📌 Project Purpose

This project was built to strengthen understanding of:

Object Relational Mapping (ORM)

CRUD operations

Relational database design

SQL joins and aggregation

Python database integration

Command-line application development

It is suitable for academic submission, resume showcase, and interview demonstrations.

🛠️ Technologies Used

Python

SQLite Database

SQLAlchemy ORM

Raw SQL (for reporting)

Command Line Interface

🚀 Key Features

Add new expenses

Delete existing expenses

Search expenses by date

View category-wise spending summary

Set monthly budget limits

Check whether budget is exceeded

Persistent local database storage

🗄️ Database Design Overview

The system consists of three main tables:

Category

Stores types of expenses such as Food, Travel, Shopping, etc.

Expense

Stores individual expense records including title, amount, date, and linked category.

Budget

Stores monthly spending limits for comparison against total expenses.

Relationship

There is a one-to-many relationship between Category and Expense, where one category can contain multiple expenses.

📊 Reporting

The application generates category-wise spending analytics using SQL aggregation and JOIN operations.
This demonstrates understanding of relational queries and data analysis fundamentals.

🎯 Learning Outcomes

Through this project, I gained practical experience in:

Mapping Python classes to database tables using ORM

Performing Create, Read, Update, and Delete operations

Designing normalized relational database structures

Writing SQL queries for analytics

Building structured and modular CLI applications

🔮 Future Improvements

CSV export functionality

Web interface using Flask

User authentication system

Data visualization with charts

Multi-user support

💡 Conclusion

FinTrack Pro demonstrates how Python can be effectively integrated with relational databases to build real-world applications.
It reflects a strong understanding of database concepts, backend logic, and structured programming practices.
