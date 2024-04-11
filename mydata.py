
# To do:
# Make a function for checking missing data
# Make a function to search for specific data(ints or strings)
# Make a function for showing all keys(Column headings)
# make a function for showing all records(Rows)
# Make a function for adding data
# Make a function for removing or updating data

# ----- Start Function Definitions ----- #
def check() -> (int|bool):
    ''' Checks whether the data is properly aligned or missing and returns the number of records'''
    n_records = None
    for key in data:
        if len(data[key]) == 0: # Check whether keys have empty lists
            print(f'Warning! No data in {key}!\n')
            break
        
        if n_records == None: # Get the size of the list of the first key
            n_records = len(data[key])
            break
    
    for key in data: # Compare the list sizes of other keys with the first one
        if n_records == len(data[key]): # If the list sizes are the same; then its a good table
            # print(f'{key} is OK.')
            pass
        else:
            print(f'Values are missing!\nRe-check data.') # If the list sizes vary; then some data is missing
            return False
    return n_records

def search_value(value:str|int|float) -> (int|None):
    '''Search input then return key and index. If not return None. '''
    for key in data:
        if value in data[key]:
            return key,data[key].index(value)
        else:
            return None

def show_keys():
    for key in data:
        print(key,end=' ')
    print('')

def show_records():
    for row in range(n_rows):
        for key in keys:
            value = data[key][row]
            print(value,end=' ')
        print('')
        
def calc_cost():
    cost_vals = []
    for row in range(n_rows):
        cost_vals.append(data['Qty'][row]*data['Price'][row])
    data.update(Cost=cost_vals)
    
def get_largest() -> (list):
    '''Search input then return key and index. If not return None. '''
    largest = []
    for key in data:
        sizes = []
        sizes.append(len(key)) # Get string length of column label
        for value in data[key]:
            sizes.append(len(str(value)))    
        sizes.sort(reverse=True)
        largest.append(sizes[0])
    return largest   
# ----- End Function Definitions ----- #


# ----- Start Global Variables ----- #
data = {
    'Item'  :['Paint-Brush', 'Eraser', 'Pen', 'Paper', 'Book'],
    'Qty'   :[5, 6, 10, 2, 5],
    'Price' :[1, 0.5, 0.25, 3, 8]
}

global n_rows
n_rows = check()
keys = data.keys()
# ----- End Global Variables ----- #

def show_table() -> None:
    #print(search_value('Eraser'))    
    show_keys()
    show_records()
    print('\n')

def calculate():
    calc_cost()
    show_keys()
    show_records()
    print('\n')

def main():
    print(get_largest())
    #show_table()
    #calculate()
    
#main()