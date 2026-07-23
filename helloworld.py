# Basket total with discount program

def basket_total(prices, discount=0.0):
    subtotal = sum(prices)
    return round(subtotal * (1 - discount), 2)

print(basket_total([1.35, 2.20, 0.99], discount=0.1))  # Example usage with a 10% discount

# Tip splitter program

def tip_splitter(bill, tip_percent=0.15, people=1):
    total = bill * (1 + tip_percent)
    return round(total / people, 2)

print(tip_splitter(80, tip_percent=0.15, people=4))  # Example usage with a 15% tip and 4 people and total bill of 80

# Example unit converter (from miles to kilometers)

def miles_to_km(miles):
    return round(miles * 1.60934, 2)

print(miles_to_km(10))  # Example usage with 10 miles

# Example password strength checker based on the length

def password_strength(password):
    if len(password) < 8:
        return "Weak"
    return "Strong"

print(password_strength("hello"))  # Example usage with a weak password
print(password_strength("Python123"))  # Example usage with a strong password