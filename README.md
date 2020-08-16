# Election Analysis

#Overview:

#Much like the stocks, the election analysis served to create an automated way to gather data that can either be reused or updated. This time, we created it with python, not vba.
The python used was relatively barebones, no externally installed packages and served only to introduce us more to if then statements, loops, opening and reading CSV 
files, and creating, opening, and writing text files. the data highlighted key points from the data, including how many votes cast, who won the election, 
which county had the best turnout by sheer numbers, and what percentage each candidate received. 

#Analysis:

overall, the statistics and numbers shown in election_results.txt demonstrate every bullet point here, but to briefly summarize:

    #Overall, citizens cast 369,711 votes. 
    #Of those votes, the most (306,055 for 82.8%) came from Denver county. Jefferson was a not close second (38,855 for 10.5%) and Arapahoe trailed in last (24,801 for 6.7%)
    #This makes Denver the largest by quantity (again, 306,055 for 82.8%), but we don't know enough to say whether or not its population was merely larger, 
    if they had better turnout rates, or some combination of the two. 
    #Regarding candidates, Charles Casper Stockham got  85,213 for 23.0% of the vote. Diana DeGette got 272,892 for 73.8%, and Raymon Anthony Doane got 11,606 for 3.1%. 
    #This makes Diana the winner, with 272,892 of 369,711 votes, leaving her with 73.8% of the total vote.
    
#Script Applications and modifications

#Overall, the script is pretty universal, as it focuses on rows, not specific keywords. If data from other elections is presented in a similar manner, it could easily
capture the same statistics. Issues would arise only if a CSV file contained data in different columns, say, ballot ID, candidate, then county, instead of ballot id, county,
and candidate, or if any additional columns were also thrown into the mix, like time of vote. One solution, if possible, would be to search for a keyword within the CSV headers.
I'm a little unsure of how to write the code, but writing something looking for a keyword, such as county or candidate, determining what column that is, and creating a variable 
based on that column, making it read candidate_name = row[Candidate_Column] instead of candidate_name = row[2]. There are other issues that may arise, such as 
if the dataset contains more than one election, or if it uses alternate words like district or vote cast for, so the CSV must still be glanced at for that information. While this 
Assumes no new data would be worth analyzing, it's entirely possible a new variable, such as vote cast by mail in or in person, whether the voter was a Democrat, Republican 
or Independent, and if they voted for anything else in this election. Much like how county was added, this data can be accounted for by recycling the current code's structure but
changing what it looks for. If the voter's registered affiliation was captured in column 5, for example, it could be captured with changes like Party_status = row[4] or 
Party_status = row[Party_Column], and making similar appropriate changes throughout the code.
