import pandas as pd
from faker import Faker
import random

faker = Faker()


def generate_students_dataframe(count):
    if not count:
        raise Exception("Please provide the number of rows")

    data = []

    for _ in range(count):
        student = {
            'Name': faker.name(),
            'Email': faker.email(),
            'Age': random.randint(17, 25),
            'Grade': random.choice(['A', 'B', 'C', 'D', 'E']),
            'Attendance (%)': round(random.uniform(60, 100), 2)
        }
        data.append(student)

    return pd.DataFrame(data)


def generate_employees_dataframe(count):
    if not count:
        raise Exception("Please provide the number of rows")

    data = []

    for _ in range(count):
        employee = {
            'Name': faker.name(),
            'Email': faker.email(),
            'Age': random.randint(17, 25),
            'Department': random.choice(['HR', 'Customer', 'IT', 'Product', 'Sales']),
            'Salary': round(random.randint(1000, 10000))
        }
        data.append(employee)

    return pd.DataFrame(data)


def generate_fruits_dataframe(n=10):
    fruit_names = ['Apple', 'Banana', 'Orange', 'Mango', 'Grapes', 'Pineapple', 'Kiwi', 'Strawberry']
    states = ['Fresh', 'Rotten', 'Ripe', 'Unripe', 'Bruised']

    data = [{
        'Fruit Name': random.choice(fruit_names),
        'Price (INR)': round(random.uniform(10, 300), 2),
        'State': random.choice(states),
        'Stock': random.randint(0, 500)
    } for _ in range(n)]

    return pd.DataFrame(data)


def generate_marks_dataframe(n=10):
    sections = ['A', 'B', 'C']
    data = []

    for _ in range(n):
        maths = random.randint(0, 100)
        science = random.randint(0, 100)
        english = random.randint(0, 100)
        pe = random.randint(0, 100)
        avg = round((maths + science + english + pe) / 4, 2)

        student = {
            'Student Name': faker.name(),
            'Class': random.randint(9, 12),
            'Section': random.choice(sections),
            'Maths': maths,
            'Science': science,
            'English': english,
            'PE': pe,
            'Average': avg
        }
        data.append(student)

    return pd.DataFrame(data)


def generate_business_dataframe(n=10):
    current_year = 2025
    data = []

    for i in range(n):
        year = current_year - i
        sales = random.randint(50000, 5000000)
        purchases = random.randint(10000, 400000)
        expenses  = random.randint(100000, 4000000)
        profits = sales - purchases - expenses
        losses = max(0, random.randint(0, purchases // 4) if profits < 100000 else 0)
        stock_price = round(random.uniform(100, 1000), 2)

        record = {
            'Year': year,
            'Profits': profits,
            'Losses': losses,
            'Sales': sales,
            'Purchases': purchases,
            'Expenses': expenses,
            'Products Launched': random.randint(0, 20),
            'Stock Price': stock_price
        }
        data.append(record)

    return pd.DataFrame(data[::-1])  # Optional: Oldest year first
