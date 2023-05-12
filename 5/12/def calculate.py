def calculate_total(price, percent):
    total = price + percent * price
    return total
my_price = 78.55
my_tip = 20
current = calculate_total(my_price, my_tip/100)
print(current)