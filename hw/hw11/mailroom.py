import os
donors = []


def menu():
    global donors
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
            sorted_name = sort_by_name()
            for donor in sorted_name:
                print(donor[0])
            input(u"\nPress enter to continue...")
        elif(name.replace(' ', '').isalpha()):
            break
    # If the loop breaks, name is neither 'quit' or 'list'
    name = name.title()
    # Uses name to check for contain boolean and uses it with index
    contains_and_index = contains_index(name)
    contains, index = contains_and_index[0], contains_and_index[1]
    if(not contains):
        donors.append([name, 0, 0])
    # Add donation
    donation = add_donation(index)
    if(donation == 'quit'):
        return
    # Print a letter
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
            # amount is rounded to 2 decimal place
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
    Thank you so much for your kind donation of $%.2f. We here at the\n\
Foundation for Everyone Needs Potato Salad greatly appreciate it. You \n\
money will go towards researching the best way for everyone in the world\n\
to enjoy potato salad.\n\
\n\
Thanks again,\n\
\n\
Chong Park\n\
\n\
Director, Foundation for Everyone Needs Potato Salad\n\n\n" % (name, donation))
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
    """
    Executed when R is pressed in the main menu.
    It creates a report in table format.
    Items on the columns are joined by tabs to create a tabular
    table. The tab-ing is determined by the length of variable in the
    column.
    Format follows:
    Name            |Total           |#       |Average Donation
    -----------------------------------------------------------
    1234567890123456|1234567890123456|12345678|12345....
    Example Name    |1000.00         |2       |500.00
    where number is how many spaces are in each column
    """
    os.system('clear')
    global donors
    # Using variable tab and tab2 as tabs for spacing
    tab = "\t|"
    tab2 = "\t\t|"
    s_l = sort_by_donation()
    # newlist will hold the string values for each row of donor information
    newlist = []
    for x in s_l:
        # avg is calculated by total donation / # of donation
        # it will get float with 2 decimal values
        avg = '%.2f' % (float(x[1]) / x[2])
        # row holds list of each items of donor info.
        # row = [name, total, # donation, avg]
        row = [x[0], '%.2f' % x[1], str(x[2]), str(avg)]
        # Below is tabbing for correct tab space depends on length of the name
        # or donation amount. Max char per name and total donation
        # is 16. It will only account for that much tabbing at the moment
        if(len(row[0]) > 7):
            r_i = [(tab).join(row[:2]), (tab).join(row[2:])]
        else:
            r_i = [(tab2).join(row[:2]), (tab).join(row[2:])]
        if(len(row[1]) >= 7):
            row_items = (tab).join(r_i)
        else:
            row_items = (tab2).join(r_i)
        newlist.append(row_items)

    col = ["Name", "Total", "#", "Average Donation"]
    subtopic = [(tab2).join(col[:2]), (tab).join(col[2:])]
    columns = (tab2).join(subtopic)
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


def sort_by_donation():
    """
    Sorts donors list to a new list in order of most to least donation
    This sorting algorithm uses insertion method.
    """
    global donors
    # s_l is short hand for sorted_list
    # d is short hand for single donor in donors
    # s_i is short hand for sorted index
    s_l = []
    for d in donors:
        # d is short hand for sorted_list
        if(len(s_l) == 0):
            sorted_i = 0
        else:
            # current d's total donation is greater than the 1st value in
            # sorted_list's total donation
            if(d[1] >= s_l[0][1]):
                sorted_i = 0
            # current d's total donation is less than the last value in
            # sorted_list's total donation
            elif(d[1] < s_l[-1][1]):
                sorted_i = len(s_l)
            # otherwise, look for index where d's total donation can squeen
            # in between
            else:
                i = 0
                while (i < len(s_l) - 1):
                    if(s_l[i][1] <= d[1] and s_l[i + 1][1] > d[1]):
                        sorted_i = i + 1
                        break
                    i += 1
        s_l.insert(sorted_i, d)
    return s_l


def sort_by_name():
    """
    Sorts donors list to a new list in alphabetical order of the name
    This sorting algorithm uses insertion method.
    """
    # s_l is short hand for sorted_list
    # d is short hand for single donor in donors
    # s_i is short hand for sorted index
    global donors
    s_l = []
    for d in donors:
        if(len(s_l) == 0):
            sorted_i = 0
        else:
            # current d's name is less than the 1st value in
            # sorted_list's name
            if(d[0] < s_l[0][0]):
                sorted_i = 0
            # current d's name is bigger than the last value in
            # sorted_list's name
            elif(d[0] > s_l[-1][0]):
                sorted_i = len(s_l)
            # otherwise, look for index where d's name can squeeze
            # in between
            else:
                i = 0
                while(i < len(s_l) - 1):
                    if(s_l[i][0] < d[0] and s_l[i + 1][0] > d[0]):
                        sorted_i = i + 1
                        break
                    i += 1
        s_l.insert(sorted_i, d)
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
