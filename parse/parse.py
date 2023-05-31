import csv

# Set up input and output variables for the script
dutyTrack = open("calendar.csv", "r")

# Set up CSV reader and process the header
csvReader = csv.reader(dutyTrack)
header = next(csvReader)
nameIndex = header.index("SUMMARY")
dateIndex = header.index("DTSTART")

# Make an empty list
csvList = []

# Loop through the lines in the file and get each coordinate
for row in csvReader:
    name = row[nameIndex]
    name = name.replace("(P) ", "")
    name = name.replace("(S) ", "")
    date = row[dateIndex].rstrip(' 0:0')
    date = date.replace("/",'.')
    csvList.append([name,date])

# Print the coordinate list
file=open("output.txt","w")
file.writelines(["%s," % item  for item in csvList])
file.close()
