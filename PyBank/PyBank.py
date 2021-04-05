#os module allow to ceate a file paths across operating systems
import os
#Module for reading  csv files
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')


#Create variable for each records to calculate the requested totals
total_months =0
total_net_profit_losses = 0
average_change = 0     #average_change= total net profit losses / total months
greatest_increase = 0  #date and amount
greatesst_desxrease = 0  #date and amount


