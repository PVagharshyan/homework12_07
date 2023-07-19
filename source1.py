check = False

class AuthenticationError(Exception):
    pass

class InputError(Exception):
    pass

flag = True
while flag:
    try:
        check = eval(input("Is logged in(True or False):"))
        if(type(check) == bool):
            flag = False
        else:
            raise InputError("Incorrect booking!")
    except InputError as err:
        print(str(err))
        flag = True
    except NameError as err:
        print("Incorrect booking!")
        flag = True

def loged():
    return check

def authentication(func):
    def wrapper(*args, **kwargs):
        if loged():
            return func(*args, **kwargs)
        else:
            raise AuthenticationError("Sorry, but you are not logged in yet")
    return wrapper

@authentication

def func():
    print("the user is already logged in to the network")

try:
    func()
except AuthenticationError as err:
    print(str(err))
