import pathlib
import os
from string import ascii_uppercase

# task 1
def listDirs(pt):
    print([x.name for x in os.scandir(path = pt) if x.is_dir()])
# ../tsis5/regex.py

def listFiles(pt):
    print([x.name for x in os.scandir(path = pt) if x.is_file()])


def listDirsAndFiles(pt):
    print([x.name for x in os.scandir(path = pt)])


# task 2
def checkPath(p):
    find_status = os.access(path = p, mode = os.F_OK)
    print(f'Existance : {find_status}')
    read_status = os.access(path = p, mode = os.R_OK)
    print(f'Radibility : {read_status}')
    write_status = os.access(path = p, mode = os.W_OK)
    print(f'Writability : {write_status}')
    exec_status = os.access(path = p, mode = os.X_OK)
    print(f'Executability : {exec_status}')

# task 3
def exist_and_retrive_path_info(p):
    find_status = os.access(path = p, mode = os.F_OK)
    if find_status:
        print(f'File : {os.path.basename(p)}')
        print(f'Directory : {os.path.dirname(p)}')
    else:
        print('Path is not executable')


# task 4
def count_lines(filename):
    file = open(filename, 'r')
    count = 0
    for line in file:
        count += 1
    return count


# task 5
def write_to_file(filename, new_list):
    file = open(filename, 'a')
    file.write(str(new_list))
    file.close()

    file = open(filename , 'r')
    print(file.read())


# task 6
def generate_files():
    for char in ascii_uppercase:
        file = open(f'./files/{char}.txt', 'x')
        file.close()


# task 7
def copyContent(init_filename, target_filename):
    init_file = open(init_filename, 'r')
    file_content = init_file.read()
    init_file.close()

    target_file = open(target_filename, 'w')
    target_file.write(str(file_content))
    target_file.close()
    print('Successfully copied')

    target_file = open(target_filename, 'r')
    print(target_file.read())
    target_file.close()


# task 8
def delete_file(p):
    if os.path.exist(p):
        os.remove(p)
        print('Successfully deleted the file')
    else:
        print('File does not exist')

def main():
    path = '..'
    print('Task 1')
    listDirs(path)
    listFiles(path)
    listDirsAndFiles(path)

    print('Task 2')
    checkPath(path)

    print('Task 3')
    exist_and_retrive_path_info('../TSIS5/str.py')

    print('Task 4')
    print(f'Number of lines in a file demofile.txt = {count_lines("demofile.txt")}')

    print('Task 5')
    write_to_file('demofile2.txt', ['Hello', 'World'])

    print('Task 6')
    #generateFiles()

    print('Task 7')
    copyContent('demofile.txt', 'demofile3.txt')

    print('Task 8')
    delete_file('./demofile.txt')


if __name__ == '__main__':
    main()