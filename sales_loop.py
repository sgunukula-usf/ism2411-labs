# Excersize 1: A Running Total

sales = [120 , 80 , 250 , 175 , 90 , 410 , 60 , 215]
total = 0     #initialize 
for sale in sales:
    total += sale   #update
print(f"Total: ${total}")

# Excersize 2: Total, count, and average

total = 0
count = 0
for sale in sales:
    total += sale
    count += 1

average = total / count
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${average:.2f}")

# Excersize 3: The largest value so far

current_max = 0  # or sales [0], to be safe with negetive numbers
for sale in sales:
    if sale > current_max:
        current_max = sale

print(f"Largest sale: ${current_max}")

# Excersize 4: Count only qualifying sales

count_over_100  = 0 
total_over_100 = 0
for sale in sales:
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale

print(f"Sales over $100: {count_over_100}")
print(f"Total of sales: ${total_over_100}")

# Excersize 5: Skip or stop

for sale in sales:
    if sale < 400:
        print(f"Alert:410 outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
print(f"${sale}")

# Excersize 6: Manage the index explicitly

total = 0
i = 0       #index
while i < len(sales):
    total += sales[i]
    i += 1

print(f"Total (while loop): ${total}")

# Excersize 7: Select the discount tier

for sale in sales:
    if sale < 200:
        discount = 0.10
    elif sale < 100:
        discount = 0.05
    else:
        discount = 0

# still inside: for sale in sales 
discounted_price = sale * (1 - discount)
print(
    f"${sale} -> ${discount*100:.0f}% discount -> "
    f"${discounted_price:.2f}"
)