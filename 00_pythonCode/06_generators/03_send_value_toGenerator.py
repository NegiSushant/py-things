# yield generates the data as well as send the data to it

def chai_customer():
    print("Welcome! What chai would you like?")
    order = yield

    while True:
        print(f"Preparing: {order}")
        order = yield

stall = chai_customer()
next(stall) # start the generator

stall.send("Masala Chai!")
stall.send("Leamon Chai!")