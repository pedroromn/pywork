#! -*- coding: utf-8 -*-

"""
Program: filesys.py
Author: Ken

Provides a menu-driven tool for navigating a file system
and gathering information on files.
"""

import os
import os.path


QUIT = '7'

COMMANDS = ('1', '2', '3', '4', '5', '6', '7')

MENU = """1 List the current directory
2 Move up
3 Move down
4 Number of files in the directory
5 Size of the directory in bytes
6 Search for a filename
7 Quit the program"""

def main():
    """Main Function"""
    while True:
        print os.getcwd()
        print
        print MENU
        command = accept_command()
        run_command(command)
        if command == QUIT:
            print "Have a nice day!"
            break

def accept_command():
    """Inputs and returns a legitimate command number"""
    while True:
        command = raw_input("Enter a number: ")
        if not command in COMMANDS:
            print "Error: command not recognized"
        else:
            return command

def run_command(command):
    """Selects and runs a command"""
    if command == '1':
        list_current_dir(os.getcwd())
    elif command == '2':
        move_up()
    elif command == '3':
        move_down(os.getcwd())
    elif command == '4':
        print "The total number of files is", \
            count_files(os.getcwd())
    elif command == '5':
        print "The total number of bytes is", \
            count_bytes(os.getcwd())
    elif command == '6':
        target = raw_input("Enter the search string: ")
        file_list = find_files(target, os.getcwd())
        if not file_list:
            print "String not found"
        else:
            for file_target in file_list:
                print "Archivo localizado!" + " -> " + file_target


def list_current_dir(dir_name):
    """Prints a list of the cwd's contents."""
    lyst = os.listdir(dir_name)
    for element in lyst: print element


def move_up():
    """Moves up to the parent directory"""
    os.chdir("..")

def move_down(current_dir):
    """Moves down to the named subdirectory if it exists."""
    new_dir = raw_input("Enter the directory name: ")
    if os.path.exists(current_dir + os.sep + new_dir) and \
       os.path.isdir(new_dir):
        os.chdir(new_dir)
    else:
        print "ERROR: no such name"

def count_files(path):
    """Returns the number of files in the cwd and alls 
    its subdirectories."""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += 1
        else:
            os.chdir(element)
            count += count_files(os.getcwd())
            os.chdir("..")
    return count

def count_bytes(path):
    """Returns the number of bytes in the cwd and all 
    its subdirectories"""
    count = 0
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            count += os.path.getsize(element)
        else:
            os.chdir(element)
            count += count_bytes(os.getcwd())
            os.chdir("..")
    return count


def find_files(target, path):
    """Returns a list of the filenames that contain
    the target string int he cwd and all its subdirectories."""
    files = []
    lyst = os.listdir(path)
    for element in lyst:
        if os.path.isfile(element):
            if element == target:
                files.append(path + os.sep + element)
        else:
            os.chdir(element)
            files.extend(find_files(target, os.getcwd()))
            os.chdir("..")
    return files


if __name__ == "__main__":
    main()
