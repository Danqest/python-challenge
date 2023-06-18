#import the OS & csv library
import os
import csv

# define the PATH variable for data to be used and read the csv dataset
PATH = os.path.join('Resources', 'election_data.csv')
# read the csv
with open(PATH) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    # define varables to count
    ballot_count_len = 0
    count_stockham = 0
    count_degette = 0
    count_doane = 0

    # iterate through the csv and count total ballots and ballots per candidate
    for row in csvreader:
        ballot_count_len += 1
        
        if row[2] == 'Charles Casper Stockham':
            count_stockham += 1
        elif row[2] == 'Diana DeGette':
            count_degette += 1
        elif row[2] == 'Raymon Anthony Doane':
            count_doane += 1

    # calculate percentage of total votes per candidate
    CCS_pct = round((count_stockham / ballot_count_len)*100,3)
    DDG_pct = round((count_degette / ballot_count_len)*100,3)
    RAD_pct = round((count_doane / ballot_count_len)*100,3)

    # basic logic to verify winner
    winner = max(count_stockham, count_degette, count_doane)
    winner_name = ''
    
    if winner == count_stockham:
        winner_name = 'Charles Casper Stockham'
    elif winner == count_degette:
        winner_name = 'Diana DeGette'
    else: 
        winner_name = 'Raymon Anthony Doane'

    # return the variables to the terminal
    print('Election Results')
    print('----------------------------')
    print(f'Total Votes: {ballot_count_len}')
    print('----------------------------')
    print(f'Charles Casper Stockham: {CCS_pct}% ({count_stockham})')
    print(f'Diana DeGette: {DDG_pct}% ({count_degette})')
    print(f'Raymond Anthony Doane: {RAD_pct}% ({count_doane})')
    print('----------------------------')
    print(f'Winner: {winner_name}')
    print('----------------------------')

    # return the variables to a text file
    with open("./analysis/analysis.txt", "w") as f:
        print('Election Results', file=f)
        print('----------------------------', file=f)
        print(f'Total Votes: {ballot_count_len}', file=f)
        print('----------------------------', file=f)
        print(f'Charles Casper Stockham: {CCS_pct}% ({count_stockham})', file=f)
        print(f'Diana DeGette: {DDG_pct}% ({count_degette})', file=f)
        print(f'Raymon Anthony Doane: {RAD_pct}% ({count_doane})', file=f)
        print('----------------------------', file=f)
        print(f'Winner: {winner_name}', file=f)
        print('----------------------------', file=f)