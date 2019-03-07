"""
Created on Sat Mar  2 21:29:16 2019

@author: maribelojeda
"""

#This code analyses the election_data file in order to extract:
# the number of votes, the winner of the election, a list with the candidates who received votes...
# the votes per candidates and its percentage compared with the total of votes

#import libraries
import os
import csv

#A dictionary is created to store other dictionaries containing the candidate name, number of votes and percentage
dictionary = dict()

#This function is used to extract the list of candidates without duplicates
def Remove(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list 

#This function add a dictionary with the candidates information to the main dictionary
def addDictionary(id, element):
    name= "id"+str(id)
    dictionary[name]= element

#The csv file is imported
csvpath = os.path.join('.', 'Resources', 'election_data (1).csv')


with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # The lists of the data aimed to obtain and store in the dictionary are created. Even though the file has 3 columns 
    # the country and the votes Id are not required for the purpose of this analysis
    candidate_list = []

    for row in csvreader:
        candidate_list.append(row[2])

#The removed function is called to get the list of candidates who received votes 
candidates = Remove(candidate_list)

#The number of votes is calculated by checking the length of a column in the dataset
number_of_votes=len(candidate_list)

#The next step is to calculate the number of votes per candidate and its percentage
# A votes per candidates zeros-list is initialized with the same length of the candidates' list 
votes_per_candidate = [0] * len(candidates)

#The votes that received each candidate are summed
for name in range(len(candidates)):
    for index in range(len(candidate_list)):
            if candidate_list[index] == candidates[name]:
                votes_per_candidate[name] += 1

# A votes percentage zeros-list is initialized with the same lenght of the candidates list 
votes_percentage=[0]*len(candidates)

#To get the votes percentage, the number of votes per candidate is divided by the total number of votes
for name in range(len(candidates)):
    votes_percentage[name]= '{0:.2%}'.format(votes_per_candidate[name]/number_of_votes)

#Then the information of each candidate (name, number of votes and percentage) is stored in a dictionary and then this 
#dictionary into another one using the function "add Dictionary"
for i in range(len(votes_per_candidate)):
    new_dictionary = {"candidate": candidates[i], "votes":votes_per_candidate[i] , "percentage":votes_percentage[i]}
    addDictionary(i, new_dictionary)


#The winner of the election was obtained using the dictionary by checking which was the maximum number of votes
# and then finding which candidate received those votes
max_votes = max(d['votes'] for d in dictionary.values())

print(type(max_votes))
for j in dictionary.values():
    if j['votes'] ==  max_votes:
        winner= j['candidate']
        break

#Formating variables
number_of_votes = format(number_of_votes,",d")
for j in dictionary.values():
    j['votes'] = format(j['votes'],",d")

#The total number of votes, winner of the election and information of each candidate are printed in the console
print("Election Results")
print("___________________")
print(f"Number of votes: {number_of_votes}")
print("Winner: " +winner)
print("_________________________________________")
print("Candidate, Percentage, Number of votes ")
for d in dictionary.values():
    print(f"{d['candidate']}      {d['percentage']}          {d['votes']}")


#Then the same information is stored into a csv file with the name of "Election_Results"
output_file = os.path.join("Election_Results.csv")
title_dictionary = ['id', 'candidate','votes','percentage']

with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    #Prints the title of the file, the number of votes and the winner
    writer.writerow(["Election Results"])
    writer.writerow(["Total votes: ",number_of_votes])
    writer.writerow(["Winner: ",winner])

    #Prints the dictionary data
    w = csv.DictWriter(datafile, title_dictionary)
    w.writeheader()
    for key,val in sorted(dictionary.items()):
        row = {"id": key}
        row.update(val)
        w.writerow(row)
    