import random

NUMBERS_ON_LINE = 6


def main():
    number_quick_picks = int(input("How many quick picks?"))
    while number_quick_picks < 0:
        print("Please enter a number greater than 0")
        number_quick_picks = int(input("How many quick picks?"))

    for i in range(number_quick_picks):
        quick_pick = []
        for j in range(NUMBERS_ON_LINE):
            number = random.randint(1, 45)
            while number in quick_pick:
                number = random.randint(1, 45)
            quick_pick.append(number)
        quick_pick.sort()
        # the following uses a generator expression (like a list comprehension)
        # to format each number in quick_pick in the same way
        # this is then turned into a single string with the join method
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()
