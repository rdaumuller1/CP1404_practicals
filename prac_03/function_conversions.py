# MENU = """C - Convert Celsius to Fahrenheit
# F - Convert Fahrenheit to Celsius
# Q - Quit"""
#
#
# def main():
#     print(MENU)
#     choice = input(">>> ").upper()
#
#     while choice != "Q":
#         if choice == "C":
#             celsius = float(input("Celsius: "))
#             fahrenheit = celsius_to_fahrenheit_conversion(celsius)
#             print("Result: {:.2f} F".format(fahrenheit))
#         elif choice == "F":
#             fahrenheit = float(input("Fahrenheit: "))
#             celsius = fahrenheit_to_celsius_conversion(fahrenheit)
#             print("Result: {:.2f} C".format(celsius))
#         else:
#             print("Invalid option")
#         print(MENU)
#         choice = input(">>> ").upper()
#     print("Thank you.")
#
#
# def celsius_to_fahrenheit_conversion(celsius):
#     return celsius * 9 / 5 + 32
#
#
# def fahrenheit_to_celsius_conversion(fahrenheit):
#     return 5 / 9 * (fahrenheit - 32)
#
#
# main()
#
#
# def main():
#     score = float(input("Enter score: "))
#     print(catergorise_score(score))
#
#
# def catergorise_score(score):
#     if score < 0 or score > 100:
#         print("Invalid Score")
#     elif score < 50:
#         print("Bad")
#     elif score < 90:
#         print("Passable")
#     else:
#         print("Excellent")
#
#
# main()
