import  random


def dice():
    value = random.randrange(1,7)
    if value==1:
        print('+--------+')
        print("|        |")
        print("|    *   |")
        print("|        |")
        print('+--------+')
    elif value==2:
        print('+--------+')
        print("| *      |")
        print("|        |")
        print("|      * |")
        print('+--------+')
    elif value==3:
        print('+--------+')
        print("| *      |")
        print("|    *   |")
        print("|      * |")
        print('+--------+')
    elif value==4:
        print('+--------+')
        print("| *    * |")
        print("|        |")
        print("| *    * |")
        print('+--------+')
    elif value==5:
        print('+--------+')
        print("| *    * |")
        print("|    *   |")
        print("| *    * |")
        print('+--------+')
    elif value==6:
        print('+--------+')
        print("| *    * |")
        print("| *    * |")
        print("| *    * |")
        print('+--------+')


dice()