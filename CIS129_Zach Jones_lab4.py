# Module 4 Lab-4
# Zach Jones
# 24 Feb 2025
# A program to modify bonus portion to include different levels and types and eliminate the day off program.

# declare local variables
monthlySales = 0  # monthly sales amount
storeAmount = 0  # store bonus amount
empAmount = 0  # employee bonus amount
salesIncrease = 0  # percent of sales increase
prompt = 'Monthly sales = ' # prompt will be a string literal

# include code to get the monthly Sales

monthlySales = float(input('Monthly sales = '))

# include code to Calculate the Store Bonus

if monthlySales >= 110000:
	storeAmount = 6000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 70000:
    storeAmount = 3000
else:
    storeAmount = 0

# include code to get the Increase in Sales
salesIncrease = float(input('Enter the percentage increase in sales: '))
salesIncrease = salesIncrease / 100

# include code to Calculate the Employee Bonus

if salesIncrease >= .05:
	empAmount = 75
elif salesIncrease >= .04:
	empAmount = 50
elif salesIncrease >= .03:
	empAmount = 40
else:
	empAmount = 0

# include code to print out all the results

print("The store bonus amount is $", storeAmount)
print("The employee bonus amount is $", empAmount)
if ( storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have reached the highest bonus amounts possible! ')
