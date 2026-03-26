chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai Order: {chai_order}")

chai_recipe = {} # another way to create dictionary
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Recipe base: {chai_recipe['base']}")

del chai_recipe['liquid']
print(f"Recipe: {chai_recipe}")

# membership testing
print(f"Is sugur in the order? {'sugar' in chai_order}")

chai_order = {"type": "Ginger Chai", "size":"Midium", "Sugar": 1}
print(f"Order details (keys): {chai_order.keys()}")
print(f"Order details (values): {chai_order.values()}")
print(f"Order details (item): {chai_order.items()}")


last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")

extra_spices = {"cardamom": "crushed", "ginger": 'slices'}

chai_recipe.update(extra_spices)

print(f"Updated chai recipe: {chai_recipe}")

# chai_size = chai_order["size"]
customer_note = chai_order.get("note", "No Note")
print(f"chai size is: {customer_note}")