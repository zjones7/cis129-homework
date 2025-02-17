coffee_price = 5
muffin_price = 4
cookie_price = 3
tea_price = 2
tax_rate = 0.06

# user input

num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))
num_cookies = int(input("Number of cookies bought? "))
num_teas = int(input("Number of teas bought? "))

# subtotal

coffee_subtotal = num_coffees * coffee_price
muffin_subtotal = num_muffins * muffin_price
cookie_subtotal = num_cookies * cookie_price
tea_subtotal = num_teas * tea_price
subtotal = coffee_subtotal + muffin_subtotal

tax = subtotal * tax_rate

total = subtotal + tax

# printing receipt

print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{num_coffees}")
print(f"Number of muffins bought?\n{num_muffins}")
print(f"Number of cookies bought? {num_cookies}")
print(f"Number of teas bought? {num_teas}")
print("***************************************\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price} each: ${coffee_subtotal:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${muffin_subtotal:.2f}")
print(f"{num_cookies} Cookies at ${cookie_price} each: ${cookie_subtotal:.2f}")
print(f"{num_teas} Tea at ${tea_price} each: ${tea_subtotal:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Your total is: ${total:.2f}, Thank you for shopping with us today!")
print("***************************************")
