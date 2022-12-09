num1:int=None
num2:int=None
math:str=None
result:float=None

print("Kérek egy számot")
num1=int(input())
print("Kérek egy másik számot")
num2=int(input())
print("Kérek egy műveletet: +, -, *, /")
math=str(input())

match math:
    case "+":
        result=num1+num2
        print(f"{result}")
    case "-":
        result=num1-num2
        print(result)
    case "*":
        result=num1*num2
        print(result)
    case "/":
        result=num1/num2
        print(result)
    case _:
        print("Ilyet nem tidok számolni")