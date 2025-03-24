def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    if(n2!=0):
        return n1/n2
    else:
        return "Division by zero is invalid"

calc={
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    num1=float(input("Enter the first number: "))

    should_accumulate=True
    while should_accumulate:
        operation=input("Choose an operation to perform:\n+\n-\n*\n/\n")
        num2=float(input("Enter the second number: "))
        answer=calc[operation](num1,num2)
        print(f"{num1} {operation} {num2} = {answer}")
        choice=input('Type "y" to continue calculation or "n" to start new \n')
        if choice=="y":
            num1=answer
        else:
            should_accumulate=False
            calculator()

calculator()
