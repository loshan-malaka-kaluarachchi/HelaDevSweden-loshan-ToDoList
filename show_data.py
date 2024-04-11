from mydata import data, get_largest
from mydata import n_rows

def enclose(func):
    def hline():
        print('-----------')
        val=func()
        print('-----------')
        return val
    return hline

@enclose
def draw_title():
    count = 0
    for key in data:
        string = key + (column_widths[count] - key.__len__())*' '
        print(string, end='|')
        count += 1
    print('')


def draw_content():
    for row in range(n_rows):
        count = 0
        for key in data:
            string = str(data[key][row]) + (column_widths[count] - str(data[key][row]).__len__())*' '
            print(string, end='|')
            count += 1
        print('')

column_widths = get_largest()

#draw_title()
def greet(*names):  
     for name in names:
         print('Hello ',name)
         
greet('A','B','C','D')