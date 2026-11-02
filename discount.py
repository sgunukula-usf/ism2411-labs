# Exercise 1:
total = float(input("Enter cart total: $"))
# Add your if/elif/else here

if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.1
elif total >= 100:
    discount = 0.1
else:
    discount = 0
        
# will replace with correct logic soon
# final = total * (1 - discount)


# Exercise 3:

region = "South"
extra_discount = 0
if region == "South" and total > 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final_discount = discount + extra_discount
final = total * (1 - final_discount) 

print(f"Discount: {discount:.1%}")
print(f"Final price: ${final:,.2f}")

# Exercise 2:

if final > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")
customer_type = "whole_sale"
# Exercise 4:
 # customer_type = "whole_sale"
# if region == "South" 
#    if total > 100:
#       if customer_type == "whole_sale":
#           extra_discount = 0.03
            
if region == "South" and total > 100 and customer_type == "whole_sale":
    extra_discount = 0.03

# Exercise 5:

amount = -50

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE")    

# Exercise 6:

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False

qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_order = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_order) and not has_outstanding_balance

print(f"VIP upgrade: {vip_upgrade}")