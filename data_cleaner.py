# data_cleaner.py
# A simple Python automation script for cleaning up Excel/CSV data

import pandas as pd
import os


def clean_data(input_file, output_file):
    # Check if the input file exists
    if not os.path.exists(input_file):
        print(f"Error: '{input_file}' not found.")
        print(f"Current working directory: {os.getcwd()}")
        print("Make sure the file is in the same folder as this script or use a full path.")
        return

    # Read the file
    df = pd.read_csv(input_file)
    print("File loaded successfully!")

    # Clean spaces from text columns first
    df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)

    # Drop rows where all columns are NaN
    df.dropna(how="all", inplace=True)

    # Drop rows where all cells are empty strings
    df = df[~(df == '').all(axis=1)]

    # Make column names neat
    df.columns = [col.strip().title() for col in df.columns]

    # Save the cleaned data
    df.to_csv(output_file, index=False)
    print(f"\nCleaned file saved as: {output_file}")

    # Show summary of cleanup
    print(f"\nTotal rows after cleaning: {len(df)}")


# Example usage
if __name__ == "__main__":
    clean_data("uncleaned_data.csv", "cleaned_data.csv")
