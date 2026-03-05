"""
Reception Guest Manager
keeps track of dinner guests and generates invitations.
"""

# Data
guests = [] # Stores the names of all invited dinner guests

def format_name(name: str) -> str:  # This function cleans up the user's input and removes extra spaces
    return name.strip().title()

def get_valid_name(prompt: str) -> str: #This function gets a name from the user.
   
    while True:
        name = input(prompt).strip()

        # If the user enters nothing, reject it
        if name == "":
            print("Name cannot be empty.")
        else:
        return format_name(name)  

        # Return the cleaned and formatted name
        return format_name(name)

def add_guest(): #Prevents duplicate names
    
    name = get_valid_name("Enter guest name: ")

    if name in guests:
        print("Duplicate names are not allowed.")
        return

    # Append adds the new guest to the end of the list
    guests.append(name)
    print(f"{name} added.")


def modify_guest(): #Allows the user to change an existing guest's name.
    
    if not guests:
        print("Guest list is empty.")
        return

   name = get_valid_name("Enter guest name to remove: ")

    # Check if the guest exists
    if name in guests:
        index = guests.index(name)
        guests.pop(index)
        # pop(index) removes the item at that position
        print(" Guest removed.")
    else:
        print(" Guest not found.")


def sort_guests():
    """
    Sorts the guest list alphabetically.
    This makes invitations easier to read.
    """
    guests.sort()
    print(" Guests sorted alphabetically.")


def show_count():
    """
    Displays how many guests are currently invited.
    len(list) counts the number of items in the list.
    """
    print(f" Total guests: {len(guests)}")
