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

#Here we take out faulty values (PS) from the completer 5 year repay rate row
newdata = newdata[newdata['Completer5yrRepayRate'] != "PS"]
newdata['Completer5yrRepayRate'] = pd.to_numeric(newdata['Completer5yrRepayRate'], errors='coerce')
newdata.reset_index(drop=True, inplace=True)

# Analysis steps

# Max median earnings after 10 years was Duke
max_median_earnings = newdata['MedianEarnings10Years'].max()
max_earnings_row = newdata[newdata['MedianEarnings10Years'] == max_median_earnings]
print(max_earnings_row)

# Min avg cost was Elizabeth City State University
min_average_cost = newdata['AverageCost'].min()
lowest_cost_row = newdata[newdata['AverageCost'] == min_average_cost]
print(lowest_cost_row)

# maximum CS percentage was Montreat College
max_cs_percent = newdata['ComputerSciencePercentage'].max()
max_cs_percent_row = newdata[newdata['ComputerSciencePercentage'] == max_cs_percent]
print(max_cs_percent_row)


# Highest 50th percentile ACT admission was Duke
max_50act = newdata['50thPercentileACTAdmission'].max()
max_50act_row = newdata[newdata['50thPercentileACTAdmission'] == max_50act]
print(max_50act_row)

# Max 5 year repay rate we Elon
max_Completer5yrRepayRate = newdata['Completer5yrRepayRate'].max()
max_Completer5yrRepayRate_row = newdata[newdata['Completer5yrRepayRate'] == max_Completer5yrRepayRate]
print(max_Completer5yrRepayRate_row)


#Lowest Student Faculty Ratio shared with Duke, Bennett, and UNC School of Arts
minStudFacR = newdata['StudentFacultyRatio'].min()
minStudFacR_row = newdata[newdata['StudentFacultyRatio'] == minStudFacR]
print(minStudFacR_row)

#Duke is number 2 5 year completion
# Step 1: Get the top 7 rows with the highest 5-year completion rate
top_7_completion_rate = newdata.nlargest(7, 'Completer5yrRepayRate')

# Print the top 7 rows
print(top_7_completion_rate)


#Start The Plots


# Plot: Bar chart of Median Earnings 10 Years After Graduation by Institution
# Step 1: Sort data by 'MedianEarnings10Years' in descending order
sorted_data = newdata.sort_values(by='MedianEarnings10Years', ascending=False)

# Step 2: Plot the data
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='MedianEarnings10Years',
    data=sorted_data,
    palette='Blues_d'
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Median Earnings 10 Years After Graduation by Institution')
plt.xlabel('Institution Name')
plt.ylabel('Median Earnings 10 Years ($)')
plt.tight_layout()

# Show plot
plt.show()



# Filter for the top 7 institutions by 'MedianEarnings10Years'
top_7_data = newdata.nlargest(7, 'MedianEarnings10Years')

# Plotting the top 7 institutions by median earnings 10 years after graduation
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='MedianEarnings10Years',
    data=top_7_data,
    palette='Blues_d',
    hue=None  # Resolve future warning by setting hue to None
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Top 7 Institutions by Median Earnings 10 Years After Graduation')
plt.xlabel('Institution Name')
plt.ylabel('Median Earnings 10 Years ($)')
plt.tight_layout()

# Show and close plot
plt.show()


# Filter for the 7 institutions with the lowest student-to-faculty ratio
lowest_7_data = newdata.nsmallest(7, 'StudentFacultyRatio')

# Plotting the 7 institutions with the lowest student-to-faculty ratio
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='StudentFacultyRatio',
    data=lowest_7_data,
    palette='Greens_d'
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Top 7 Institutions with the Lowest Student-to-Faculty Ratio')
plt.xlabel('Institution Name')
plt.ylabel('Student-to-Faculty Ratio')
plt.tight_layout()

# Show and close plot
plt.show()



# Filter for the top 7 institutions with the highest ACT Admission score
top_7_act_data = newdata.nlargest(7, '50thPercentileACTAdmission')

# Plotting the top 7 institutions with the highest ACT Admission score
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='50thPercentileACTAdmission',
    data=top_7_act_data,
    palette='Reds_d'
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Top 7 Institutions by 50th Percentile ACT Admission Score')
plt.xlabel('Institution Name')
plt.ylabel('50th Percentile ACT Score')
plt.tight_layout()

# Show and close plot
plt.show()



# Step 2: Create the bar chart
plt.figure(figsize=(12, 8))
sns.barplot(
    x='InstitutionName',
    y='Completer5yrRepayRate',
    data=top_7_completion_rate,
    palette='Purples_d'  # Purple color scheme
)

# Customize the chart
plt.xticks(rotation=90)
plt.title('Top 7 Institutions by 5-Year Completion Rate')
plt.xlabel('Institution Name')
plt.ylabel('5-Year Completion Rate')
plt.tight_layout()

# Show the chart
plt.show()


plt.close()
