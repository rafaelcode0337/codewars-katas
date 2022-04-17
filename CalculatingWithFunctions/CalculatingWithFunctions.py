def zero(operation = False):
    if operation:
        return operation(0)
    else:
        return 0
    
def one(operation = False):
    if operation:
        return operation(1)
    else:
        return 1
    
def two(operation = False):
    if operation:
        return operation(2)
    else:
        return 2
    
def three(operation = False):
    if operation:
        return operation(3)
    else:
        return 3
    
def four(operation = False):
    if operation:
        return operation(4)
    else:
        return 4
    
def five(operation = False):
    if operation:
        return operation(5)
    else:
        return 5
    
def six(operation = False):
    if operation:
        return operation(6)
    else:
        return 6
    
def seven(operation = False):
    if operation:
        return operation(7)
    else:
        return 7
    
def eight(operation = False):
    if operation:
        return operation(8)
    else:
        return 8
    
def nine(operation = False):
    if operation:
        return operation(9)
    else:
        return 9

def plus(x):
    return lambda y: y + x
    
def minus(x):
    return lambda y: y - x
    
def times(x):
    return lambda y: y * x

def divided_by(x):
    return lambda y: y // x
