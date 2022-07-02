# import the csv and as modules
import csv; import os

# load the file to read the survey data
inputFile = os.path.join("Resources", "election_data.csv")

# output file election data analysis
outputFile = os.path.join("Analysis", "Election Analysis.txt")

# variables
totalVotes = 0      # variable that holds the total number of votes
candidates = [] #list to hold all the candidates
candidatevotes = {} # dictionary to hold each candidates votes
winningcount = 0 #to hold the winning count
winner = ""

# read the csv file
with open(inputFile) as electionData:
    #create the csv reader
    csvreader = csv.reader(electionData)
    
    # read the header
    header = next(csvreader)
   
    #row will be lists
     # index 0 is the Ballot ID and index 2 is the candidate
    for row in csvreader:
        # add on to the total votes
        totalVotes += 1 # same as totalVotes = totalVotes + 1
       
        # check to see if the candidate is in the list of candidates
        if row[2] not in candidates:
            # add to the list of candidates if not in already
            candidates.append(row[2])

            #add the value to the dictionary too
            candidatevotes[row[2]] = 1

        else:
            #if candidate is in list, add a vote to the count
            candidatevotes[row[2]] +=  1

voter_output = ""

for candidates in candidatevotes:
    #get the vote count and it's respective percentage
    votes = candidatevotes.get(candidates)
    votesPct =(float(votes) / float(totalVotes)) * 100.00
    voter_output += f"{candidates}: {votesPct:,.3f}% ({votes:,})\n"
    
    #compare the votes to the winning count
    if votes > winningcount:
        #vote becomes new winner
        winningcount = votes
        #update winning candidate
        winner = candidates


output = (
    f"\nElection Results\n"
    f"-------------------------------\n"
    f"Total Votes: {totalVotes:,}\n"
    f"-------------------------------\n"
    f"{voter_output}"
    f"-------------------------------\n"
    f"Winner: {winner}\n"
    f"-------------------------------\n"
)

# print output
print(output)

# export the data to a text file
with open(outputFile, "w") as textFile:
    # write the output to the text file
    textFile.write(output)