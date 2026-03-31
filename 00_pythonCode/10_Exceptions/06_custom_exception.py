class OutOfIngedientError(Exception):
    pass

def make_chai(milk, sugur):
    if milk == 0 or sugur == 0:
        raise OutOfIngedientError("Missing milk or sugar")
    print("Chai is ready...")


make_chai(0, 1)
