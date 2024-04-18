directory = '/home/mypc/MYPY/ErrorHandling/'
f_name = 'A_Textfile.txt'
f_path = directory + f_name

try:
    f_handle = open(f_path, mode='r')
except FileNotFoundError:
    print('File named \'{}\' not found!'.format(f_name))
    print('Check if the file path or file name is correct')
else:
    content = f_handle.read()
    f_handle.close()
    print(content)