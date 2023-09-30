# Top-Scorers
# Get the top scorers

## Description
The purpose of this program is to output the top scorers and the highest score in alphabetic order.
The program takes a plain-text file as input, such as TestData.csv.

## Explaination
To tackle the given problem, I first had to find a way to read the csv file data. To do this, I decided to use the built in "open" method, and opened the file in read mode as we will only need to read the data in this instance. Next, to ensure this was successful, I printed the data, and found that there was whitespace, so I removed this using the .strip method. Now that the data had been formatted, it was ready to be processed. I used a nested for loop as the data was in a 2d array structure, looping through each element (representing each row) and within that, each element represented the first name, last name and score, hence the use of the second for loop. To compare the scores, I set a variable (highestScore) to 0, and for every score, if it was higher than this variable, it would be overwritten with the new highest score. For the first highest scorer, an array containing one empty string element was overwritten with the highest scorer's name. If there was another scorer with the same as the current highest score, their name was appended. If there then came another scorer who's score was even higher, their name would overwrite the first, and the rest of the elements in the array were deleted. Finally, once the data has completed its parsing, I simply sorted the array of names alphabetically using the "sorted" function and output the name(s) and score. 

The above was my chosen approach to the problem, as I thought that this would be the most efficient way. By storing the data as a 2d array, the data relevant to each other could be grouped together, such as the first row being the first element containing 3 elements within (eg. [[Dee, Moore, 56]]). One of the key aspects of software engineering is ensuring the maintainability of code and that it is written in a way that it is easy to understand or modify. This is why I ensured that the code was well commented, with clear structure and easy-to-understand variable names using camel casing, so that any other developers who may look at the code can understand the intended process to solve the problem. My use of for loops and indexes also meant that any changes to the data would allow the code to adapt (eg. more than the given 4 scorers), as I used the indexes "i" and "j". To test the final program, I entered extra data to the test data file and found that the top scorers would still contain previous top scorers. To fix this I added  "del topScorers[1:]" to delete every other element than the first.


## Instructions to run code
- Open the .py file in an IDE of any choice, ensure that the TestData.csv file is saved in the same folder.
- When prompted, a user must input the full name of the file they which to receive the highest scorers of, such as entering "TestData.csv".
- The program will then display the top scorer's name(s) and the highest score achieved from the given data.
