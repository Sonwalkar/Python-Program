import random


def shuffle():

    shuffle_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(len(shuffle_list)):
        no = random.randint(0, i)
        shuffle_list[i], shuffle_list[no] = shuffle_list[no], shuffle_list[i]

    print(*shuffle_list)


shuffle()
