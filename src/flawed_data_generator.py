import pandas as pd
import json
import os
import random
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

# Create directories for data if not exist
os.makedirs("data", exist_ok=True)


def generate_flawed_csv(file_path, num_rows=100):
    """
    Generate a flawed CSV file with intentional issues.

    Flaws:
    - Missing values in random rows.
    - Duplicated rows.
    - Invalid data types in numeric fields.
    - Column name mismatch.

    Args:
        file_path (str): Path to save the CSV file.
        num_rows (int): Number of rows to generate.
    """
    data = {
        "ID": range(1, num_rows + 1),
        "Name": [fake.name() for _ in range(num_rows)],
        "Age": [
            random.choice(range(18, 80))
            if random.random() > 0.2  # 20% missing
            else None
            for _ in range(num_rows)
        ],
        "Email": [fake.email() for _ in range(num_rows)],
    }

    # Convert to DataFrame
    df = pd.DataFrame(data)

    # Introduce duplicate rows
    duplicate_idx = random.sample(range(num_rows), k=num_rows // 10)  # 10%
    df = pd.concat([df, df.iloc[duplicate_idx]])

    # Add invalid data to numeric column
    invalid_indices = random.sample(range(len(df)), k=len(df) // 10)  # 10%
    for idx in invalid_indices:
        df.loc[idx, "Age"] = fake.word()

    # Rename a column for schema mismatch
    df.rename(columns={"Email": "Contact"}, inplace=True)

    df.to_csv(file_path, index=False)
    print(f"Flawed CSV generated at {file_path}")


def generate_flawed_json(file_path, num_rows=100):
    """
    Generate a flawed JSON file with intentional issues.

    Flaws:
    - Missing keys in some records.
    - Invalid data types.
    - Duplicate records.

    Args:
        file_path (str): Path to save the JSON file.
        num_rows (int): Number of records to generate.
    """
    data = []
    for i in range(1, num_rows + 1):
        record = {
            "id": i,
            "name": fake.name(),
            "age": (
                random.choice(range(18, 80))
                if random.random() > 0.2
                else None
            ),
            "email": fake.email(),
        }

        # Randomly remove a key
        if random.random() < 0.1:  # 10% missing keys
            record.pop(random.choice(list(record.keys())))

        # Introduce invalid data types
        if random.random() < 0.1:  # 10% invalid types
            record["age"] = fake.word()

        data.append(record)

    # Introduce duplicate records
    data.extend(random.sample(data, k=num_rows // 10))  # 10% duplicates

    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(f"Flawed JSON generated at {file_path}")


def generate_flawed_txt(file_path, num_rows=100):
    """
    Generate a flawed TXT file with intentional issues.

    Flaws:
    - Rows with extra/missing fields.
    - Rows with invalid values.
    - Duplicated rows.

    Args:
        file_path (str): Path to save the TXT file.
        num_rows (int): Number of rows to generate.
    """
    rows = ["ID\tName\tAge\tEmail"]  # Header row

    for i in range(1, num_rows + 1):
        name = fake.name()
        age = (
            random.choice(range(18, 80))
            if random.random() > 0.2
            else "N/A"
        )
        email = fake.email()

        # Introduce missing or extra fields
        if random.random() < 0.1:  # 10% missing fields
            row = f"{i}\t{name}\t{age}"
        elif random.random() < 0.1:  # 10% extra fields
            extra_field = fake.word()
            row = f"{i}\t{name}\t{age}\t{email}\t{extra_field}"
        else:
            row = f"{i}\t{name}\t{age}\t{email}"

        rows.append(row)

    # Add duplicate rows
    duplicates = random.sample(rows[1:], k=num_rows // 10)  # Exclude header
    rows.extend(duplicates)

    with open(file_path, "w") as f:
        f.write("\n".join(rows))
    print(f"Flawed TXT generated at {file_path}")


if __name__ == "__main__":
    # Generate flawed datasets
    generate_flawed_csv("data/flawed_sample.csv", 100)
    generate_flawed_json("data/flawed_sample.json", 100)
    generate_flawed_txt("data/flawed_sample.txt", 100)
