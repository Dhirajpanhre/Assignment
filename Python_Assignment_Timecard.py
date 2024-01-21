import pandas as pd
from datetime import datetime, timedelta

def consecutive_7days_work(df):
    print("\n \n")
    for i in range(len(df) - 1):
        current_name, current_position, current_start, current_end = (
            df.at[i, 'Employee Name'],
            df.at[i, 'Position ID'],
            df.at[i, 'Time'],
            df.at[i, 'Time Out']
        )
        next_name, next_position, next_start, next_end = (
            df.at[i + 1, 'Employee Name'],
            df.at[i + 1, 'Position ID'],
            df.at[i + 1, 'Time'],
            df.at[i + 1, 'Time Out']
        )

        # Check for NaT values before converting to datetime
        if pd.notna(current_start) and pd.notna(current_end) and pd.notna(next_start) and pd.notna(next_end):
            # Convert time columns to datetime objects
            current_start, current_end, next_start, next_end = (
                datetime.strptime(str(current_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(current_end), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_end), '%Y-%m-%d %H:%M:%S')
            )

            # a) Check for 7 consecutive days of work

            if (next_start - current_end).days == 1:
                print(f"{current_name} ({current_position}) worked for 7 consecutive days.")


def work_less_than_10(df):
    print("\n \n")
    for i in range(len(df) - 1):
        current_name, current_position, current_start, current_end = (
            df.at[i, 'Employee Name'],
            df.at[i, 'Position ID'],
            df.at[i, 'Time'],
            df.at[i, 'Time Out']
        )
        next_name, next_position, next_start, next_end = (
            df.at[i + 1, 'Employee Name'],
            df.at[i + 1, 'Position ID'],
            df.at[i + 1, 'Time'],
            df.at[i + 1, 'Time Out']
        )

        # Check for NaT values before converting to datetime
        if pd.notna(current_start) and pd.notna(current_end) and pd.notna(next_start) and pd.notna(next_end):
            # Convert time columns to datetime objects
            current_start, current_end, next_start, next_end = (
                datetime.strptime(str(current_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(current_end), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_end), '%Y-%m-%d %H:%M:%S')
            )

            # b) Check for less than 10 hours between shifts but greater than 1 hour
            if 1 < (next_start - current_end).total_seconds() // 3600 < 10:
                print(f"{current_name} ({current_position}) has less than 10 hours between shifts but greater than 1 hour.")

 
def work_more_than_14(df):
    print("\n \n")
    for i in range(len(df) - 1):
        current_name, current_position, current_start, current_end = (
            df.at[i, 'Employee Name'],
            df.at[i, 'Position ID'],
            df.at[i, 'Time'],
            df.at[i, 'Time Out']
        )
        next_name, next_position, next_start, next_end = (
            df.at[i + 1, 'Employee Name'],
            df.at[i + 1, 'Position ID'],
            df.at[i + 1, 'Time'],
            df.at[i + 1, 'Time Out']
        )

        # Check for NaT values before converting to datetime
        if pd.notna(current_start) and pd.notna(current_end) and pd.notna(next_start) and pd.notna(next_end):
            # Convert time columns to datetime objects
            current_start, current_end, next_start, next_end = (
                datetime.strptime(str(current_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(current_end), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_end), '%Y-%m-%d %H:%M:%S')
            )

            # c) Check for more than 14 hours in a single shift
            if (current_end - current_start).total_seconds() // 3600 > 14:
                print(f"{current_name} ({current_position}) worked for more than 14 hours in a single shift.")


def analyze_excel(file_path):
    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)
    print("\n \n")
 
    # Check for 7 consecutive days of work
    consecutive_7days_work(df)

    # Check for less than 10 hours between shifts but greater than 1 hour
    work_less_than_10(df)

    # Check for more than 14 hours in a single shift
    work_more_than_14(df)

    """for i in range(len(df) - 1):
        current_name, current_position, current_start, current_end = (
            df.at[i, 'Employee Name'],
            df.at[i, 'Position ID'],
            df.at[i, 'Time'],
            df.at[i, 'Time Out']
        )
        next_name, next_position, next_start, next_end = (
            df.at[i + 1, 'Employee Name'],
            df.at[i + 1, 'Position ID'],
            df.at[i + 1, 'Time'],
            df.at[i + 1, 'Time Out']
        )

        # Check for NaT values before converting to datetime
        if pd.notna(current_start) and pd.notna(current_end) and pd.notna(next_start) and pd.notna(next_end):
            # Convert time columns to datetime objects
            current_start, current_end, next_start, next_end = (
                datetime.strptime(str(current_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(current_end), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_start), '%Y-%m-%d %H:%M:%S'),
                datetime.strptime(str(next_end), '%Y-%m-%d %H:%M:%S')
            )

            # a) Check for 7 consecutive days of work

            if (next_start - current_end).days == 1:
                print(f"{current_name} ({current_position}) worked for 7 consecutive days.\n")

            # b) Check for less than 10 hours between shifts but greater than 1 hour
            if 1 < (next_start - current_end).total_seconds() // 3600 < 10:
                print(f"{current_name} ({current_position}) has less than 10 hours between shifts but greater than 1 hour.\n")

            # c) Check for more than 14 hours in a single shift
            if (current_end - current_start).total_seconds() // 3600 > 14:
                print(f"{current_name} ({current_position}) worked for more than 14 hours in a single shift.\n") """

if __name__ == "__main__":
    #file_path = input("Enter the Excel file path: ")
    file_path = "Assignment_Timecard.xlsx"
    analyze_excel(file_path)
