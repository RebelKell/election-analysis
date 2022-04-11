# Election Analysis

## Overview
We were hired by the Colorado Board of Elections to run an election audit of their most recent congressional election.

They have tasked us with the following:
1. Calculating total votes cast.
2. Calculate percentage and total count of votes for each county.
3. Determine which county had the largest turnout.
4. Calculate percentage and total count of votes for each candidate.
5. Determine the winner of the election.

### Resources
 To run this analysis we were provided .csv file with all the votes cast in the election. We used Python 3.7 to build the program and Visual Studio to write and debug our code.  


## Election Audit Results


In total 369,711 voters cast a ballot across three counties for three candidates vying for the congressional seat. This congressional district consists of three counties - Arapahoe, Denver and Jefferson. 

Below is a breakdown of the county results in this congressional district:

- **Jefferson**: 10.5% (38,855)
- **Denver**: 82.8% (306,055)
- **Arapahoe**: 6.7% (24,801)

Denver, the most populous county in the district, had the most votes cast.

There were three candidates running in this election. Below are the results for each candidate broken down by name, their percentage of the vote and the total number of votes they received. 
- **Charles Casper Stockham**: 23.0% (85,213)
- **Diana DeGette**: 73.8% (272,892)
- **Raymon Anthony Doane**: 3.1% (11,606)

Based on these results, Diana DeGette won the popular with 272,892 total votes - 73.8% of total votes cast.

## Election-Audit Summary
The script that we wrote to run this analysis is a solid base to run the analysis of any election that the the Colorado Board of Elections oversees. This script could handle the addition of more candidates and counties and easily tabulate the results,  provide a breakdown of the results and determine a winner. 

However, if the Colorado Board of Elections were to use this script in the future, we would suggest the following modifications to provide a richer analysis: 

- Add a breakdown of county results by candidate. Additional analysis on how the candidates did within each county could provide more insight on the election and potentially highlight any irregularaties. 
- Add a flag for duplicate ballot IDs. Adding this to the script would allow for the election board to see where ballots may have been added more than once - adding more security and confidenceto the results. 




