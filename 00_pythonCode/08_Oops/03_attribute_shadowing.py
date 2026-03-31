class Chai:
    temperature = "hot"
    strength = "Strong"


cutting = Chai()

print(cutting.temperature)

cutting.temperature = "Mild"
cutting.cup = "small"

print("After changing: ", cutting.temperature)
print("Cup size: ", cutting.cup)
print("Direct look into the class: ", Chai.temperature)

del cutting.temperature
print(cutting.temperature) # hot attribute shadowing

del cutting.cup
print(cutting.cup) # AttributeError: 'Chai' object has no attribute 'cup'

