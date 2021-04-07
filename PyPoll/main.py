#os module allow to ceate a file paths across operating systems
import os
#Module for reading  csv files
import csv

election_datacsv = os.path.join('..', 'Resources', 'election_data.csv')
with open(election_datacsv) as csvfile:
    csv_reader = csv_reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    
