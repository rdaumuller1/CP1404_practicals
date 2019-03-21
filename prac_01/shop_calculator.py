
number_of_items = float(input("Number of Items: "))
total_price = 0
while number_of_items > 0:
        price_of_item = float(input("Price of item: "))
        total_price = total_price + price_of_item
        number_of_items = number_of_items - 1
print ("Total Price for 3 Items:", total_price)
