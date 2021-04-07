import os
import csv
election_datacsv = os.path.join('..', 'Resources', 'election_data.csv')
with open(election_datacsv, 'r') as csvfile:
    csv_read = csv_reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
#Assigning variables
candidates_names = []
cand_percentage_votes = []
cand_total_num_votes = []
winner_poplr_vote = []
total_num_votes = []
election_data = []

for row in csv_read:
    total_num_votes += 1
    if row[2] in election_data.keys():
        election_data[row[2]] = election_data[row[2]] + 1
        election_data[row[2]] = 1

#Calculating the number of votes for each candidate
for key, value in election_data.items():
    candidates_names.append(key)
    cand_total_num_votes.append(value)

#calculate the percentages
def percentage_votes(election_data[])
    candidates_names = str(election_data[])
    cand_percentage_votes = (total_num_votes / cand_total_num_votes) * 100

#Looking for the winner
new_elect_data = list(zip(candidates_names, cand_total_num_votes, cand_percentage_votes))

winner_cand = []
for candidates_names in new_elect_data:
    if max(total_num_votes) == candidates_names[1]:
        winner_cand.append(candidates_names[0])
winner_poplr_vote = winner_cand[0]

#Providing the Results
print("Election Results")
print("________________________________")
print("Total Votes :", + int(total_num_votes))
print("________________________________")
print(candidates_names)
print("__________________________________")
print("Winner :", + str(candidates_names, winner_poplr_vote))
print("________________________________________________")

#Writting a outer file
    output = analysis.txt
    with open('analysis.txt' , 'w')
        write("Election Results" "\n")
        write("____________________________________") "\n")
        write("Total Votes : " + int(total_num_votes) "\n")
        write("__________________________________")
        write("Candidates-names: " + str(candidates_names) "\n")
        write("____________________________________________________")
        write("Winner : ", + str(candidates_names, winner_poplr_vote)) "\n")
    close = analysis.txt
