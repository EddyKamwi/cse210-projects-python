import Journal as j
import random as r
import sqlite3 as lite
from datetime import datetime

def main():
    # define constants
    CONN = lite.Connection("journal.db")
    CURSOR = CONN.cursor()

    # create table if it does not exit
    query =  '''
            CREATE TABLE IF NOT EXISTS entries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                prompt TEXT NOT NULL,
                answer TEXT NOT NULL
            )
            '''
    CURSOR.execute(query)
    CONN.commit()
    
    # create a dictionary as a virtualfile
    journalEntries = {}

    # all prompts for the program
    prompts = [
            "Who was the most interesting person I interacted with today?",
            "What was the best part of my day?",
            "How did I see the hand of the Lord in my life today?",
            "What was the strongest emotion I felt today?",
            "If I had one thing I could do over today, what would it be?",
            "Did you minister to any one today? Who is in the most need to be ministered to?",
            "How often did I feel the Savior's love during the day?",
            "What was one thing I did to prepare myself to partake of the sacrament?",
            "Are you happy? Why?"]
    
    # program welcome message
    print("Welcome to the Journal Program!")

    # loop main menu
    while True:
        menu = "Please select one of the following choices:\n1. Write\n2. Display\n3. Load \n4. Save \n5.Quit\n> "
        ans = input(menu)

        # write to journal
        if ans == "1":
            prompt = r.choice(prompts)
            promptAns = input(prompt+"\n>")

            while promptAns == "":
                promptAns= input("please enter a valid answer \n> ")

            journal = j.Journal(prompt,promptAns)
            date = datetime.now()
            journalEntries[len(journalEntries)] = [prompt,promptAns,date.strftime("%d-%m-%Y")]

        # Display to journal
        elif ans=="2":
            for index in journalEntries:
                pair = journalEntries[index]
                journal = j.Journal(pair[0],pair[1],pair[2])
                print(journal.GetJournalDisplay())

        # Load Journal
        elif ans=="3":
            query = "SELECT * FROM entries"
            journalEntries = {}
            rows = CURSOR.execute(query)
            CONN.commit()
            for row in rows:
                journalEntries[row[0]] = [row[1],row[2],row[3]]       

        # Save current Journal
        elif ans=="4":
            if len(journalEntries) !=0:
                for index in journalEntries:
                    entry = journalEntries[index]
                    query = "INSERT INTO `entries` (`date`, `prompt`, `answer`) VALUES (?,?,?)"
                    CURSOR.execute(query,(entry[0],entry[1],entry[2]))
                    CONN.commit()

            else:
                print("Sorry there is nothing to save!")

        # exit
        elif ans=="5":
            break
        

            
    

if __name__ == "__main__":
   main()