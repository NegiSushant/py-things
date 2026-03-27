# Syntax: [expression loop if condition]
# [expression for item in iterable if condition]
# [tea for tea in menu if "Iced" in tea]

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger chai"
]

iced_item = [tea for tea in menu if "Iced" in tea]

print(iced_item)