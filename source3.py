class IsNotString(Exception):
    pass
def decorator(func):
    def wraper(*args, **kwargs):
        for i in args:
            if type(i) != str:
                raise IsNotString("There is a non-text argument in the ordered argument construct!") 
    return wraper

@decorator
def func(a, b):
    pass

try:
    func(1, "Paylak Vagharshyan")
except IsNotString as err:
    print(str(err))
else:
    print("Constraints are met")

