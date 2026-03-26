# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams

print(f"Total gram of base tea is: {total_grams}")


remainh_tea = black_tea_grams - ginger_grams

print(f"Total gram of remaining tea is: {remainh_tea}")

milk_liter = 7
servings = 4

milk_per_serving = milk_liter / servings
print(f"Milk per serving is {milk_per_serving}")

total_tea_bags = 7

pots = 4
bags_per_pot = total_tea_bags // pots
print(f"While tea bags per pot: {bags_per_pot}")


total_cadamom_pods = 10
pods_per_cup = 3

leftover_pods = total_cadamom_pods / pods_per_cup
print(f"Leftover C pods {leftover_pods}")

base_flavor_strength = 2
scale_factor = 3

powerfull_flavour = base_flavor_strength ** scale_factor
print(f"Scaled flavour strength {powerfull_flavour}")


is_boiling = True #True = 1 & false = 0
stri_count = 5
total_action = stri_count + is_boiling
print(f"Total actions: {total_action}")

milk_present = 0 # no milk
print(f"Is there milk? {bool(milk_liter)}")

# logical operations
water_hot = True
tea_added = False

can_serve = water_hot and tea_added
print(f"Can serve chai? {can_serve}")

