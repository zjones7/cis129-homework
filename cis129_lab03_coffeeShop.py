coffee_price = 5
muffin_price = 4
tax_rate = 0.06

# user input

num_coffees = int(input("Number of coffees bought? "))
num_muffins = int(input("Number of muffins bought? "))

# subtotal

coffee_subtotal = num_coffees * coffee_price
muffin_subtotal = num_muffins * muffin_price
subtotal = coffee_subtotal + muffin_subtotal

tax = subtotal * tax_rate

total = subtotal + tax

# printing receipt

print("\n***************************************")
print("My Coffee and Muffin Shop")
print(f"Number of coffees bought?\n{num_coffees}")
print(f"Number of muffins bought?\n{num_muffins}")
print("***************************************\n")
print("***************************************")
print("My Coffee and Muffin Shop Receipt")
print(f"{num_coffees} Coffee at ${coffee_price} each: ${coffee_subtotal:.2f}")
print(f"{num_muffins} Muffins at ${muffin_price} each: ${muffin_subtotal:.2f}")
print(f"6% tax: ${tax:.2f}")
print("---------")
print(f"Total: ${total:.2f}")
print("***************************************")
