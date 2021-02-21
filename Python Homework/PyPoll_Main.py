import os
import csv

#Set input file path variable 
election_csv = os.path.join("Resources", "election_data.csv")

#Initialize variables
candidates =[]
vote_dict ={}
total_votes = 0

#Open file and read
with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
 
    csv_header = next(csv_reader)
       
    #Make dictonary of candidate to votes
    for row in csv_reader:
        total_votes = total_votes +1
        
        if(row[2] not in candidates):
            candidates.append(str(row[2]))
            vote_dict[row[2]] =0

        vote_dict[row[2]] += 1
    
    #Create output string part1
    output1= f"""
        Election Results
        -----------------------
        Total votes: {total_votes}
        ----------------------- """

    #Create output string part2 dynamically
    output2=""
    for candidate, votes in vote_dict.items():
        output2 = output2 + "\n" +"\t"+f"{candidate}: {(votes/total_votes)*100:.3f}%  ({votes})"
        #print(f"{candidate}: {(votes/total_votes)*100:.3f}%  ({votes})")

    #Get Max votes and winner  set the output string part3
    maxVotes=0
    for candidate, votes in vote_dict.items():
        if votes > maxVotes:
            maxVotes = votes
            winner = candidate
    
    output3=f""" 
        ----------------------
        Winner: {winner}
        ----------------------
             """

    #Print the whole output
    print(output1)
    print(output2)
    print(output3)
    
#Write the output to an Analysis file
#Set path of the file
output_path = os.path.join("Analysis", "pyPoll_Analysis.txt")

with open(output_path, 'w') as outputCsvfile:
    # Initialize csv.writer
    csv_writer = csv.writer(outputCsvfile)
    csv_writer.writerow([output1])
    csv_writer.writerow([output2])
    csv_writer.writerow([output3])

   
  

    