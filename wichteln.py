"""random secret santa assignment script"""

import csv
from random import shuffle


def read_participants(csv_path):
    """
    Reads participants from a .csv file and returns a list of names.
    """
    participants = []
    with open(csv_path, newline="") as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            participants.append(row[0])
    return participants


def write_each_santa_to_txt(santas):
    """
    Writes a separate .txt file for each santa with the name of the gift receiver.
    Useful if you want to send the assignments without reading them yourself.
    """
    for i in range(len(santas)):
        santa = santas[i]
        gift_receiver = santas[(i + 1) % len(santas)]
        with open(f"{santa}.txt", "w") as file:
            file.write(
                f"Dear {santa},\n\nYou are the secret santa of {gift_receiver}.\n\nMerry Christmas!"
            )


def print_santas(santas):
    """
    Prints the secret santa assignments to the console.
    """
    for i in range(len(santas)):
        santa = santas[i]
        gift_receiver = santas[(i + 1) % len(santas)]
        print(f"{santa} -> {gift_receiver}")


# Get shuffled list of santas
santas = read_participants("participants.csv")
shuffle(santas)

print_santas(santas)
