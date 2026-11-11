"""
Read an integer `N` representing a user's platform rating.

Print the category associated with that rating.

Ratings of 2100 or higher are "grand master".
Ratings from 1900 to 2099 are "candidate master".
Ratings from 1600 to 1899 are "expert".
Ratings from 1400 to 1599 are "pupil".
Ratings below 1400 are "newbie".

For odd ratings, print the category in lowercase; for even ratings, print it in uppercase.
"""
# Get user input (input is always a string)
N = int(input("Enter the rating of the person: "))

# Check if the rating is even or odd and determine the category accordingly
if (N % 2) == 0:
    if N >= 2100:
        print("GRAND MASTER")
    elif N >= 1900:
        print("CANDIDATE MASTER")
    elif N >= 1600:
        print("EXPERT")
    elif N >= 1400:
        print("PUPIL")
    else:
        print("NEWBIE")
else:
    if N >= 2100:
        print("grand master")
    elif N >= 1900:
        print("candidate master")
    elif N >= 1600:
        print("expert")
    elif N >= 1400:
        print("pupil")
    else:
        print("newbie")