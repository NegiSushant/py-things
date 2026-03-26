chai_type = "Ginger chai"
customer_name = "Priya"

print(f"Oder for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}") # till 7 index
print(f"First word: {chai_description[12:]}") # start from 12
print(f"First word: {chai_description[0::-1]}") # reverse the string

lable_text = "Chain Special"
encoded_label = lable_text.encode("utf-8")
print(f"Encoded label: {lable_text}")
print(f"Encoded label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")

print(f"Decoded label: {decoded_label}")