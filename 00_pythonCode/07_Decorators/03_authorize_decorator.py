from functools import wraps

def require_admin(funcs):
    @wraps(funcs)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: Admins only!")
            return None
        else:
            return funcs(user_role)
    return wrapper

@require_admin
def acess_tea_invetory(role):
    print("Access granted to tea inventory!")

acess_tea_invetory("user")
acess_tea_invetory("admin")