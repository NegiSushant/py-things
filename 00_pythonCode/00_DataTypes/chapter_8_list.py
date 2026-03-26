ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar")

print(f"Ingredients are: {ingredients}")

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(chai_ingredients)

chai_ingredients.insert(2, "black tea")

print(f"chai: {chai_ingredients}")

last_added = chai_ingredients.pop()

print(f"last added: {last_added}")
print(f"chai: {chai_ingredients}")

print(f"chai: {chai_ingredients.reverse()}")
chai_ingredients.sort() # sort list

sugar_levels = [1, 2, 3, 4, 5]
print(f"Maximum sugar lavel: {max(sugar_levels)}")
print(f"Minimum sugar lavel: {min(sugar_levels)}")
