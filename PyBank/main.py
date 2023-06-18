#import the OS & csv library
import os
import csv

# define the PATH variable for data to be used and read the csv dataset
PATH = os.path.join('Resources', 'budget_data.csv')

# read the csv
with open(PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    
    # initialize variables
    count_len = 0
    total_pnl = 0
    date_vector = []
    pnl_vector = []
    pnl_diff = []
    avg_pnl = 0
    
    # iterate through csv
    for row in csvreader:
        count_len += 1
        
        total_pnl += int(row[1])
        
        date_vector.append(row[0])
        pnl_vector.append(int(row[1]))

    # calculate PnL differences
    for i in range(1, len(pnl_vector)):
        pnl_diff.append(pnl_vector[i] - pnl_vector[i-1])
    
    # insert 0 into list position 0
    pnl_diff.insert(0, 0)

    # calculate average pnl, max, min, and list positions
    avg_pnl = round(sum(pnl_diff) / (count_len - 1), 2)
    
    max_pnl = max(pnl_diff)
    min_pnl = min(pnl_diff)
    
    list_pos_max = pnl_diff.index(max_pnl)
    list_pos_min = pnl_diff.index(min_pnl)

    # return the variables to the terminal
    print('Financial Analysis')
    print('----------------------------')
    print(f'Total Months: {count_len}')
    print(f'Total: ${total_pnl}')
    print(f'Average Change: ${avg_pnl}')
    print(f'Greatest Incease in Profits: {date_vector[list_pos_max]} (${max_pnl})')
    print(f'Greatest Decrease in Profits: {date_vector[list_pos_min]} (${min_pnl})')

    # return the variables to a text file
    with open("./analysis/analysis.txt", "w") as f:
        print('Financial Analysis', file=f)
        print('----------------------------', file=f)
        print(f'Total Months: {count_len}', file=f)
        print(f'Total: ${total_pnl}', file=f)
        print(f'Average Change: ${avg_pnl}', file=f)
        print(f'Greatest Incease in Profits: {date_vector[list_pos_max]} (${max_pnl})', file=f)
        print(f'Greatest Decrease in Profits: {date_vector[list_pos_min]} (${min_pnl})', file=f)