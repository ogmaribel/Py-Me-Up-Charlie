"""
Created on Sat Mar  2 21:29:16 2019

@author: maribelojeda
"""
#This code analyses financial records stored in a csv in order to extract:
# the number of months on the dataset, the sum of all the P&L, the average change in P&L,...
# the greatest increase and the greatest decrease

#import libraries
import os
import csv

#The csv file is imported
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # Lists of the data required are created. 
    budget_list = []
    month_list = []
    change_list = []
    counter = 0
    max_value = 0
    #The min_value is initialized with an infinitum value
    min_value = float("inf")

    #The months and budget of the csv file are store in the lists
    for row in csvreader:
        month_list.append(row[0])
        budget_list.append(int(row[1]))

        #The change per month is calculated and stored in a list
        if counter > 0:
            change = budget_list[counter] - budget_list[counter-1]
            change_list.append(change)

            #The minimum and maximum changes are saved in variables
            if change >  max_value:
                max_value = change
                count_max= counter

            if change < min_value:
                min_value = change
                count_min= counter

        counter += 1

#Formating the variables
max_value = format(max_value,",d")
min_value = format(min_value,",d")
total_months= format(len(budget_list),",d")
total_budget = format(sum(budget_list), ",d")
average_change= '{:0,.2f}'.format(sum(change_list)/len(change_list))

#The results are printed in the console
print("\n")        
print("Finantial Analysis")
print("________________________")

print(f"Total of months: {total_months}")
print(f"Total: {total_budget}" )
print(f"Average Change: {average_change}")
print(f"Greatest Increase in Profits: {month_list[count_max]} : {max_value}")
print(f"Greatest Decrease in Profits: {month_list[count_min]} : {min_value}")

#The results are printed in a csv file using the zip methond
titles = ["Total of months", "Total", "Average Change", "Greatest Increase in Profits Date","Greatest Increase in Profits:","Greatest Decrease in Profits Date:","Greatest Decrease in Profits:"]
amounts = [total_months, total_budget, average_change, month_list[count_max],max_value,month_list[count_min],min_value]

# Zip all the lists together into tuples
summary = zip(titles, amounts)

# save the output file path
output_file = os.path.join("finantial_summary.csv")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Finantial Analysis"])
    writer.writerows(summary)

