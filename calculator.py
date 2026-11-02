# Excersize 1:

price = 50
quantity = 12
revenue = price * quantity

print(f"Revenue is: ${revenue:.2f}") # thousands sep not a problem

# Excersize 2:

cost = 32
margin = (price - cost) / price # we want a float: the underlying variable never changes

print(f"Margin is: {margin:.2%}") # percentage format

#####
# Excersize 3: Compare two products
# giving numbers
# what if we need to calculate two margins

margin_a = .36
margin_b = .25

product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Excersize 4: 
price = 150 # price = 100
margin = .35 # margin = .25
is_premium = price > 100
good_margin = margin > .3

use_product_a = is_premium and good_margin

print(f"Use product: {use_product_a}")

# excersize 5:

# print(17/5) # 3.4
# print(17//5) # 3
# print(17%5) # 2 

# Excersize 7: Packing problem

# BOX_SIZE = 24 # CONSTANT DO NOT TOUCH 
#items_ordered = int(input("Number of items ordered: "))
#full_boxes = items_ordered // BOX_SIZE # floor divison
#loose_items = items_ordered % BOX_SIZE # modulus operator
#exact_fit = loose_items == 0

#print(f"Full boxes: {full_boxes}")
#print(f"Loose items: {loose_items}")
#print(f"Exact fit: {exact_fit}")

# Excersize 6: 

# stage 1: inputs 
product = input("Enter product name: ") # str
price = float(input("Enter product price: ")) # float
cost = float(input("Enter product cost: ")) # float
quantity = int(input("Enter quantity sold: ")) # int
discount = float(input("Enter discount percentage: ")) # float

# stage 2: calculations
revenue = price * quantity
discounted_revenue = revenue * (1 - discount) # DANGER
gross_margin = (price - cost) / price
net_profit = discounted_revenue - (cost * quantity)

# stage 3: outputs
print(f"Product: {product}")
print(f"Revenue: ${revenue:.2f}")
print(f"Net Revenue: ${discounted_revenue:.2f}")
print(f" Margin: {gross_margin:.2%}")
print(f"Profit: ${net_profit:.2f}")
