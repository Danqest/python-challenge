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
PATH = 'C:/Users/Danqest/Desktop/CODING/GT-VIRT-DATA-PT-01-2023-U-LOLC/03 - Python Unit/python-challenge/PyPoll/Resources/election_data.csv'
election_data = pd.read_csv(PATH)

# define a variable with the length of the dataframe
ballot_col_len = len(election_data['Ballot ID'])

# count votes for each candidate, calculate percentage of total votes, and save as variables
CCS_cnt = election_data['Candidate'].loc[election_data['Candidate'] == 'Charles Casper Stockham'].count()
CCS_pct = round((CCS_cnt / ballot_col_len)*100, 3)

DDG_cnt = election_data['Candidate'].loc[election_data['Candidate'] == 'Diana DeGette'].count()
DDG_pct = round((DDG_cnt / ballot_col_len)*100,3)

RAD_cnt = election_data['Candidate'].loc[election_data['Candidate'] == 'Raymon Anthony Doane'].count()
RAD_pct = round((RAD_cnt / ballot_col_len)*100,3)

# store top vote winner as variable
vote_winner = election_data['Candidate'].describe()
vote_winner = vote_winner['top']

# return the variables to the terminal
print('Election Results')
print('----------------------------')
print(f'Total Votes: {ballot_col_len}')
print('----------------------------')
print(f'Charles Casper Stockham: {CCS_pct}% ({CCS_cnt})')
print(f'Diana DeGette: {DDG_pct}% ({DDG_cnt})')
print(f'Raymond Anthony Doane: {RAD_pct}% ({RAD_cnt})')
print('----------------------------')
print(f'Winner: {vote_winner}')
print('----------------------------')

# return the variables to a text file
with open("./analysis/analysis.txt", "w") as f:
    print('Election Results', file=f)
    print('----------------------------', file=f)
    print(f'Total Votes: {ballot_col_len}', file=f)
    print('----------------------------', file=f)
    print(f'Charles Casper Stockham: {CCS_pct} ({CCS_cnt})', file=f)
    print(f'Diana DeGette: {DDG_pct} ({DDG_cnt})', file=f)
    print(f'Raymon Anthony Doane: {RAD_pct} ({RAD_cnt})', file=f)
    print('----------------------------', file=f)
    print(f'Winner: {vote_winner}', file=f)
    print('----------------------------', file=f)