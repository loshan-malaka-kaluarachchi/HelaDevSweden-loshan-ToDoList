# To-Do list
# Add item
# Delete item
# Change item
# Mark item as incomplete
# Mark item as complete
# list[ tuple[TaskID:int, TaskName:str, Status:str], ... , ... ]

items = [
    ('1', 'Getting Familiar with the Python Development Environment', 'Complete'),
    ('2', 'Python Data Types, Variables & Inbuilt functions', 'Complete'),
    ('3', 'Flow Control', 'Complete'),
    ('4', 'Flow Control in Python (Looping techniques)', 'Complete' ),
    ('5', 'Functions in Python', 'Complete'),
    ('6', 'Unit testing in Python', 'Complete'),
    ('7', 'Functions, Modules, Unit Testing, Previous Excersises', 'Complete'),
    ('8', 'Applying Collection Types - Simple TODO application', 'Incomplete'),
    ('9', 'Solution Discussion', 'Incomplete'),
    ('10', 'HTTP Request handling and Web Scraping using Python', 'Incomplete')
]

def prompt_usr(keyword:str) -> str:
    ''' Selector function for getting user inputs and returns user's strings'''
    # ----- Print Only Start ----- #
    
    def show_help() -> str:
        message = """
My TODO-List - (Powered by HelaDevs Family)
-------------------------------------------
    Description
    -----------
    * SHOW      -   Show to-do list
    * FIND      -   Search task
    * ADD       -   Add item
    * DEL       -   Delete item
    * MOD       -   Change item name or status(Complete/Incomplete)
    * HELP      -   Show this help menu
    * EXIT      -   Exit this program
    
    Syntax
    ------
    * Note - STATUS is 0 or 1 for 'Incomplete' and 'Complete' respectively
    * Command keywords are not entirely case sensitive
             
    SHOW
    FIND -id [TASK_ID]
    FIND -name [string]
    ADD [TASK_NAME]
    DEL -id [TASK_ID]
    MOD -id [TASK_ID] -name "[NEW_NAME]" -status [STATUS]
    MOD -id [TASK_ID] [STATUS] 
    HELP
    
    """
        return print(message)
    # ----- Print Only End ----- #
    
    def get_task_name_from_user() -> str:
        return input('Enter task: ')
    def get_task_status_from_user() -> str:
        return input('Enter task status: ')
    def get_task_id_from_user() -> str:
        return input('Enter task ID: ')
    def get_user_command_string() -> str:
        return input('Enter command(For Help Enter \'HELP\'): ')
    
    func_list = {
        'TaskID':   get_task_id_from_user,
        'TaskName': get_task_name_from_user,
        'Status':   get_task_status_from_user,
        'GetUserCommand':   get_user_command_string,
        'ShowHelp': show_help 
    }
    return func_list[keyword]()

def fetch_colum_widths(items: list) -> tuple:
    '''Return column widths for padding purposes'''
    def get_dimesions() -> tuple:
        '''Find and return dimensions'''
        rows = len(items)
        cols = len(items[0])
        return rows,cols
    
    def get_max_col_width(col_n:int) -> int:
        '''Return maximum column width'''
        width = 0
        for row in items:
            current_length = len(row[col_n])
            if current_length > width:
                width = current_length
            else:
                continue
        return width
    
    widths = []
    number_of_columns = get_dimesions()[1]
    for column in range(number_of_columns):
        widths.append(get_max_col_width(column))
    return widths

def show_table(data: list) -> None:    
    def make_table(items:list) -> list:
        def arrange_content() -> list:
            strings = []
            left_char = '|'; right_char = '|'
            column_widths = fetch_colum_widths(items)
            for item in items:
                count = 0
                for member in item:
                    strings.append(left_char + member.ljust(column_widths[count]))
                    count += 1
                strings.append(right_char + '\n')
            return strings
    
        def h_line(char: str, shrink: int) -> str:
            row_length = 0
            for string in table:
                if string.endswith('\n'):
                    row_length += len(string) - 1 - shrink
                    break
                else:
                    row_length += len(string)
                    continue
            return '+' + char*row_length + '+\n'
    
        table = arrange_content()
        line_str = h_line('-',shrink=2)
        table.insert(0,line_str)
        table.append(line_str)
        return table
    
    for item in make_table(data):
        print(item,sep='',end='')

def update_number_of_tasks() -> int:
    count = 0
    for task in items: # Variable Task is a dummy variable 
        count += 1
    return count
    
def add_task(task_name: str) -> None:
    global count
    item = (str(count + 1), task_name, 'Incomplete')
    count += 1
    items.append(item)

def del_task(task_id: str) -> None:
    for tup_item in search_by_task_id(task_id):
        items.remove(tup_item)
    
def fetch_status(t_status:str) -> str|None: # Called inside the match case block
    ''' Return task status as a string literal (Complete | Incomplete) '''
    if t_status == '0':
        return 'Incomplete'
    elif t_status == '1':
        return 'Complete'
    else:
        return None
    
    
def search_by_task_id(task_id_string: str) -> tuple|None:
    '''Search and returns an item from the TO-DO list based on Task ID'''
    column_index = 0
    search_results = []
    for item in items:
        if item[column_index] == task_id_string:
            search_results.append(item)
        else:
            continue
    return search_results

def search_by_task_name(task_name_string: str) -> tuple|None:
    '''Search and returns an item from the TO-DO list based on Task Name'''
    column_index = 1
    search_results = []
    for item in items:
        if item[column_index].startswith(task_name_string):
            search_results.append(item)
        else:
            continue
    return search_results

def search_by_status(fstatus) -> tuple|None:
    '''Search and returns an item from the TO-DO list based on Task ID'''
    completion = fetch_status(fstatus)
    column_index = 2
    search_results = []
    for item in items:
        if item[column_index] == completion:
            search_results.append(item)
        else:
            continue
    return search_results

usr_input = None
count = update_number_of_tasks() 
prompt_usr('ShowHelp')
show_table(items)

while True:
    
    usr_input = prompt_usr('GetUserCommand')
    # With reference to PEP 636 -Structural Pattern Matching Tutorial
    match usr_input.split():
        case [('SHOW'|'show'|'Show')]:
            show_table(items)
            
        case [('FIND'|'find'|'Find'|'Search'), '-id', id]:
            print(f'\nSearch results for: Task ID - {id}')
            show_table(search_by_task_id(id))
            print('\n')
            
        case [('FIND'|'find'|'Find'|'Search'), '-name', name]:
            print(f'\nSearch results for: Task Name - {name}')
            show_table(search_by_task_name(name))
            print('\n')
            
        case [('FIND'|'find'|'Find'|'Seach'),'-status', status]:
            print(f'\nSearch results for: Task Status - {status}')
            show_table(search_by_status(status))
            print('\n')
            
        case [('ADD'|'add'|'Add'), taskname]:
            add_task(taskname)
            update_number_of_tasks()
            print('Task added!\n')
            
        case [('DEL'|'del'|'Del'|'delete'), taskid]:
            del_task(taskid)
            update_number_of_tasks()
            print('Item deleted!\n')
            
        case [('MOD'|'mod'|'Mod'|'Change'|'change'),'-id', taskid, '-name', *new_task_name, '-status', new_status]:
            old_tup_item = search_by_task_id(taskid)[0]
            old_task_name = old_tup_item[1]
            old_task_status = old_tup_item[2]
            index = items.index(old_tup_item)
            new_string = ''
        
            if fetch_status == None:
                print('Invalid status entry!\nStatus should be 0 or 1.')
                break
            for word in new_task_name:
                new_string += word.strip('\"') + ' '
            new_string = new_string.removesuffix(' ')
            new_status = fetch_status(new_status)
            new_tup_item = (taskid, new_string, new_status)
            
            items.remove(old_tup_item)           
            items.insert(index,new_tup_item)
            print(f'\nSuccessfully changed\n   Task {taskid} : {old_task_name} ({old_task_status})\n=> Task {taskid} : {new_string} ({new_status})!\n')
        
        case [('MOD'|'mod'|'Mod'|'Change'|'change'), '-id', taskid, new_status]:
            old_tup_item = search_by_task_id(taskid)[0]
            old_task_name = old_tup_item[1]
            old_task_status = old_tup_item[2]
            index = items.index(old_tup_item)
            
            new_status = fetch_status(new_status)
            new_tup_item = (taskid, old_task_name, new_status)
            items.remove(old_tup_item)
            items.insert(index, new_tup_item)
            print(f'\nSuccessfully changed\n   Task {taskid} : {old_task_name} ({old_task_status})\n=> Task {taskid} : {old_task_name} ({new_status})!\n')
        
        case [('HELP'|'help'|'Help')]:
            prompt_usr('ShowHelp')
        
        case [('EXIT'|'Exit'|'exit'|'QUIT'|'quit')]:
            print('Exiting!')
            break
        case _:
            print("Invalid Command!\nTry again.")