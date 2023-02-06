from art import *
import logo

def main():
    print(logo.cal)

    # Loop until the program exit
    while True:
        # Loop until user enter valid inputs
        while True:
            try:
                first, operation, second = input("\033[92mEnter your math: \033[0m").split(" ")
                first = float(first)
                second = float(second)
                if operation in ['+', '-', '*', '/']:
                    break
            except:
                pass
            
        # calculate and print input
        result = calculate(first, operation, second)
        print(f"{first} {operation} {second} = {result}")
        
        
        # Loop until user enter valid input
        while True:
            next = continue_with(result)
            match next:
                case 'n':
                    print()
                    print()
                    break
                case 'e':
                    print(text2art("Bye",font='rnd-small',chr_ignore=True))
                    exit()
                case 'y':
                    # Continue the calculation with result from the previous calculation
                    while True:
                        try:
                            operation, second = input(f"\033[92mContinue enter the math: \033[0m{result} ").split(" ")
                            first = result
                            second = float(second)
                            if operation in ['+', '-', '*', '/']:
                                break
                        except:
                            pass
                    
                    result = calculate(first, operation, second)
                    print(f"{first} {operation} {second} = {result}")
                    
        
def continue_with(result):
    while True:
        next = input(f"\033[92mType 'y' to continue calculating with {result}, type 'n' to start a new calculation or type 'e' to exit program: \033[0m").lower()
        if next in ['y', 'n', 'e']:
            return next            



def calculate(first, operation, second):
    '''
    Function takes 3 parameter and return the result 
    '''
    match operation:
        case '+':
            return first + second
        case '-':
            return first - second
        case '*':
            return first * second
        case '/':
            return first / second
        
        
if __name__ == "__main__":
    main()        
