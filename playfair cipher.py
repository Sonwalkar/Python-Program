''' Playfair Cipher Encryption'''

import math, time


t1 = time.time()
# Here creates a 5x5 matrix
def createMatrix(rowCount, colCount, dataList):
    mat = []
    for i in range(rowCount):
        rowList = []
        for j in range(colCount):
            rowList.append(dataList[rowCount * i + j])
        mat.append(rowList)

    return mat


def makeUniquelist(key, alpha):
    uniquelist=[]
    # Here only append unique letters of key
    for i in range(len(key)):
        if key[i] not in uniquelist:
            uniquelist.append(key[i])

    # Here remaining letters are added but not same
    for j in range(len(alpha)):
        if alpha[j] not in uniquelist:
            uniquelist.append(alpha[j])

    return uniquelist

def msgPair(msg):
    # Convert message string to list
    msglist = list(msg)
    #message pair list
    msgpr = []

    # If same letters paired then add 'x' befor second letter
    i=0
    for k in range(math.ceil(len(msglist) / 2)):
        if msglist[i] == msglist[i+1]:
            msglist.insert(i+1, 'x')
        i += 2

    # If message lenth is odd then add "x" at the end pair
    if len(msglist)%2 != 0:
        msglist.append('z')

    # Makes message paring
    for i in range(math.ceil(len(msglist)/2)):
        rowList = []
        for j in range(2):
            rowList.append(msglist[2 * i + j])
        msgpr.append(rowList)

    return msgpr



def getindex(matrix, column):
    indexofrow = 0
    indexofcolumn = 0
    for row in matrix:
        if column in row:
            indexofrow = matrix.index(row)
            indexofcolumn = row.index(column)

    return [indexofrow, indexofcolumn]


# Here replace pairs by to cnvert plain text to cipher text
def replacePairs(matrix, message):
    global index1
    global index0

    ciphertext = []
    for i in message:
        index0 = getindex(matrix, i[0])
        index1 = getindex(matrix, i[1])

        # If pair is in same Column
        if index0[1] == index1[1]:
            ciphertext.append(matrix[(index0[0] + 1) % 5][index0[1]])
            ciphertext.append(matrix[(index1[0] + 1) % 5][index1[1]])

        # If pair is in same row
        elif index0[0] == index1[0]:
            ciphertext.append(matrix[index0[0]][(index0[1] + 1) % 5])
            ciphertext.append(matrix[index0[0]][(index1[1] + 1) % 5])

        # If pair is not in same row or same column
        else:
            ciphertext.append(matrix[index0[0]][index1[1]])
            ciphertext.append(matrix[index1[0]][index0[1]])
        #print(matrix[index0[0]][index0[1]], matrix[index1[0]][index1[1]], "[", index0[0], index0[1], "] [", index1[0], index1[1],"]")
        #print(matrix[index0[0]][index1[1]], matrix[index1[0]][index0[1]] , "[", index0[0], index1[0], "] [", index1[0], index0[1],"]")

    return ciphertext


def main():
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    userkey = input("Enter key: ").lower()
    msg = input("Enter message: ").lower()

    # Here remove blank spaces
    userkey = userkey.replace(' ', '')
    msg = msg.replace(' ', '')

    # Replace j by i
    userkey = userkey.replace('j', 'i')

    key = list(userkey)

    # Before creating 5x5 Matrix first create unique list that contain key and alphabets
    matr = makeUniquelist(key, alpha)

    # after creating unique list now we make 5x5 matrix
    matrix = createMatrix(5, 5, matr)
    print("5x5 Key matrix:")
    for i in matrix:
        print(i)

    # Message pairing
    message = msgPair(msg)
    print("\nKey pairs: ")
    print(message)

    # Now Replace original message to cipher text
    ciphertext = ''.join(replacePairs(matrix, message))

    print("\nCiphertext: ", ciphertext)


main()

t2 = time.time()
print("Execution time: ", t2-t1)
