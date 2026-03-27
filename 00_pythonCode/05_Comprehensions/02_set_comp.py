# Syntax: {expression for item in iterable if condition}

favourite_chais = [
    "Masala Chai", "Green Tea", "Masala Chai", "Lemon Tea", "Green Tea", "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
length_chai = {chai for chai in favourite_chais if len(chai)> 10}

print(unique_chai)
print(length_chai)

recipes = {
    "Masala Chai": ["ginger", "cardamom", "clove"],
    "Elaichi Chai": ["cardamom", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = { spice for ing in recipes.values() for spice in ing}

print(unique_spices)