# Simple Notes App - Kris, 2025
# Saves notes to a file, reads them back, and lets user search for keywords in notes.

# Function to write a new note to the file
def write_note():
    # Open the file in append mode, so new notes are added to the end
    with open("notes.txt", "a") as file:
        note = input("Type your note: ")  # Ask user for a note
        file.write(note + "\n")  # Write note to file with a newline
        print("Note saved!\n")  # Confirm to user

# Function to read and display all notes from the file
def read_notes():
    print("All notes:")  # Header for display
    with open("notes.txt", "r") as file:  # Open file in read mode
        for line in file:
            print(line.strip())  # Print each note, removing extra spaces/newlines

# Function to search for a keyword in the notes
def search_notes():
    keyword = input("Word to search for: ")  # Get keyword from user
    found = False  # Track if we find a match
    with open("notes.txt", "r") as file:
        for line in file:
            if keyword in line:  # If keyword is in the current note
                print("Found:", line.strip())  # Show the matching note
                found = True
    if not found:
        print("No note found with that word.")  # Let user know if nothing matched

# Main loop—keeps running until user chooses to quit
while True:
    # Show menu options each time
    print("\n1. Write note  2. Read notes  3. Search notes  4. Quit")
    choice = input("Pick an option: ")  # Get menu choice from user
    if choice == "1":
        write_note()
    elif choice == "2":
        read_notes()
    elif choice == "3":
        search_notes()
    elif choice == "4":
        break  # Exit the loop and program
    else:
        print("Invalid option.")  # Warn if menu choice isn't valid
