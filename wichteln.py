import argparse
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


def write_santas_to_txt(santas):
    with open("santas.txt", "w") as file:
        for i in range(len(santas)):
            santa = santas[i]
            gift_receiver = santas[(i + 1) % len(santas)]
            file.write(f"{santa} -> {gift_receiver}\n")


def write_santas_to_txt_separate(santas):
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


def main():
    parser = argparse.ArgumentParser(description="Secret Santa Assignment Script")
    parser.add_argument(
        "-s",
        "--secret",
        action="store_true",
        help="Write separate files for each santa (select this if you don't want to read the assignments yourself - send out the .txt files without looking at them!)",
    )
    parser.add_argument(
        "-o",
        "--open",
        action="store_true",
        help="Print to console and write to a single file (select this if you are okay with knowing the assignments)",
    )
    parser.add_argument(
        "-r",
        "--reshuffle",
        action="store_true",
        help="Reshuffle until user confirms (select this if you want to play secret santa god)",
    )

    args = parser.parse_args()

    # Ensure only one flag is selected
    if sum([args.secret, args.open, args.reshuffle]) != 1:
        parser.error(
            "Exactly one of --help, --secret, --open, or --reshuffle must be specified"
        )

    # Get shuffled list of santas
    santas = read_participants("participants.csv")
    shuffle(santas)

    if args.reshuffle:
        while True:
            print_santas(santas)
            response = input("Keep this assignment? (y/n): ")
            if response.lower() == "y":
                write_santas_to_txt(santas)
                break
            else:
                shuffle(santas)
    elif args.secret:
        write_santas_to_txt_separate(santas)
    elif args.open:
        print_santas(santas)
        write_santas_to_txt(santas)


if __name__ == "__main__":
    main()
