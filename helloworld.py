#basket total with discount program

def basket_total(prices, discount=0.0):
    subtotal = sum(prices)
    return round(subtotal * (1 - discount), 2)

print(basket_total([1.35, 2.20, 0.99], discount=0.1))  # Example usage with a 10% discount

#tip splitter program

def tip_splitter(bill, tip_percent=0.15, people=1):
    total = bill * (1 + tip_percent)
    return round(total / people, 2)

print(tip_splitter(80, tip_percent=0.15, people=4))  # Example usage with a 15% tip and 4 people and total bill of 80