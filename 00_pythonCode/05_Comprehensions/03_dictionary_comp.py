# Syntax: {expression for item in iterable if condition}
# expression = {key: value}

tea_price_inr = {
        "Masala Chai": 40,
        "Green Tea":50,
        "Leamon Tea": 200
    }

tea_prices_usd = { tea: price / 90 for tea, price in tea_price_inr.items()}

print(tea_prices_usd)