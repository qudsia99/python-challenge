# python-challenge
Week 3 Assignment, Python
#=========================
#=========================
#PYBANK ACTIVITY#

#First import corresponding modules (os, and csv)

import os
import csv

#Create all proper variables to store info in, important to note different variables are assigned different values due to the variable type ranging from a dictionary, list, or plain string.

totalmonths = [] 
netvalue = 0 # of all period
totalprofits = []
month_of_change = []
net_change_list = []
maxprofit= ["", 0]
minprofit = ["", 9999999999999999999]
prev_net = 0

#=======================================

#Creating path to the file we are going to use (budget_data.csv). Here we are just utilizing os module
csvpath = os.path.join("PyBank","Resources", "budget_data.csv") 


#Opening the file we are extracting data from (budget_data.csv)
#NOTE: encoding it is not necessary in this step, as the data bank does not contain any foreign characters
#Since we are not adding on to the data, we are only going to be cleaning up, so we will use the 'r' function

with open(csvpath, 'r', encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #Skipping the header
    csv_header = next(csvreader)

    #Running the loop
    for row in csvreader:
        totalmonths.append(row[0])
        netvalue += int(row[1])

         #Tracking the net change
        net_change = int(row[1]) - prev_net
        prev_net = int(row[1])
        net_change_list += [net_change]
        month_of_change += [row[0]]

        #Calculating Maxprofit of all period
        if net_change > maxprofit[1]:
            maxprofit[0] = row[0]
            maxprofit[1] = net_change

        #Calculating Minprofit of all period
        if net_change < minprofit[1]:
            minprofit[0] = row[0]
            minprofit[1] = net_change
        

        #counting all months placed in index = [0] as in each row there is 1 month, then adding it to the variable 'totalmonths'
    print("There are a total of " + str(len(totalmonths)) + " months")
    print("The net Profit/loss is: $" + str(netvalue) + " over the entire period")
    print("Max Profit: " + str(maxprofit))
    print("Min Profit: " + str(minprofit))
           
    # Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / len(totalmonths)
    print("The monthly avg. " + str(net_monthly_avg))



#Transfer all data into a Zip file, to be used later
zipbankclean_csv = list(zip(totalmonths, str(netvalue), str(net_monthly_avg), str(maxprofit), str(minprofit)))


bank_output_file = os.path.join("PyBank", "Analysis", "bank_output.csv")


#opening the output file
with open(bank_output_file,"w", newline='') as bankresults:
    csvwriter = csv.writer(bankresults)

    #create a header
    csvwriter.writerow(["Total Months","Net Total of Profit/Loss ", "Average Profit/Loss","Max Profit","Min Profit"])

    #write row values
    csvwriter.writerows([[str(len(totalmonths))], [str(netvalue)], [str(net_monthly_avg)],[str(maxprofit)],[str(minprofit)]])
    

#==============================
#PYPOLL ACTIVITY#

#importing modules

import os
import csv

#Create all proper variables to store info in, important to note different variables are assigned different values due to the variable type ranging from a dictionary, list, or plain string.


candidate_dict = {} #important dictionary, as it will contain all important info relating to every candidate,
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
