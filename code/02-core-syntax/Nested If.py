"""
Write a program to input from user an integer(n) representing the rating of a person on a platform.

You have to print the category of that person.

If the rating is greater than or equal to 2100 then that person is "grand master".
If the rating is greater than or equal to 1900 then that person is "candidate master".
If the rating is greater than or equal to 1600 then that person is "expert".
If the rating is greater than or equal to 1400 then that person is "pupil".
If the rating is smaller than 1400 then that person is "newbie".

NOTE: Print all the chars of the category of the person in lowercase if rating is odd otherwise print in UPPERCASE
"""

N = int(input())

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
