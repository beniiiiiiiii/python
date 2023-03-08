def szumOfTwoNumbers(a:float, b:float)->float:
    result:float=None
    result=a+b
    return result

def differenceOfTwoNumbers(a:float, b:float)->float:
    result:float=None
    if a>b:
        result=a-b
    else:
        result=b-a
    return result

def multiplicationOfTwoNumbers(a:float, b:float)->float:
    result:float=None
    result=a*b
    return result

def divisionOfTwoNumbers(a:float, b:float)->float:
    result:float=None
    if a>b:
        result=a/b
    else:
        result=b/a
    return result
