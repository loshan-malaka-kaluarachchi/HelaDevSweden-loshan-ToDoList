
def divide(a:float,b:float) -> float:
        return a/b
def showTerror(possible_culprits: TypeError):
    print('You have entered the following string/s for numeric calculations:')
    for arg in possible_culprits.args:
        arg_text = str(type(arg))
        if arg_text.find('str') != -1:
            print(f'\'{arg}\'')
            
try:
    x = 1;  y = 'b';    z = divide(x,y); 
    print(f'\n{x}/{y} = {z}')
except ZeroDivisionError:
    print('Division by zero is not allowed!')
except TypeError:
     showTerror(TypeError(x,y))
    
    