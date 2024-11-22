def validate_schema(df, schema):
    """
    Validate a DataFrame against a predefined schema.

    Args:
        df (pd.DataFrame): DataFrame to validate.
        schema (dict): Dictionary defining the expected schema. 
                       E.g., {
                           "id": "int",
                           "name": "str",
                           "age": "float",
                           "email": "str"}

    Returns:
        bool: True if validation passes, raises ValueError otherwise.
    """
    for column, dtype in schema.items():
        if column not in df.columns:
            raise ValueError(f"Missing column: {column}")
        if df[column].dtypes.name != dtype:
            raise ValueError(
                f"Column {column} has incorrect type."
                f"Expected {dtype}, got {df[column].dtypes.name}."
                )
    return True


def check_missing_values(df):
    """
    Check for missing values in a DataFrame.

    Args:
        df (pd.DataFrame): DataFrame to validate.

    Returns:
        dict: Summary of missing values.
    """
    missing_values = df.isnull().sum().to_dict()
    return missing_values
