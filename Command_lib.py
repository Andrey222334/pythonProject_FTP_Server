import os
import shutil

def CurrentDirectory():
    return os.getcwd()

def CreatrDir(path):
    os.mkdir(path)

def RemoveDir(path):
    os.rmdir(path)

def ChoseDirectory(path):
    if path != 'up':
        os.chdir(path)
    else:
        current_directory = CurrentDirectory()
        for i in range(len(current_directory)-1, -1, -1):
            if current_directory[i] == '\\':
                break
            current_directory = current_directory[0:len(current_directory)-1]
        os.chdir(current_directory)

def CreateFile(path):
    new_file = open(path, 'w')
    new_file.close()

def WriteFile(path):
    write_file = open(path, 'w')
    write_txt = []
    while True:
        str_write = input()
        if str_write != '/end':
            write_txt.append(str_write + '\n')
            write_file.write(str_write + '\n')
        else:
            break
    write_file.close()
    return ''.join(write_txt)

def ReadFile(path):
    read_file = open(path, 'r')
    st = ''
    while True:
        line = read_file.readline()
        if not line:
            break
        st += line
    read_file.close()
    return st

def RemoveFile(path):
    os.remove(path)

def CopyFile(path, copy_path):
    shutil.copy(path, copy_path, follow_symlinks=True)

def MoveFile(path, move_path):
    shutil.move(path, move_path)

def RenameFile(path, new_name):
    os.rename(path, new_name)