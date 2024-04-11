def read_lines(filepath:str, n_lines:int, mode:str='r') -> list:

    fhandle = open(filepath, mode)
    fcontent = []
    for i in range(n_lines):
        fcontent.append(fhandle.readline())
    fhandle.close()
    return fcontent
    
def write2file(filepath:str, contents:list, n_lines:int, mode:str='w') -> None:
    
    fhandle = open(filepath, mode)
    for line in contents:
        fhandle.write(line)
    fhandle.close()

strings = read_lines("file1.txt",2)
write2file("file2.txt", strings,2)

for line in read_lines("file2.txt",2):
    print(line,end='')