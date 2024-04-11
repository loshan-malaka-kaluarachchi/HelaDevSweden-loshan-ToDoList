#TODO: Write the functions for arithmatic operations here
#These functions should cover Task 2
def add(num1:float, num2:float) -> float:
    return num1 + num2

def subtract(num1:float, num2:float) -> float:
    return num1 - num2

def multiply(num1:float, num2:float) -> float:
    return num1*num2

def divide(num1:float, num2:float) -> float:
    if num2 == 0:
        print('float division by zero')
        return None
    else:
        return num1/num2

def power(base:float, index:float) -> float:
    if base == 0 and index < 0:
        print('float division by zero')
        return None
    else:
        return base**index

def remainder(num1:float, num2:float) -> float:
    if num2 == 0:
        print('float division by zero')
        return None
    else:
        return num1%num2

def exit() -> None:
    quit()    
    
def reset() -> int:
    return -2

history = []
def show_history(data:list) -> None:
    if len(data) == 0:
        print('No history to show')
    else:
        for calc in data:
            print(calc)
    
#-------------------------------------
#TODO: Write the select_op(choice) function here
#This function sould cover Task 1 (Section 2) and Task 3
def select_op(choice):
    math_operations = {
        '+':add,
        '-':subtract,
        '*':multiply,
        '/':divide,
        '^':power,
        '%':remainder
    }
    def unknown_Operation() -> None:
        print('Unrecognized operation')
        
    def invalid_Usr_Input() -> None:
        print('Not a valid number, please enter again.')
        
    def errorUnknown() -> None:
        print('Something went wrong')
    
    def is_there_dollar_sign(value:str) -> bool:
        for char in value:
            if char == '$':
                return True
            else:
                continue
        return False
                
    def is_there_hash_sign(value: str) -> bool:
        for char in value:
            if char == '#':
                return True
            else:
                continue
        return False
            
    def is_there_an_alpha(value:str) -> bool:
        for char in value:
            if char.isalpha():
                return True
            else:
                return False
                
########################################################
    if choice == '#':
        return -1
    
    if is_there_an_alpha(choice):
        unknown_Operation()
        reset() 
    
        
    while choice in ['+','-','*','/','%','^']:
        firstnum = input('Enter first number: ')
        print(firstnum)
        if is_there_hash_sign(firstnum):
            print("Done. Terminating")
            exit()
        if is_there_dollar_sign(firstnum):
            break
        if is_there_an_alpha(firstnum):
            invalid_Usr_Input()
            continue
            
        secondnum = input('Enter second number: ')
        print(secondnum)
        if is_there_hash_sign(secondnum):
            print("Done. Terminating")
            exit()
        if is_there_dollar_sign(secondnum):
            break
        if is_there_an_alpha(secondnum):
            invalid_Usr_Input()
            continue
        
        firstnum = float(firstnum)
        secondnum = float(secondnum)
        result = math_operations[choice](firstnum,secondnum)
        string = f'{firstnum} {choice} {secondnum} = {result}'
        print(string)
        break
        
        
#End the select_op(choice) function here
#-------------------------------------
#This is the main loop. It covers Task 1 (Section 1)
#YOU DO NOT NEED TO CHANGE ANYTHING BELOW THIS LINE
while True:
  print("Select operation.")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  

  # take input from the user
  choice = input("Enter choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends here
    print("Done. Terminating")
    exit()