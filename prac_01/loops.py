# a
# for i in range(0, 101, 10):
#         print(i, end =' ')
# print()


# b
# for i in range(20, 0, -1):
#     print(i, end = ' ')
# print()


# c
# number_of_stars = int(input("Number of stars: "))
# for number_of_stars in range(number_of_stars):
#     print("*", end = '')


# d
number_of_stars = int(input("Number of stars: "))
for number_of_stars in range(number_of_stars):
    while number_of_stars > 0:
        print("*", end='')
        number_of_stars = number_of_stars - 1


# e
# sales = float(input("Enter sales: $"))
# while sales >= 0:
#     if sales < 1000:
#         bonus = sales * 0.1
#     else:
#         bonus = sales * 0.15
#     print("Bonus = ", bonus)
#     sales = float(input("Enter sales: $"))
