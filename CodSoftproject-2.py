def calculator():

    firstNum =0
    secondNum = 0
    function = ""


    while True:
        try:
            firstNum = float(input("Please provide a number:"))
            break
        except:
            print("Invalid input.Please try again.")

            
    while True:
        try:
            function = input("Please choose an operator(+,-,/,*):")
            if (function in ['+','-','/','*']):
                break
        except:
            print("Invalid input.Please try again.")

    while True:
        try:
            secondNum = float(input("Please provide a number:"))
            break
        except:
            print("Invalid input.Please try again.")


    if(function == "+"):
        result = firstNum + secondNum
    elif(function == "-"):
        result = firstNum - secondNum
    elif(function == "/"):
        result = firstNum / secondNum
    elif(function == "*"):
        result = firstNum * secondNum
    else:
        result = "Invalid operator"

    print("Your result is", result)
    print("\n")
    
    
            
            
if __name__=="__main__":
    while True:
        calculator()
