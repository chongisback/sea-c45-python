import os
donors = []
name_d = {}

MAIN_MENU = u"\n\
Choose from the following: \n\
T - Send a (T)hank you \n\
R - Create a (R)eport \n\
quit - Quit the program \n\
> "

THANKS_MENU = u"\n\
Please enter a name or choose from the following: \n\
list - Print a list of previous donors\n\
quit - Return to main menu \n\
> "

LETTER = u"\n\
Dear %s, \n\
\n\
    Thank you so much for your kind donation of $%.2f. We here at the\n\
Foundation for Everyone Needs Potato Salad greatly appreciate it. You \n\
money will go towards researching the best way for everyone in the world\n\
to enjoy potato salad.\n\
\n\
Thanks again,\n\
\n\
Chong Park\n\
\n\
Director, Foundation for Everyone Needs Potato Salad\n\n\n"


def menu():
    global donors
    os.system('clear')
    choice = input(MAIN_MENU)
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
        name = input(THANKS_MENU)
        if(name == 'quit'):
            return
        # If name is 'list' loop does not break nor return
        # to the main menu
        elif(name == 'list'):
            os.system('clear')
            print("List of Names")
            print("-------------")
            sorted_name = sort_by_name()
            for donor in sorted_name:
                print(donor)
            input(u"\nPress enter to continue...")
        elif(name.replace(' ', '').isalpha()):
            break
    # If the loop breaks, name is neither 'quit' or 'list'
    name = name.title()
    # Dictionary version
    if(name not in name_d.keys()):
        name_d[name] = [0, 0]
    donation = add_donation_d(name)
    if(donation == 'quit'):
        return
    # Print a letter
    create_a_letter(name, donation)


def add_donation_d(name):
    os.system('clear')
    global donors
    while True:
        amount = input(u"\nPlease enter the donation amount or 'quit': ")
        if(amount == 'quit'):
            return amount
        elif(is_number(amount)):
            # amount is rounded to 2 decimal place
            amount = float("{0:.2f}".format(float(amount)))
            name_d[name][0] += amount
            name_d[name][1] += 1
            return amount


def create_a_letter(name, donation):
    """
    This function prints a "Thank you" letter
    """
    os.system('clear')
    print(LETTER % (name, donation))
    # Exception check for quitting after printing the letter
    # This was added to pass the test_mailroom.py
    exception = input("Press Enter to continue....")
    if(exception == 'quit'):
        quit()


def contains_index(name):
    """
    Returns True, and index, if name is contained in the donors list.
    Returns False, and last index if name is not contained in the donors list
    """
    global donors
    contains = False
    index = 0
    for donor in donors:
        if(donor[0] == name):
            contains = True
            break
        index += 1
    print([contains, index])
    return [contains, index]


def create_report():
    os.system('clear')
    global name_d
    sp = column_length()
    s_n = sort_by_donation()
    print (s_n)
    # newlist will hold the string values for each row of donor information
    newlist = []
    for x in s_n:
        # avg is calculated by total donation / # of donation
        # it will get float with 2 decimal values
        avg = '%.2f' % (float(name_d[x][0]) / name_d[x][1])
        # row holds list of each items of donor info.
        # row = [name, total, # donation, avg]
        row = [x, '$%.2f' % name_d[x][0], str(name_d[x][1]), '$%s' % str(avg)]
        # Below is tabbing for correct tab space depends on length of the name
        # or donation amount. Max char per name and total donation
        # is 16. It will only account for that much tabbing at the moment
        row_i = [sp[s].format(x) for (s, x) in enumerate(row)]
        row_items = ' | '.join(row_i)
        newlist.append(row_items)

    col = ["Name", "Total", "#", "Average Donation"]
    c = [sp[s].format(x) for (s, x) in enumerate(col)]
    columns = ' | '.join(c)
    print(columns)
    print("-----------------------------------------------------------")
    for items in newlist:
        print(items)
    print("\n\n\n")
    # Exception check for quitting after printing the letter
    # This was added to pass the test_mailroom.py
    exception = input("Press Enter to continue....")
    if(exception == 'quit'):
        quit()


def column_length():
    """
    Calculates how many spaces the columns need based on
    max number of characters for each characters. It will resize
    the column to fit any data.
    """
    global name_d
    a, b, c = 0, 0, 0
    for name in name_d.keys():
        if(len(name) > a):
            a = len(name)
        if(len(str(name_d[name][0])) > b):
            b = len(str(name_d[name][0]))
        if(len(str(name_d[name][1])) > c):
            c = len(str(name_d[name][1]))
    # default values for the table column
    if(a < 4):
        a = 4
    if(b < 5):
        b = 5
    if(c < 1):
        c = 1
    # Ran past the 80 character limit. Added lists together
    spaces = ['{:<%s}' % a, '{:>%s}' % (b + 2)]
    spaces += ['{:>%s}' % c, '{:^%s}' % (b - c + 1)]
    return spaces


def sort_by_donation():
    """
    Returns a list of name based on total donation amount.
    """
    global name_d
    # s_l is short hand for sorted_list
    # d is short hand for single donor in donors
    # s_i is short hand for sorted index
    s_l = []
    s_d = []
    for k in name_d.keys():
        # d is short hand for sorted_list
        if(len(s_d) == 0):
            sorted_i = 0
        else:
            # current d's total donation is greater than the 1st value in
            # sorted_list's total donation
            if(name_d[k][0] >= s_d[0]):
                sorted_i = 0
            # current d's total donation is less than the last value in
            # sorted_list's total donation
            elif(name_d[k][0] < s_d[0]):
                sorted_i = len(s_d)
            # otherwise, look for index where d's total donation can squeen
            # in between
            else:
                i = 0
                while (i < len(s_d) - 1):
                    if(s_d[i] <= name_d[k][0] and
                            s_d[i + 1][0] > name_d[k][0]):
                        sorted_i = i + 1
                        break
                    i += 1
        s_d.insert(sorted_i, name_d[k][0])
        s_l.insert(sorted_i, k)
    return s_l


def sort_by_name():
    """
    Sorts donors list to a new list in alphabetical order of the name
    This sorting algorithm uses insertion method.
    """
    # s_l is short hand for sorted_list
    # d is short hand for single donor in donors
    # s_i is short hand for sorted index
    global name_d
    s_l = []
    for key in name_d.keys():
        if(len(s_l) == 0):
            sorted_i = 0
        else:
            # current d's name is less than the 1st value in
            # sorted_list's name
            if(key < s_l[0]):
                sorted_i = 0
            # current d's name is bigger than the last value in
            # sorted_list's name
            elif(key > s_l[-1]):
                sorted_i = len(s_l)
            # otherwise, look for index where d's name can squeeze
            # in between
            else:
                i = 0
                while(i < len(s_l) - 1):
                    if(s_l[i] < key and s_l[i + 1] > key):
                        sorted_i = i + 1
                        break
                    i += 1
        s_l.insert(sorted_i, key)
    return s_l


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
