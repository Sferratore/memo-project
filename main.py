from MemoBlock import *

"""This application works as a memo that stores the tasks you write on it. 
It has 3 main functions, \"show\", \"insert\" and \"delete\".
 At its closing, the application stores all your information in a file named \"memodatabase.txt\". """




choice = 0
mb = MemoBlock("MainMemo")                #Initialization

try:
    start_file = open("memodatabase.txt", 'r')
    file_content = start_file.readlines()
    for elem in file_content:
        data_in_elem = elem.split(" ")
        print(data_in_elem)
        date_information = data_in_elem[1].split("-")
        print(date_information)
        day = int(date_information[2])
        month = int(date_information[1])
        year = int(date_information[0])
        descr = data_in_elem[2]
        mb.addMemo(Memo(year, month, day, descr))
except FileNotFoundError as fxe:
    print("\nFirst start of the application\n")



while choice != 9:     #Choice cycle

    try:
        choice = int(input(("\nChoose a task.\n1.Look at the memos\n2.Insert a new memo\n3.Remove a memo\n9.Exit\n>>")))
        if choice == 1:  #"show" function
            print(mb)
        elif choice == 2: #"store" function
            mb.addMemo(Memo(int(input("Year: ")), int(input("Month: ")), int(input("Day: ")), input("Insert description: ")))
        elif choice == 3:
            mb.removeMemo(int(input("Memo ID: ")))
        elif choice == 9:
            f = open('memodatabase.txt', 'w')
            f.write(repr(mb))
            f.close()
            break

    except Exception as err:        #Exceptions handling
        print("An Exception occurred! Description= {}\n".format(err))
        continue














