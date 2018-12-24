# import lists
import os
import csv

# declare variables
voter_ID = list()
county = list()
candidate = list()
text_break = "-----------------------------------"
# Placeholders for re-formatted contents
unique_count = list()
total_count = list()
percentage_of_count = list()

# Initiating file path
csvpath = os.path.join("..", 'PyPoll_Resources', "election_data.csv")
output_path = os.path.join("..", "PyPoll_Resources", "election_results.txt")

# open csv reader 
with open(csvpath, "r") as csvfile:
    csvreader = csv.reader(csvfile)

    # first row as header - skip
    headline = next(csvreader)

    # identify the list for unique counts
    for line in csvreader:
        voter_ID.append(line[0])
        county.append(line[1])
        candidate.append(line[2])
        if line[2]not in unique_count:
            unique_count.append(line[2])
    total_votes = len(voter_ID)

   #use crazy for c in loop 
    for c in unique_count:
        total_count.append(candidate.count(c))
        percentage_of_count.append(round(candidate.count(c)/total_votes*100,2))
        Victor = unique_count[total_count.index(max(total_count))]

    # print results - make sure winner is defined this time
    print("Election Results")
    print(text_break)
    print(f"Total Votes: {total_votes}")
    print(text_break)
    for x in range(len(unique_count)):
        print(str(unique_count[x]) + ": " + str(percentage_of_count[x]) +"%" +" " + "(" + str(total_count[x]) + ")")
    print("")
    print(text_break)
    print(f"Winner: {Victor}") 
    print(text_break)

    # Writting data to a file using text.write
    with open(output_path,"w") as text_file:
        text_file.write(f"Election Results: \n")
        text_file.write(f"{text_break}\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write(f"{text_break}\n")
        for x in range(len(unique_count)):
            text_file.write("" + str(unique_count[x]) + ": " + str(percentage_of_count[x]) +"%" +" " + "(" + str(total_count[x]) + ")" + "\n")
        text_file.write(f"{text_break}\n")
        text_file.write(f"Winner: {Victor}\n")
        text_file.write(f"{text_break}\n")

