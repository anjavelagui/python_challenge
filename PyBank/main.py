#importing os module and csv files
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open('csvpath' , 'r') as csvfile:

#Create variable for each records to calculate the requested totals
    total_months = []   #month count
    total_net_profit = 0
    total_net_losses = 0
    change_prof_loss = []    #average_change= total net profit losses / total months
    date_count = []
    greatest_increase = 0  #date and amount
    greatest_decrease = 0  #date and amount

# CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
#Read each row of data after the header
    for row in csvreader:
#Calculate the total number of months included in the dataset
    total_months = total_months + 1

#Calculate the total amount profit over the entire period
    previous_profit = int(row[1])
    total_net_profit = total_net_profit + int(row[1])

#Calculate the change in losses over the entire period
    previous_losses = int(row[1])
    total_net_losses = total_net_losses + int(row[1])

#Calculate the Total
    total_amount = total_net_profit - total_net_losses

#Calculate average of change
    average_change =sum (change_prof_loss)/len(change_prof_loss)

#Calculate greater increase - decrease- date and amount
    greatest_increase = max(change_prof_loss)
    greatest_decrease = min(change_prof_loss)

#Providing Financial Analysis Report
    print("Financial Analysis")
    print("------------------------")
    print("Total Months: " + round(total_months))
    print("Total: " + int(total_amount))
    print("Average Change: " + int(average_change))
    print("Greatest Increase In Profits: " + int(greatest_increase))
    print("Greatest Decrease In Profits: " + int(greatest_decrease))

#Writting a outer file
    output = analysis.txt
    with open('analysis.txt' , 'w')
        write("Financial Analysis" "\n")
        write("------------------------") "\n")
        write("Total Months: " + round(total_months) "\n")
        write("Total: " + int(total_amount) "\n")
        write("Average Change: " + int(average_change) "\n")
        write("Greatest Increase In Profits: " + int(greatest_increase) "\n")
        write("Greatest Decrease In Profits: " + int(greatest_decrease)) "\n")
    close = analysis.txt
