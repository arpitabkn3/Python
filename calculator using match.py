num1=int(input("enter the number"))
num2=int(input("enter the number"))
op=int(input("enter the op"))
match op:
    case "+":
        print("addition",nume1+num2)
        case "-":
            print("subtraction",num1-num2)
            case "*":
                print("multiplication",num1*num2)
                case "/":
                    print("division",num1/num2)
                    print("invalid operator")
