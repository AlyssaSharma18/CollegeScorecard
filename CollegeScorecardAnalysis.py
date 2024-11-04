import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
data = pd.read_csv("C:/Users/alyss/Downloads/Most-Recent-Cohorts-Institution_10022024/Most-Recent-Cohorts-Institution.csv")  # Default sheet_name is the first sheet

#print(data.head)

#print(data.loc[0:5, ['CCBASIC', 'PCIP11', 'COSTT4_A', 'C150_4', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10']])

newdata = data.loc[:, ['INSTNM', 'CCBASIC', 'PCIP11', 'COSTT4_A', 'C150_4', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10',
                       'ACTCM50', 'COMPL_RPY_5YR_RT']]

newdata = newdata.iloc[2255:2377]



newdata = newdata.rename(columns={
    'INSTNM': 'InstitutionName',
    'CCBASIC': 'CarnegieClass',
    'PCIP11': 'ComputerSciencePercentage',
    'COSTT4_A': 'AverageCost',
    'C150_4': 'CompletionRate',
    'DEBT_MDN': 'MedianDebt',
    'MD_EARN_WNE_P10': 'MedianEarnings10Years',
    'ACTCM50': '50thPercentileACTAdmission',
    'COMPL_RPY_5YR_RT': 'Completer5yrRepayRate'
})

# Remove rows where 'Completers5yrRepayRate' is equal to "PS"
newdata = newdata[newdata['Completer5yrRepayRate'] != "PS"]

# Convert the column to numeric, coercing errors to NaN
newdata['Completer5yrRepayRate'] = pd.to_numeric(newdata['Completer5yrRepayRate'], errors='coerce')


# Optionally, reset the index after filtering
newdata.reset_index(drop=True, inplace=True)

# Print the updated DataFrame
print(newdata.head())






# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Adjust display width to fit columns
pd.set_option('display.max_colwidth', None)  # Show full column width


print(newdata.describe(include='all'))



# Step 1: Find the maximum value in the 'MedianEarnings10Years' column
max_median_earnings = newdata['MedianEarnings10Years'].max()

# Step 2: Filter the DataFrame to get the row(s) with the maximum median earnings
max_earnings_row = newdata[newdata['MedianEarnings10Years'] == max_median_earnings]

# Print the row(s)
print(max_earnings_row)

# Step 1: Find the minimum value in the 'AverageCost' column
min_average_cost = newdata['AverageCost'].min()

# Step 2: Filter the DataFrame to get the row(s) with the minimum average cost
lowest_cost_row = newdata[newdata['AverageCost'] == min_average_cost]

# Print the row(s)
print(lowest_cost_row)




# Step 1: Find the maximum value in the comp sci percent column
max_cs_percent = newdata['ComputerSciencePercentage'].max()

# Step 2: Filter the DataFrame to get the row(s) with the maximum median earnings
max_cs_percent_row = newdata[newdata['ComputerSciencePercentage'] == max_cs_percent]

# Print the row(s)
print(max_cs_percent_row)


# Step 1: Find the maximum value in the 'MedianEarnings10Years' column
max_50act = newdata['50thPercentileACTAdmission'].max()

# Step 2: Filter the DataFrame to get the row(s) with the maximum median earnings
max_50act_row = newdata[newdata['50thPercentileACTAdmission'] == max_50act]

# Print the row(s)
print(max_50act_row)


# Step 1: Find the maximum value in the 'MedianEarnings10Years' column
max_Completer5yrRepayRate = newdata['Completer5yrRepayRate'].max()

# Step 2: Filter the DataFrame to get the row(s) with the maximum median earnings
max_Completer5yrRepayRate_row = newdata[newdata['Completer5yrRepayRate'] == max_Completer5yrRepayRate]

# Print the row(s)
print(max_Completer5yrRepayRate_row)



# Reset display options to defaults
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
pd.reset_option('display.width')
pd.reset_option('display.max_colwidth')
