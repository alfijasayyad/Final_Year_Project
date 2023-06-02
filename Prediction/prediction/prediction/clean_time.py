import pandas as pd

# Load the Excel sheet
df = pd.read_excel('Survey.xlsx', engine='openpyxl')

# Define a function to clean up the values
def clean_time(time_str):
    if isinstance(time_str, str):
        if '-' in time_str:
            time_vals = time_str.split('-')
            time = (int(time_vals[0]) + int(time_vals[1])) / 2.0
        else:
            time = int(time_str.split(' ')[0])
        return time
    else:
        return time_str

# Apply the clean_time function to the relevant columns
df['The time you spend in playing games?'] = df['The time you spend in playing games?'].apply(clean_time)
df['The time you spend in listening music?'] = df['The time you spend in listening music?'].apply(clean_time)
df['The time you spend in social media?'] = df['The time you spend in social media?'].apply(clean_time)
df['The time you spend in doing work?'] = df['The time you spend in doing work?'].apply(clean_time)

# Save the cleaned up data back to the Excel sheet
df.to_excel('my_sheet_cleaned.xlsx', index=False)
