import pandas as pd

# Replace 'your_file.xlsx' with the path to your Excel file
data = pd.read_csv("C:/Users/alyss/Downloads/Most-Recent-Cohorts-Institution_10022024/Most-Recent-Cohorts-Institution.csv")  # Default sheet_name is the first sheet

#print(data.head)

#print(data.loc[0:5, ['CCBASIC', 'PCIP11', 'COSTT4_A', 'C150_4', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10']])

newdata = data.loc[:, ['INSTNM', 'CCBASIC', 'PCIP11', 'COSTT4_A', 'C150_4', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10']]




newdata = newdata.rename(columns={
    'INSTNM': 'InstitutionName',
    'CCBASIC': 'CarnegieClass',
    'PCIP11': 'ComputerSciencePercentage',
    'COSTT4_A': 'AverageCost',
    'C150_4': 'CompletionRate',
    'GRAD_DEBT_MDN': 'MedianDebt',
    'MD_EARN_WNE_P10': 'MedianEarnings10Years'
})

print(newdata.head())

# Set display options to show all rows and columns
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Adjust display width to fit columns
pd.set_option('display.max_colwidth', None)  # Show full column width


print(newdata.describe(include='all'))

# Reset display options to defaults
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')
pd.reset_option('display.width')
pd.reset_option('display.max_colwidth')
