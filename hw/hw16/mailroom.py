import os
name_d = {}

MAIN_MENU = u"\n\
Choose from the following: \n\
T - Send a (T)hank you \n\
R - Create a (R)eport \n\
S - (S)ave current donor memory to a file \n\
O - (O)pen a previously saved file \n\
A - (A)dd donors from other file \n\
P - (P)rint letters for current total donation per donor \n\
quit - Quit the program \n\
> "

THANKS_MENU = u"\n\
Please enter a name or choose from the following: \n\
list - Print a list of previous donors\n\
quit - Return to main menu \n\
> "

PRINT_MENU = u"\n\
Choose from the following to print total donation for donors: \n\
A - Print (A)ll thank you letters\n\
C - (C)hoose thank you letter by entering the name\n\
quit - Return to main menu\n\
> "

PRINT_MENU2 = u"\n\
Choose from the following to print all donors' donations: \n\
A - Print (A)ll thank you letters in one file\n\
S - Print all thank you letters in (S)eparate file\n\
quit - Return to main menu\n\
> "

LETTER = u"\n\
Dear {name}, \n\
\n\
    Thank you so much for your kind donation of ${donation}. We here at the\n\
Foundation for Everyone Needs Potato Salad greatly appreciate it. You \n\
money will go towards researching the best way for everyone in the world\n\
to enjoy potato salad.\n\
\n\
Thanks again,\n\
\n\
Chong Park\n\
\n\
Director, Foundation for Everyone Needs Potato Salad\n\n\n"

FILE_WRITE = u"\nYour file has been saved to '%s'... \n\
Would you like to clear the memory of donors(Y/N)?\n\
>"

CONTINUE = u"\nPress enter to continue..."


def menu():
    os.system('clear')
    choice = input(MAIN_MENU)
    if(choice == 'T' or choice == 't'):
        thank_you_name()
    elif(choice == 'R' or choice == 'r'):
        create_report()
    elif(choice == 'S' or choice == 's'):
        write_file("dict")
    elif(choice == 'O' or choice == 'o'):
        read_file(False)
    elif(choice == 'A' or choice == 'a'):
        read_file(True)
    elif(choice == 'P' or choice == 'p'):
        print_letters()
    elif(choice == 'quit'):
        quit()


def read_file(add_to):
    """
    Reads file and uploads dictionary from the file.
    """
    global name_d
    os.system('clear')
    file_name = input(u"Please enter a file name you would like to open > ")
    try:
        if(file_name == 'quit'):
            return
        f = open('%s' % file_name, 'r')
    except IOError:
        print(u"\nFile doesn't exist")
        input(CONTINUE)
        return
    lines = f.readlines()
    test = lines.pop(0).replace('\n', '')
    # Validates if the file has a header of MAILROOM_file_name
    validation = (test == "MAILROOM_%s" % file_name)
    if(validation is False):
        print(u"\nThe file header does not match file for this program.")
        print(u"The file is not a previously saved session.")
        input(CONTINUE)
        return
    else:
        # If user had selected the regular open file, it will clear the dict
        # However, if the user chooses to add, it will keep the current dict
        #   and add information from the files.
        if(add_to is False):
            name_d = {}
        for l in lines:
            name = ""
            d = []
            items = l.split()
            for item in items:
                # If there are multiple string because user could have
                # entered first and last, or first, middle and last name
                # It will go through and add them into 'name'
                if(item.isalpha()):
                    name += item
                elif(is_number(item)):
                    d.append(float(item))
                elif(item.isnumeric()):
                    d.append(int(item))
            if(name in name_d.keys()):
                name_d[name][0] += d[0]
                name_d[name][1] += d[1]
            else:
                name_d[name] = d


def write_file(file_type, text=""):
    """
    Writes strings into a file.
    Parameter=('letter', string_of_letter) will write file of string_of_letter
    Parameter=('dict') will write a file with donor/donation info
    """
    global name_d
    os.system('clear')
    file_name = input(u"Please enter a file name you would like to save to > ")
    if(file_name == 'quit'):
            return
    f = open('%s' % file_name, 'w')
    # This will be validator for opening file. It will look for the header
    #   in the format of MAILROOM_file_name
    if(file_type == 'dict'):
        f.write('MAILROOM_%s\n' % file_name)
        for key in name_d.keys():
            row = [key, str(name_d[key][0]), str(name_d[key][1])]
            f.write('%s\n' % ' '.join(row))
        f.close()
        # This asks user if they want to clear the dictionary or keep it
        clear = input(FILE_WRITE % file_name)
        if(clear == 'Y' or clear == 'y'):
            name_d = {}
    elif(file_type == 'letter'):
        f.write(text)
        f.close()


def thank_you_menu():
    """
    This function prompts user for a name, which it validates and
    returns in .title() format.
    """
    while True:
        os.system('clear')
        name = input(THANKS_MENU)
        if(name == 'quit'):
            return 'quit'
        # If name is 'list' loop does not break nor return
        # to the main menu
        elif(name == 'list'):
            os.system('clear')
            print("List of Names")
            print("-------------")
            sorted_name = sort_by_name()
            for donor in sorted_name:
                print(donor)
            input(CONTINUE)
        elif(name.replace(' ', '').isalpha()):
            break
    return name.title()


def thank_you_name():
    """
    Executed when 'T' is entered from main menu.
    Gets a name from thank_you_menu() and it uses it
    to see if it needs to quit, or proceed with adding into dictionary
    or add donation to existing values
    """
    global name_d
    name = thank_you_menu()
    if(name == 'quit'):
        return
    # Dictionary version
    if(name not in name_d.keys()):
        name_d[name] = [0, 0]
    donation = add_donation(name)
    if(donation == 'quit'):
        return
    # Print a letter
    create_a_letter(name, donation)


def add_donation(name):
    os.system('clear')
    global name_d
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
    letter = LETTER.format(name=name, donation=donation)
    print(letter)
    # Exception check for quitting after printing the letter
    # This was added to pass the test_mailroom.py
    exception = input(CONTINUE)
    if(exception == 'quit'):
        quit()
    return letter


def print_letters():
    """
    Finds the paramter needed to write a file
    The parameter sends the type of file it will be writing which is "letter"
    and the letter itself to write.
    Choice A)
    Determines whether if letters for every donor should be printed and
        attempt to write to a file. Within sub menu, you can choose to print
        one by one, or all in one file.
    Choice C)
    Asks user for a name. Prints a letter and attempt to write to a file
    """
    global name_d
    letter_to_write = ""
    while(True):
        os.system('clear')
        choice = input(PRINT_MENU)
        if(choice == 'A' or choice == 'a'):
            os.system('clear')
            choice2 = input(PRINT_MENU2)
            if(choice2 == 'A' or choice == 'a'):
                for key in name_d.keys():
                    letter_to_write += create_a_letter(key, name_d[key][0])
                write_file('letter', letter_to_write)
                return
            elif(choice2 == 'S' or choice2 == 's'):
                for key in name_d.keys():
                    letter_to_write = create_a_letter(key, name_d[key][0])
                    write_file('letter', letter_to_write)
                return
            elif(choice2 == 'quit'):
                return
        elif(choice == 'C' or choice == 'c'):
            key = thank_you_menu()
            if(key == 'quit'):
                return
            letter_to_write = create_a_letter(key, name_d[key][0])
            write_file('letter', letter_to_write)
            return
        elif(choice == 'quit'):
            return


def create_report():
    """
    Creates report with a table
    """
    os.system('clear')
    global name_d
    sp = column_length()
    s_n = sort_by_donation()
    border = sp.pop(4) + 9
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

    col = ['Name', 'Total', '#', 'Average Donation']
    c = [sp[s].format(x) for (s, x) in enumerate(col)]
    columns = ' | '.join(c)
    print(columns)
    print("-" * border)
    for items in newlist:
        print(items)
    print("\n\n\n")
    # Exception check for quitting after printing the letter
    # This was added to pass the test_mailroom.py
    exception = input(CONTINUE)
    if(exception == 'quit'):
        quit()


def column_length():
    """
    Calculates how many spaces the columns need based on
    max number of characters for each characters. It will resize
    the column to fit any data.
    """
    # a is for name length
    # b is for total donation length which should add 2 for '$' and '.'
    # c is for number of donation
    # d or (b - c + 1) is maximum donation length if divided by smallest
    # e returns total spacing of a through d
    #   possible c.
    #   IE. 10000/10 = 1000 -> 5 - 2 + 1 = 4
    #   IE. 10000/99 = ~100 -> 5 - 2 + 1 = 4 will still space by 4 and have
    #   extra space, but will not be less space
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
    d = b - c + 1
    if(d < 17):
        d = 17
    e = a + b + c + d
    # Ran past the 80 character limit. Added lists together
    spaces = ['{:<%s}' % a, '{:>%s}' % (b + 2)]
    spaces += ['{:>%s}' % c, '{:^%s}' % d, e]
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

print('Welcome to Mailroom Madness')
while True:
    menu()
