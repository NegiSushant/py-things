order_amount = int(input("enter the order amount: "))

delivery_fees = 0 if order_amount > 300 else 30

print(f"Delivery fees is: {delivery_fees}")
# if order_amount > 300:
#     delivery_fees = 0
# else
