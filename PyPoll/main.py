#import modules

import os
import csv

#Create all proper variables to store info


candidate_dict = {} #Most important dictionary, as it will contain all important info relating to every candidate,
                    #such as their name, votes received, and percentage value

totalvotes = []  #How many votes were cast entirely

current_row = [] #For keeping track of which row we are currently on
last_row = []

votes_for_candidate = 0 #Setting variables to zero
votes_per = 0

current_candidate = "" #Empty string in order to add candidate name


#create data file path 

csvpath = os.path.join("PyPoll","Resources","election_data.csv")


#Opening file using 'r', as we are only extracting info.

with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping header
    csvheader = next(csvreader)

    #Running for loop 
    for row in csvreader:
        totalvotes.append(row[0])
        current_candidate = row[2]
        #print(current_candidate)

        if current_candidate not in candidate_dict:
            candidate_dict["Name"] = (current_candidate)  
            candidate_dict["Total Votes"] = (votes_per)
            #candidate_dict["Percentage of Votes"] = (((candidate_dict(str["Total Votes"]))/str(totalvotes))*100 + "%")
            
            #Resetting votes count for the next candidate on list
            votes_per = 0
    
        elif current_candidate in candidate_dict:
            votes_per += 1 
            #Adding onto the vote count if the candidate is the same
        

    #winner = max(candidate_dict["Total Votes"].values())
    #Finding the winner based on the max value from the "Total Votes" key in the candidate dictionary
    #print("The Winner is: " + str(winner))


#Now to export our cleaned data to a new file.

poll_cleaned = os.path.join("PyPoll","Analysis","pollclean.csv")

#Open file with writing ability
with open(poll_cleaned, 'w', newline="") as pollfile:
    csvwriter = csv.writer(pollfile)

    #Create header
    csvwriter.writerow(["Total Votes Cast", "List of Candidates","Total Votes Per Candidate", "Percentage of Votes", "Winner"])

    #Filling in row values, using dictionary
    csvwriter.writerows([str(totalvotes)], [str(candidate_dict["Name"])],[str(candidate_dict["Total Votes"])],[str(candidate_dict["Percentage of Votes"])], [str("winner")])