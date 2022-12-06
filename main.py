import random
import time
import emoji


def printone():
    print("\nyou rolled a", random.randint(1, 6), "🥳","\n")


def printtwo():
    print("\nyou rolled a", random.randint(2, 12), "🥳", "\n")


def menu(count):
    print(emoji.emojize(':video_game: '), end='')
    print('How many', emoji.emojize(':game_die:') + ' would you like to roll', emoji.emojize(':video_game:'), "\n 1) one \n 2) two \n 3) quit")
    i = int(input('\n > '))

    if i == 1:
        printone()
        return 0
    if i == 2:
        printtwo()
        return 0
    if i == 3:
        count += 1
        return count
    else:
        print("enter a valid input please!")


count = 0
a = 0

while a < 2:
    if count != 0:
        print(" Quitting", end='')
        for i in range(3):
            time.sleep(.4)
            print(".", end='')
        print("☹")
        time.sleep(2)
        exit()
    count = menu(count)
