````markdown
# 🧪 DFAlchemy

**The Alchemy of DataFrames — For Teachers, Students, and Developers.**  
A Python library to rapidly create, convert, and manipulate Pandas DataFrames with ease.

---

## 🚀 What is DFAlchemy?

`DFAlchemy` is a lightweight and powerful module that simplifies working with Pandas DataFrames. Whether you're a teacher trying to demonstrate a concept, or a developer quickly testing logic — DFAlchemy helps you create DataFrames magically from lists, dicts, JSONs, CSVs, or even fake data.

---

## 🎯 Key Features

### 📚 For Teachers
- `generate_students_dataframe(n=10)` – Creates realistic student records (names, marks, attendance).
- `generate_sales_dataframe(n=20)` – Sample sales data (product, price, quantity, revenue).
- `generate_dates_dataframe(n=15, freq='D')` – Create datetime-based DataFrames.
- `generate_null_dataframe()` – Showcase missing value handling.
- `generate_multiindex_example()` – Pre-made multi-indexed DataFrame for teaching.

### 👨‍💻 For Developers
- `to_dataframe(obj)` – One function to convert lists, dicts, CSVs, JSON, etc. to DataFrame.
- `load_csv(path)` – Safe wrapper around `pd.read_csv`.
- `load_json(path)` – Load JSON files into DataFrames easily.
- `preview(df, max_rows=5)` – Preview DataFrames in a clean, tabular CLI format.
- `save_df(df, path, format='csv')` – Save to CSV/JSON with one line.
- `compare_dfs(df1, df2)` – Diff two DataFrames for fast debugging.

### 🧙‍♂️ Magic Data Creation
- `fake_data(cols=['name', 'email', 'address'], n=10)` – Generate fully fake but realistic data using `Faker`.

### 🖼️ (Planned) Visual + Advanced Features
- `theme.set('dark')` – Pretty terminal output using themes.
- `from_api(url)` – Convert JSON API response to DataFrame.
- `from_sql(query, uri)` – Load directly from SQL databases (SQLite, MySQL, etc.)
- `plot_dataframe(df)` – (Optional) Plot sample visualizations using matplotlib/seaborn.

---

## 🔧 Installation

```bash
pip install dfalchemy
````

---

## 🧪 Example Usage

```python
from dfalchemy.generators import fake_data
from dfalchemy.converters import to_dataframe

# Generate 5 fake records with names and emails
df = fake_data(cols=['name', 'email'], n=5)
print(df)

# Convert a list of dicts to DataFrame
data = [{'name': 'Alice'}, {'name': 'Bob'}]
df2 = to_dataframe(data)
print(df2)
```

---

## 🧩 Project Structure

```
dfalchemy/
├── __init__.py
├── generators.py       # fake_data, generate_students_dataframe, etc.
├── converters.py       # list/dict/json → DataFrame
├── loaders.py          # CSV/JSON → DataFrame
├── utils.py            # preview, compare, save
```

---

## 🤝 Contributing

We welcome suggestions, pull requests, and feature ideas!

1. Fork the repo
2. Create a new branch
3. Add your changes
4. Submit a pull request

---

## 📜 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 💬 Credits

Made with ❤️ by **Bhavya Soni** a.k.a zGamingTechz
For teachers, students, devs, and data lovers.

---

```