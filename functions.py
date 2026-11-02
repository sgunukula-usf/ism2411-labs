# Excersize 1

# Define calculate tax function 

def calculate_tax(price, rate):
    return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax for $250 at 8%: ${tax2:.2f}") #20.00
print(f"Another Tax: ${calculate_tax(150, 0.05):.2f}") # 7.50

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

# calling the function

price = 200
tier = ["gold", "silver", "bronze", "none"]

for t in tier:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# Exercise 3

# write it out manually first, then refactor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${after_tax:.2f}")
print(f"After tax: ${after_tax:.2f}")

# refactor into a function

def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax


print(f"Final price after gold discount and tax: ${final_price(200, 'gold', 0.07):.2f}")

# Exercise 4

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    final = final_price(price, tier, 0.07)
    print(f"Final price for ${price} with {tier} discount: ${final:.2f}")

# Exercise 6

x = 100 # apple

def double_it():
    x = 999 # another apple
    return x * 2

print(x)
print(double_it())
print(x)
