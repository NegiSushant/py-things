# Generators: used for memory optimizations
# Syntax: iterable(expression for item in iterable if condition)
# Syntax: (expression for item in iterable if condition)
# [x for x in items]  make entire list in memory
# (x for x in items)  like a stream

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = (sale for sale in daily_sales if sale > 5)
print(total_cups) # <generator object <genexpr> at 0x000002604D648380>

total_cups = sum(sale for sale in daily_sales if sale > 5)
print(total_cups) # 61