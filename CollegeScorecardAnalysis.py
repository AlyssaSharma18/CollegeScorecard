import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load and preprocess data
data = pd.read_csv("C:/Users/alyss/Downloads/Most-Recent-Cohorts-Institution_10022024/Most-Recent-Cohorts-Institution.csv")

newdata = data.loc[:, ['INSTNM', 'CCBASIC', 'PCIP11', 'COSTT4_A', 'C150_4', 'GRAD_DEBT_MDN', 'MD_EARN_WNE_P10',
                       'ACTCM50', 'COMPL_RPY_5YR_RT', 'STUFACR', 'ICLEVEL']]
newdata = newdata.iloc[2255:2377]
newdata = newdata[newdata['ICLEVEL'] == 1]

newdata = newdata.rename(columns={
    'INSTNM': 'InstitutionName',
    'CCBASIC': 'CarnegieClass',
    'PCIP11': 'ComputerSciencePercentage',
    'COSTT4_A': 'AverageCost',
    'C150_4': 'CompletionRate',
    'GRAD_DEBT_MDN': 'MedianDebt',
    'MD_EARN_WNE_P10': 'MedianEarnings10Years',
    'ACTCM50': '50thPercentileACTAdmission',
    'COMPL_RPY_5YR_RT': 'Completer5yrRepayRate',
    'STUFACR': 'StudentFacultyRatio',
    'ICLEVEL': 'InstitutionLevel'
})

newdata = newdata[newdata['Completer5yrRepayRate'] != "PS"]
newdata['Completer5yrRepayRate'] = pd.to_numeric(newdata['Completer5yrRepayRate'], errors='coerce')
newdata.reset_index(drop=True, inplace=True)

# Sort data by 'MedianEarnings10Years' in descending order and select the top 7
top_7_data = newdata.sort_values(by='MedianEarnings10Years', ascending=False).head(7)

# Plot: Bar chart of top 7 institutions by Median Earnings 10 Years After Graduation
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='MedianEarnings10Years',
    data=top_7_data,
    palette='Blues_d'
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Top 7 Institutions by Median Earnings 10 Years After Graduation')
plt.xlabel('Institution Name')
plt.ylabel('Median Earnings 10 Years ($)')
plt.tight_layout()

# Show plot
plt.show()

plt.close()