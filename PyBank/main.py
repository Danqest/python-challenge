#import the OS library and install dependencies if not already available
import os
package = "pandas"
try:
    __import__package
except:
    os.system("pip install "+ package)

# import the pandas library
import pandas as pd

# define the PATH variable for data to be used and read the csv dataset
PATH = 'C:/Users/Danqest/Desktop/CODING/GT-VIRT-DATA-PT-01-2023-U-LOLC/03 - Python Unit/python-challenge/PyBank/Resources/budget_data.csv'
budget_data = pd.read_csv(PATH)

# define a variable with the length of the dataframe
date_col_len = len(budget_data['Date'])

# define a variable for the sum of Profits/Losses column
total_pnl = sum(budget_data['Profit/Losses'])

# define a new column in the dataframe which displays the monthly difference between Profits/Losses
budget_data['PnL Delta'] = budget_data['Profit/Losses'].diff()

# define a variable for the average change in Profits/Losses
pnl_delta = round(budget_data['PnL Delta'].sum() / (len(budget_data)-1), 2)

# define variables to hold the max pnl_delta figure and date
max_row_date = budget_data['Date'].loc[budget_data['PnL Delta'] == budget_data['PnL Delta'].max()].item()
max_row_value = budget_data['PnL Delta'].loc[budget_data['PnL Delta'] == budget_data['PnL Delta'].max()].item()

# define variables to hold the min pnl_delta figure and date
min_row_date = budget_data['Date'].loc[budget_data['PnL Delta'] == budget_data['PnL Delta'].min()].item()
min_row_value = budget_data['PnL Delta'].loc[budget_data['PnL Delta'] == budget_data['PnL Delta'].min()].item()

# return the variables to the terminal
print('Financial Analysis')
print('----------------------------')
print(f'Total Months: {date_col_len}')
print(f'Total: ${total_pnl}')
print(f'Average Change: ${pnl_delta}')
print(f'Greatest Incease in Profits: {max_row_date} (${max_row_value})')
print(f'Greatest Decrease in Profits: {min_row_date} (${min_row_value})')

# return the variables to a text file
with open("./analysis/analysis.txt", "w") as f:
    print('Financial Analysis', file=f)
    print('----------------------------', file=f)
    print(f'Total Months: {date_col_len}', file=f)
    print(f'Total: ${total_pnl}', file=f)
    print(f'Average Change: ${pnl_delta}', file=f)
    print(f'Greatest Incease in Profits: {max_row_date} (${max_row_value})', file=f)
    print(f'Greatest Decrease in Profits: {min_row_date} (${min_row_value})', file=f)