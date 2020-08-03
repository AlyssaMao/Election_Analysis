# Election Audit

## Overview of Project

### Purpose
The purpose of the election audit analysis is to determine the winning candidate and the county with the largest turnout as well as providing specific data regarding each county and candidate based on the raw election data. 

## Results

### Analysis of Election Data
Please refer to the linked txt file below for the results of my analysis
>[Election Results](analysis/election_results.txt)

Additionally, please refer to the code referenced below for how the results were generated 
```
# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge starter code."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_results.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}

# 1: Create a county list and county votes dictionary.
county_options = []
county_votes = {}


# Track the winning candidate, vote count and percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# 2: Track the largest county and county voter turnout.
largest_county= ""
largest_turnout=0



# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]

        # If the candidate does not match any existing candidate add it to
        # the candidate list
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # And begin tracking that candidate's voter count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1

        # 4a: Write a decision statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in county_options:

            # 4b: Add the existing county to the list of counties.
            county_options.append(county_name)

            # 4c: Begin tracking the county's vote count.
            county_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        county_votes[county_name] +=1

# Save the results to our text file.
with open(file_to_save, "w") as txt_file:

    # Print the final vote count (to terminal)
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n\n"
        f"County Votes:\n")
    print(election_results, end="")

    txt_file.write(election_results)

    # 6a: Write a repetition statement to get the county from the county dictionary.
    for county_name in county_votes:
        # 6b: Initialize a variable to hold the county’s votes as they are retrieved from the county votes dictionary.
        votes2 = county_votes[county_name]
        # 6c: Calculate the percent of total votes for the county.
        vote_percentage2 = float(votes2)/float(total_votes)*100

         # 6d: Print the county results to the terminal.
        county_results=(f"{county_name}: {vote_percentage2:.1f}% ({votes2:,})\n")
         # 6e: Save the county votes to a text file.
        txt_file.write(county_results)

         # 6f: Write a decision statement to determine the winning county and get its vote count.
        if (votes2>largest_turnout) and (vote_percentage2>winning_percentage):
            largest_turnout=votes2
            largest_county= county_name
            winning_percentage2 = vote_percentage2
    # 7: Print the county with the largest turnout to the terminal.
        winning_county_summary = (
            f"----------------------\n"
            f"Largest County Turnout: {largest_county}\n"
            f"----------------------\n"
        )
        print(winning_county_summary)

    # 8: Save the county with the largest turnout to a text file.
    txt_file.write(winning_county_summary)

    # Save the final candidate vote count to the text file.
    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the
        # terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    # Print the winning candidate (to terminal)
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate's name to the text file
    txt_file.write(winning_candidate_summary)

``` 
Based on the above, I noted the following:
  * A total of 369,711 votes were cast in this congressional election 
  * Breakdown by county were as follows:
    - Jefferson county had 38,855 total votes and made up 10.5% of the total votes in the precinct
    - Denver county had 306,055 total votes and made up 82.8% of the total votes in the precinct
    - Arapahoe county had 24,801 total votes and made up 6.7% of the total votes in the precinct
  * Denver county had the largest number of votes
  * Breakdown by candidates were as follows: 
    - Charles Casper Stockham had 85,213 votes which accounted for 23% of total votes casted
    - Diana DeGette had 272,892 votes which accounted for 73.8% of total votes casted
    - Raymon Anthony Doane had 11,606 votes which accounted for 3.1% of total votes casted
  * Diane DeGette won the election with 272,892 votes which accounted for 73.8% of total votes

## Election-Audit Summary

To the election commission, the above script can be modified in order to analyze data for any given election. For example, the counties can be changed to states, and the candidates may be presidential candidates. We can then utilize a modified version of the script to capture election results for presidential elections instead of congressional elections. In a school election, where the candidate who receives the most popular vote becomes president and the candidate with the second most number of votes becomes vice president, this script can also be modified to address this need. We can modify the output to display both the winner and the runner-up and allocate the president and vice president title based on candidate vote counts accordingly. 
