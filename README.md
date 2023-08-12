# DraftKings Line Up Generator

## Installation
1. **Locate the "Code" Button:**
   On the main repository page, there's a green button labeled "Code". Click on it. This will open a small menu.

7. **Copy the Repository URL:**
   In the menu, you'll see a URL that ends with `.git`. Click the "Copy" button next to it.

8. **Open Finder**
9. **Create a New Folder (Optional):**
If you wish to keep your downloaded repositories organized, create a new folder.
10. **Open Terminal:**
Now, let's open the "Terminal" application. You can find it by using Spotlight search. Click the magnifying glass in the top-right corner of your screen, type "Terminal", and press Return when it appears.

11. **Navigate to Your Folder:**
In the Terminal window, type cd (with a space at the end), then drag and drop the folder you created (e.g., "GitHub Projects") into the Terminal window. Press Return.

12. **Download the Repository:**
In the Terminal, type in `git clone` and paste the repository URL you copied earlier and press Return. You'll see some messages as the repository is downloaded.

13. **Open the Repository:**
Go back to Finder and navigate to the folder where you downloaded the repository. Double-click the repository folder to open it.


## Usage

**Note**: It's important to note that you shouldn't change bolded cells in the `Input.exe` file

1. Open the `Input.xls` file in Excel.
1. Open the `slots` tab of the file. In Row 1, make sure there's a label for each line up slot in the game you're playing.
2. For each of the labelled columns that were set up in previous step, list all of the player names you're considering for that slot. It's okay to have players listed in multiple columns.
3. Open the `salary` tab of the file. For each player included in the `slots` tab, list their name in Column A and salary in Column B.
   1. Note that a player's name on the `salary` tab must exactly match how it's listed on the `slots` tab.
4. Open the `settings` tab. In cell B2, you can change the max salary for each game.
5. Save the Excel file as `Input.xls`.
6. Run the program to generate lineups!
   1. If you use a Mac, double-click on the `generate_lineups.sh` file.
   1. If you use a PC, double-click on the `generate_lineups.bat` file.
1. Look for your lineups (and the total salaries) in the `lineups.csv`

## License
See the `LICENSE` file contained in the root of the directory