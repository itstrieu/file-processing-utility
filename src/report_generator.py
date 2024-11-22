def generate_report(data_summary, output_file="report.txt"):
    """
    Write a summary report to a text file.

    Args:
        data_summary (dict): Dictionary containing summary metrics.
        output_file (str): Path to save the report.
    """
    with open(output_file, "w") as f:
        for key, value in data_summary.items():
            f.write(f"{key}: {value}\n")
    print(f"Report saved to {output_file}")
