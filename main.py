#import modules 
import os
import csv

#list
dates = list()
revenue = list()

#add txt break to print easier 
text_break = "-----------------------------"

#create title paths
csvpath = os.path.join("..", "Pybank_Resources", "budget_data.csv")
csv2file = os.path.join("..", "Pybank_Resources", "Financial_Analysis.txt" )

#csv reader with "r" not newline
with open(csvpath,"r") as csvfile:

    for line in csvfile:
        date = list()
        revenues = list() 

    with open(os.path.join("..","Pybank_Resources", "budget_data.csv"), "r") as data:
        bankdata = csv.reader(data)

        #read header
        linex = next(bankdata)

        for column in data:
            split_column = str.split(column, ',')
            date.append(split_column[0])
            revenue.append(int(split_column[1]))

    months = len(revenue)
    gross_revenue = sum(revenue)

    #store changes as list of values
    rev_change = list()

    for x in range(len(revenue)-1):
        rev_change.append(revenue[x+1]-revenue[x])
        avg_rev_change = round(sum(rev_change)/len(rev_change),2)
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        max_month = date[rev_change.index(max_rev_change)+1]
        min_month = date[rev_change.index(min_rev_change)+1]

    #print values
    print("Financial Analysis: ")
    print(text_break)
    print(f"Total Months: {months}")
    print(f"Total Revenue: ${gross_revenue}")
    print(f"Average Revenue Change: ${avg_rev_change}")
    print(f"Greatest Increase in Profits: {max_month} ${max_rev_change}")
    print(f"Greatest Decrease in Profits: {min_month} ${min_month}")

    #write data to text.write
    with open(csv2file, "w") as text_file:
        text_file.write("Financial Analysis: \n")
        text_file.write(text_break)
        text_file.write(f"Total Months: {months}\n")
        text_file.write(f"Total Revenue: ${gross_revenue} \n")
        text_file.write(f"Average Revenue Changes: ${avg_rev_change}\n")
        text_file.write(f"Greatest Increase in Profits: {[max_month]} ${[max_rev_change]}\n")
        text_file.write(f"Greatest Decrease in Profits: {min_month} ${min_rev_change}\n")
        text_file.close()






