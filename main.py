from src.file_handler import load_file
from src.data_validator import validate_schema, check_missing_values
from src.report_generator import generate_report


def main():
    # load the data
    df = load_file("data/large_sample.csv")

    # Validate the data
    schema = {
        "id": "int64",
        "name": "object",
        "age": "float64",
        "email": "object"}
    try:
        validate_schema(df, schema)
        print("Schema validation passed.")
    except ValueError as e:
        print(f"Schema validation failed: {e}")

    # Check for missing values
    missing_values = check_missing_values(df)

    # Generate a report
    data_summary = {
        "Missing Values": missing_values,
        "Total Rows": len(df),
        "Duplicates": df.duplicated().sum(),
    }
    generate_report(data_summary, "data/report.txt")


if __name__ == "__main__":
    main()
