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
