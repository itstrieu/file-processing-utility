import pandas as pd
import json
import os
import random
from faker import Faker

# Initialize Faker for generating realistic data
fake = Faker()

# Create directories for data if not exist
os.makedirs("data", exist_ok=True)


# Generate Large Sample CSV
def generate_large_sample_csv(file_path, num_rows=10000):
    """
    Generate a large CSV file with random sample data.

    Args:
        file_path (str): Path to save the CSV file.
        num_rows (int): Number of rows to generate.
    """
    data = {
        "id": range(1, num_rows + 1),
        "name": [fake.name() for _ in range(num_rows)],
        "age": [
            random.choice(range(18, 80))
            if random.random() > 0.1
            else None
            for _ in range(num_rows)
        ],
        "email": [fake.email() for _ in range(num_rows)],
    }
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
    print(f"Large sample CSV with {num_rows} rows generated at {file_path}")


# Generate Large Sample JSON
def generate_large_sample_json(file_path, num_rows=10000):
    """
    Generate a large JSON file with random sample data.

    Args:
        file_path (str): Path to save the JSON file.
        num_rows (int): Number of entries to generate.
    """
    data = [
        {
            "id": i,
            "name": fake.name(),
            "age": (
                random.choice(range(18, 80))
                if random.random() > 0.1
                else None
            ),
            "email": fake.email(),
        }
        for i in range(1, num_rows + 1)
    ]
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)
    print(
        f"Large sample JSON with {num_rows} entries generated at {file_path}"
    )


# Generate Large Sample TXT
def generate_large_sample_txt(file_path, num_rows=10000):
    """
    Generate a large TXT file with tab-separated sample data.

    Args:
        file_path (str): Path to save the TXT file.
        num_rows (int): Number of rows to generate.
    """
    with open(file_path, "w") as f:
        f.write("ID\tName\tAge\tEmail\n")  # Header row
        for i in range(1, num_rows + 1):
            name = fake.name()
            age = (
                random.choice(range(18, 80))
                if random.random() > 0.1
                else "N/A"
            )
            email = fake.email()
            f.write(f"{i}\t{name}\t{age}\t{email}\n")
    print(f"Large sample TXT with {num_rows} rows generated at {file_path}")


# Generate all sample data
if __name__ == "__main__":
    num_rows = 10000  # Adjust size as needed
    generate_large_sample_csv(
        os.path.join("data", "large_sample.csv"),
        num_rows
        )
    generate_large_sample_json(
        os.path.join("data", "large_sample.json"),
        num_rows
        )
    generate_large_sample_txt(
        os.path.join("data", "large_sample.txt"),
        num_rows
        )
