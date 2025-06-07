import pandas as pd
from faker import Faker
import random

faker = Faker()

def generate_students_dataframe(count=10):
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