# wichteln
 A script to shuffle participants for a round of secret santa.

## How to install

0. **Ensure you have python installed**
   The script uses the argparse and csv modules, which are included in the Python standard library. No additional installation is required.

1. **Clone the repository:**
   ```sh
   git clone <repository_url>
   cd <repository_directory>


## How to use

0. **Prepare the participants list:**
   - Modify `participants.csv` (in the same directory as `wichteln.py`) to reflect the names of your participants. Don't forget your own name! 
   - Add the names of all participants, one per line, separated by commas. For example:
     ```
     Bob,
     Ben,
     Alice
     ```

1. **Run the script with one of the following flags:**
   - `-s` or `--secret`: Write separate files for each santa without printing to the console. This is useful if you don't want to know the assignments yourself, as you can send out each .txt file to the corresponding participant without opening it.
     ```sh
     python wichteln.py --secret
     ```
   - `-o` or `--open`: Print the assignments to the console and write them to a single file named `santas.txt`.
     ```sh
     python wichteln.py --open
     ```
   - `-r` or `--reshuffle`: Print the assignments to the console and allow reshuffling until you confirm. Once confirmed, the assignments are written to `santas.txt`.
     ```sh
     python wichteln.py --reshuffle
     ```

2. **Ensure only one flag is selected at a time.** If multiple or no flags are selected, the script will raise an error.