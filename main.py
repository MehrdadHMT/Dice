import random


def random_number():
    return random.randint(1, 6)


def roll_dice():
    x = random_number()
    return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flag = False
    while not flag:
        print('*' * 50)
        print("Wanna 'play' or 'Quit' the game?!")
        ch = int(input("1. Roll a dice\n2. Quit\n.>"))

        if ch == 1:
            x = roll_dice()
            print(x)
        elif ch == 2:
            emoji = "\U0001F614"
            print(emoji * 30)
            flag = True
            break
        else:
            print("Please enter '1' to play agein or enter '2' to quit the game !!!")
            continue
