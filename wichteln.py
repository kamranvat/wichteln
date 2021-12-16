"""random secret santa assignment script"""
from random import shuffle

# Get all participants
participants = ["Bob", "Ben", "Der Ganjamann", "Harro", "Jesus"]
participants_total = len(participants)

# Shuffle participants. Each participant gives a gift to the next one in the resulting list
shuffle(participants)

# Print assigned santas
for i in range(participants_total):
	if i+1 < participants_total:
		print(participants[i] + " -> " + participants[i+1])
	else:
		print(participants[i] + " -> " + participants[0])