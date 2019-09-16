dictonary={}
quit=True
while quit:
    print('A)ADD\tD)DELETE\tF)FIND\tQ)QUIT')
    choice = str(input())
    if 'a' == choice or 'A' == choice:
        name = str(input('ENTER NAME :')).upper()
        print('ENTER NUMBER OF ', name.upper(), end=':')
        number=int(input())
        dictonary[name] = number
    elif 'D' == choice.upper():
        dname = str(input('ENTER NAME YOU WANT TO DELETE')).upper()
        del dictonary[dname]
    elif 'F' == choice.upper():
        fname = str(input('ENTER FIND NAME')).upper()
        if fname in dictonary:
            print(dictonary[fname])
        if fname not in dictonary:
            print('NOT FOUND')
    elif 'Q' == choice.upper():
        quit = False
    elif choice == 'dump':
        print(dictonary)
    else:
        print('INVALID OPTION')
