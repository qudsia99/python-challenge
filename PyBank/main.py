#First import corresponding modules (os, and csv)

import os
import csv

#Create any relevant variables to store info

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
#encoding it is not necessary in this step, as the data bank does not contain any foreign characters
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
    print(f'Max Profit: {str(maxprofit).strip("[]")}')
    print(f'Min Profit: {str(minprofit).strip("[]")}')
           
    # Calculate the Average Net Change
    net_monthly_avg = sum(net_change_list) / (len(totalmonths) - 1)
    print("The monthly avg: $" + str(net_monthly_avg))



#Transfer all data into a Zip file, to be used later
zipbankclean_csv = list(zip(totalmonths, str(netvalue), str(net_monthly_avg), str(maxprofit), str(minprofit)))


bank_output_file = os.path.join("PyBank", "Analysis", "bank_output.csv")


#opening the output file
with open(bank_output_file,"w", newline='') as bankresults:
    csvwriter = csv.writer(bankresults)

    #create a header
    csvwriter.writerow(["Total Months","Net Total of Profit/Loss ", "Average Profit/Loss","Max Profit","Min Profit"])

    #write row values
    csvwriter.writerow([len(totalmonths), netvalue, net_monthly_avg, maxprofit, minprofit])






