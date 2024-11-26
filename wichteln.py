"""random secret santa assignment script"""

import csv
from random import shuffle

# Read participants from a .csv file
participants = []
with open("participants.csv", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        participants.append(row[0])

participants_total = len(participants)

# Shuffle participants. Each participant gives a gift to the next one in the resulting list
shuffle(participants)

# Print assigned santas
for i in range(participants_total):
    if i + 1 < participants_total:
        print(participants[i] + " -> " + participants[i + 1])
    else:
        print(participants[i] + " -> " + participants[0])
