import os
donors = []


def menu():
    os.system('clear')
    choice = input("\n\
Choose from the following: \n\
T - Send a (T)hank you \n\
R - Create a (R)eport \n\
quit - Quit the program \n\
> ")
    if(choice == 'T' or choice == 't'):
        thank_you_name()
    elif(choice == 'R' or choice == 'r'):
        create_report()
    elif(choice == 'quit'):
        quit()


def thank_you_name():
    """Executed when 'T' is used in the menu function.
    This function prompts user for a name in which user can provide
    quit command to go back to the main menu, list all the donors, or
    a name to send a thank you letter. When a name is entered it will
    ask for donation and prints a letter."""
    global donors
    while True:
        os.system('clear')
        name = input(u"\n\
Please enter a name or choose from the following: \n\
list - Print a list of previous donors\n\
quit - Return to main menu \n\
> ")
        if(name == 'quit'):
            return
        # If name is 'list' loop does not break nor return
        # to the main menu
        elif(name == 'list'):
            os.system('clear')
            print("List of Names")
            print("-------------")
            for donor in donors:
                print(donor[0])
            input(u"\nPress enter to continue...")
        elif(name.replace(' ', '').isalpha()):
            break
    # If the loop breaks, name is neither 'quit' or 'list'
    name = name.title()
    contains_and_index = contains_index(name)
    contains, index = contains_and_index[0], contains_and_index[1]
    if(not contains):
        donors.append([name, 0, 0])
    donation = add_donation(index)
    if(donation == 'quit'):
        return
    create_a_letter(name, donation)


def add_donation(index):
    """
    This function adds donation to the donor list
    """
    os.system('clear')
    global donors
    while True:
        amount = input(u"\nPlease enter the donation amount or 'quit': ")
        if(amount == 'quit'):
            return amount
        elif(is_number(amount)):
            amount = float("{0:.2f}".format(float(amount)))
            donors[index][1] += amount
            donors[index][2] += 1
            return amount


def create_a_letter(name, donation):
    """
    This function prints a "Thank you" letter
    """
    os.system('clear')
    print(u"\n\
Dear %s, \n\
\n\
    Thank you so much for your kind donation of $%s. We here at the\n\
Foundation for Everyone Needs Potato Salad greatly appreciate it. You \n\
money will go towards researching the best way for everyone in the world\n\
to enjoy potato salad.\n\
\n\
Thanks again,\n\
\n\
Chong Park\n\
\n\
Director, Foundation for Everyone Needs Potato Salad" % (name, donation))
    input(u"Press enter to continue...")


def contains_index(name):
    """
    Returns True, and index, if name is contained in the donors list.
    Returns False if name is not contained in the donors list
    """
    global donors
    contains = False
    index = -1
    for donor in donors:
        index += 1
        print (donor[0])
        print (name)
        if(donor[0] == name):
            contains = True
    print([contains, index])
    return [contains, index]

"""
def alpha_add(name):
    # Alphabetically add to the list:
    # If donors list is empty, index is 0
    # If donors 0th name is greater than new name, index is 0
    # If donors last name is less than new name, index is len(donor)
    #    which is 1 spot greater than the last index of the list
    # If none of this apply, it will find a spot inbetween two names
    global donors
    if(len(donors) == 0):
        sort_i = 0
    elif(donors[0][0] > name):
        sort_i = 0
    elif(donors[-1][0] < name):
        sort_i = len(donors)
    else:
        i = 0
        while(i < len(donors)):
            if(donors[i][0] < name and donors[i + 1][0] > name):
                sort_i = i + 1
                break
            i += 1
    donors.insert(sort_i, [name, 0, 0])
    return sort_i
"""


def create_report():
    tablelist = create_list_for_table()
    tabletopics = ["Name", "Total", "#", "Average Donation"]
    tableheader = "\t|".join(tabletopics)
    print (tableheader)
    print("-----------------------------------------------------")
    for items in tablelist:
        print(items)
    # prompt_for_enter
    input("Press enter to continue...")


def create_list_for_table():
    global donors
    newlist = []
    for row_items in donors:
        newlist.append("\t|".join([row_items[0], str(row_items[1]), str(row_items[2])]))
    return newlist


def is_number(n):
    """
    Returns true if given string n is a float number
    Ex. If n="12.34" it will return True
    """
    try:
        float(n)
        return True
    except ValueError:
        return False

print("Welcome to Mailroom Madness")
while True:
    menu()
