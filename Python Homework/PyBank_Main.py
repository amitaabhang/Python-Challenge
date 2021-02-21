import os
import csv

#Set path of the file
budget_csv = os.path.join("Resources", "budget_data.csv")

#Initialize the list
dateyear =[]
profit_loss =[]

#Read the budget file
with open(budget_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    csv_header = next(csv_reader)
    
    #Make two lists, for dateyear and for profit/losses
    for row in csv_reader:
        if(row[0] != "" and row[1] != ""):
            dateyear.append(row[0])
            profit_loss.append(row[1])


#Convert the profit and losst list of strings to list of integers
converted_profit_loss = list(map(int, profit_loss))

#Set the Total months and total over the entire period
totalmonths = len(dateyear)
Total = sum(converted_profit_loss)

#Create a new list to add the difference
net_total_lst=[]
i=0    
for i in range(len(converted_profit_loss)-1):
    newValue = converted_profit_loss[i+1] -  converted_profit_loss[i]
    net_total_lst.append(newValue)

#get the date year for greatest increase and decrease in profit and losses respectively
greatestincreaseninprofit_dateyear = dateyear[net_total_lst.index(max(net_total_lst)) +1]
greatestdecreaseninprofit_dateyear = dateyear[net_total_lst.index(min(net_total_lst)) +1]

#create a string with formatted output
output = f"""
    Financial Analysis
    -------------------------
    Total Months : {totalmonths}
    Total : ${Total}
    Average  Change: ${round(sum(net_total_lst)/len(net_total_lst),2)}
    Greatest Increase In Profits : {greatestincreaseninprofit_dateyear} $({max(net_total_lst)})
    Greatest Decrease In Losses : {greatestdecreaseninprofit_dateyear} $({min(net_total_lst)})
    """
#Display the output
print(output)

#Write the output to an Analysis file
#Set path of the file
output_path = os.path.join("Analysis", "pyBank_Analysis.txt")

with open(output_path, 'w') as outputCsvfile:
    # Initialize csv.writer
    csv_writer = csv.writer(outputCsvfile)
    csv_writer.writerow([output])
