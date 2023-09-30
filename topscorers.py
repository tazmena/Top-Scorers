# Get the top scorers

highestScore = 0
topScorers = [""]

fileName = input("Please enter the full file name you'd like to enter: ")
file = open(fileName,"r") #Opened in read mode.
data = file.readlines()
data = [line.strip().split(",") for line in data[1:]] #To strip each list item of whitespace and characters, index slicing to remove column names

for i in range(0,len(data)):
    for j in range(0,len(data[i])): #Nested for loop to read 2d array (data)
        if j == 2:
            if int(data[i][j]) > int(highestScore):
                highestScore = data[i][j]
                topScorers[0] = data[i][j-2]+" "+data[i][j-1] #First name and last name, update current top scorer by overwritting topScorers[0]
                del topScorers[1:] #Deleting previous highest scorers
            elif int(data[i][j]) == int(highestScore):
                topScorers.append(data[i][j-2]+" "+data[i][j-1]) #Add on any other top scorers with same as current highest


topScorers = (sorted(topScorers)) #Sort alphabetically
for i in range(0,len(topScorers)):
    print(topScorers[i])
print("Score:",highestScore)
