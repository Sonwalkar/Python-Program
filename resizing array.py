''' Implementation of Stack with it's basic operations i.e.
push()
pop()
isEmpty()
isFull()
resizing array means if stack full then pushing element into stack then stack's size will be multiple of 2 for eg.
if nothing in the stack then stack size is 0. if only 1 element in the stack then stack size is 2. if 5 element in
the stack then stack size is 8 and so on. stack size increase like 2,4,8,16,32,64,128,...etc.

'''
array = []
stacksize = 0
pointer = 0
def is_empty():
    if pointer == 0:
        return True


def is_full():
    if pointer == stacksize:
        return True

def push():
    global stacksize
    global pointer
    value = int(input("Enter value"))
    if stacksize == 0:
        stacksize = 2
    elif is_full():
        stacksize *= 2
    array.append(value)
    pointer += 1


def pop():

    global stacksize
    global pointer

    if is_empty():
        print("Stack Is Empty")
    else:
        array.pop()
        pointer -= 1

        if pointer == 0:
            stacksize = 0
        if stacksize > 2 :
            if pointer*2 is stacksize:
                stacksize =int(stacksize/ 2)


while True:
    choice = int(input("1.Push \n2.Pop \n3.Check for Empty \n4.Print Stack\n5.Stack Size\n"))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        if is_empty() is True:
            print("Stack is empty")
        else:
            print("Stack is Not Empty")
    elif choice == 4:
        print(array)
    elif choice == 5:
        print("Stack Size:", stacksize)
    else:
        print("INVALID OPTION")
        exit(1)