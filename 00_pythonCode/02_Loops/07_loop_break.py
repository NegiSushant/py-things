flavours = ["Ginger", "out of Stock", "Lemon", "Discontinue", "Tulsi"]

for flavour in flavours:
    if flavour == "out of Stock":
        continue
    if flavour == "Discontinue":
        break
    print("Discontinued item found")

print(f"Out side of loop")
