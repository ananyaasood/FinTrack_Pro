"""
FinTrack Pro
"""

# importing required things
from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, text
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# creating database connection
engine = create_engine("sqlite:///fintrack.db", echo=False)

# session helps us talk to the database
Session = sessionmaker(bind=engine)
session = Session()

# base class for tables
Base = declarative_base()

# -------------------------------
# TABLES
# -------------------------------

class Category(Base):
    # this table stores expense categories
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    # one category can have many expenses
    expenses = relationship("Expense", back_populates="category")


class Expense(Base):
    # this table stores each expense
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    amount = Column(Float)
    date = Column(String)

    # links expense to category
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="expenses")


class Budget(Base):
    # this table stores monthly budget
    __tablename__ = "budgets"

    id = Column(Integer, primary_key=True)
    month = Column(String)
    limit = Column(Float)


# creates tables if they don’t exist
Base.metadata.create_all(engine)

# -------------------------------
# EXPENSE FUNCTIONS
# -------------------------------

def add_expense():
    # takes input from user
    title = input("Title: ")
    amount = float(input("Amount: "))
    date = input("Date (YYYY-MM-DD): ")
    category_name = input("Category: ")

    # check if category already exists
    category = session.query(Category).filter_by(name=category_name).first()

    # if not, create new category
    if not category:
        category = Category(name=category_name)
        session.add(category)
        session.commit()

    # creating expense object
    expense = Expense(
        title=title,
        amount=amount,
        date=date,
        category=category
    )

    # saving expense to database
    session.add(expense)
    session.commit()
    print("Expense added")


def delete_expense():
    # delete expense using id
    eid = int(input("Enter expense ID: "))
    expense = session.query(Expense).get(eid)

    if expense:
        session.delete(expense)
        session.commit()
        print("Expense deleted")
    else:
        print("Expense not found")

# -------------------------------
# SEARCH
# -------------------------------

def search_by_date():
    # search expenses for a specific date
    date = input("Enter date: ")
    expenses = session.query(Expense).filter_by(date=date).all()

    print("Expenses on", date)
    for e in expenses:
        print(e.id, e.title, e.amount)

# -------------------------------
# REPORT (RAW SQL)
# -------------------------------

def category_report():
    # raw SQL used for total amount per category
    sql = text("""
        SELECT c.name, SUM(e.amount)
        FROM categories c
        JOIN expenses e ON c.id = e.category_id
        GROUP BY c.name
    """)

    result = engine.execute(sql)

    print("Category wise spending")
    for row in result:
        print(row[0], ":", row[1])

# -------------------------------
# BUDGET
# -------------------------------

def set_budget():
    # sets monthly budget
    month = input("Month (YYYY-MM): ")
    limit = float(input("Limit: "))

    budget = Budget(month=month, limit=limit)
    session.add(budget)
    session.commit()
    print("Budget set")


def check_budget():
    # compares total spending with budget
    month = input("Month (YYYY-MM): ")
    budget = session.query(Budget).filter_by(month=month).first()

    expenses = session.query(Expense).all()
    total = sum(e.amount for e in expenses)

    if budget and total > budget.limit:
        print("Budget exceeded")
    else:
        print("Within budget")

# -------------------------------
# MENU
# -------------------------------

def menu():
    # main menu loop
    while True:
        print("""
1. Add Expense
2. Delete Expense
3. Search by Date
4. Category Report
5. Set Budget
6. Check Budget
7. Exit
""")

        choice = input("Choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            delete_expense()
        elif choice == "3":
            search_by_date()
        elif choice == "4":
            category_report()
        elif choice == "5":
            set_budget()
        elif choice == "6":
            check_budget()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

# program starts here
menu()
