import pandas as pd

def compare_and_print_excel(file1_path, file2_path, output_path):
    # Read the two Excel files
    df1 = pd.read_excel('excel1.xlsx')
    df2 = pd.read_excel('excel2.xlsx')

    # Find rows where any element is different between the two DataFrames
    differences = df1.ne(df2)
    different_rows = differences.any(axis=1)

    # Add a 'Status' column to indicate matching or not
    df1['Status'] = 'Matching'
    df1.loc[different_rows, 'Status'] = 'Not Matching'

    # Add a 'Reason' column for non-matching records
    df1['Reason'] = ''
    df1.loc[different_rows, 'Reason'] = differences[different_rows].apply(lambda row: ', '.join(row[row].index), axis=1)

    # Create a new Excel file with the result excluding the index column
    df1.to_excel(output_path, index=False)

    # If there are non-matching records, print the details
    if different_rows.any():
        print("Non-matching records:")
        print(df1[different_rows])

# Example usage
compare_and_print_excel('excel1.xlsx', 'excel2.xlsx', 'diff1.xlsx')
