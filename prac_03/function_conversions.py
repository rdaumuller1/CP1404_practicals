"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $"))
if sales < 1000:
    bonus = sales * 0.1
else:
    bonus = sales * 0.15
print("Bonus = ", bonus)

# number_of_items = float(input("Number of Items: "))
# total_price = 0
# while number_of_items > 0:
#         price_of_item = float(input("Price of item: "))
#         total_price = total_price + price_of_item
#         number_of_items = number_of_items - 1
# print ("Total Price for 3 Items:", total_price)
