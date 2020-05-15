import random
import string


password =""
def choosingInterger():
    return random.choice(string.digits)


def choosingString():
    return random.choice(string.ascii_letters)


def choosingSymbols():
    return random.choice(string.punctuation)

#passlength = int(input("How long password you want:"))

for i in range(10):
    functionList = [choosingInterger, choosingString, choosingSymbols]
    password += random.choice(functionList)()
print(password)
