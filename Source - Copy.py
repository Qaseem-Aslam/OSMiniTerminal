import datetime
import os
import math


def help1():
    list = {'sqrt', 'pow', 'acos', 'asin', 'atan', 'atan', 'ceil', 'cos', 'cosh', 'e', 'exp', 'fabs', 'floor', 'log', 'log10', 'log2', 'pi', 'sin', 'sinh', 'tan', 'tanh', 'abs'}
    print("All supported functions are as follows:")
    for x in list:
        if x != None:
            print(x)


def calculator():

    while 1:
        eq = input()
        if eq == "exit":
            return

        try:
            result = eval(eq, {'sqrt': math.sqrt, 'pow': pow, 'acos': math.acos, 'asin': math.asin, 'atan': math.atan, 'atan': math.atan, 'ceil': math.ceil, 'cos': math.cos,
                        'cosh': math.cosh,'e': math.e, 'exp': math.exp, 'fabs':math.fabs, 'floor': math.floor, 'log': math.log, 'log10': math.log10,'log2':math.log2,
                        'pi':math.pi, 'sin':math.sin, 'sinh': math.sinh, 'tan': math.tan, 'tanh':math.tanh, 'abs': abs,'help':help1})
            print(result)
        except SyntaxError as e:
            print("Syntax error")
        except TypeError:
            print("Incomplete Parameters!")
        except NameError:
            print("Undefined function called. Use help() to see all supported operations")


def mkdir(name):
    try:
        if not os.path.exists(name):
            os.makedirs(name)
        else:
            print("Directory already exit!")
            return
    except OSError:
        print("Error making director!")
        return
    print("Directory created successfully!")


def rmdir(name):
    try:
        os.rmdir(name)
        print("Directory removed successfully!")
    except OSError as e:
        print(e.strerror)


os.chdir("E:\\root")

while 1:
    path = os.getcwd()
    print(path[7:], end='')
    command = input('>')
    originalCommand = command
    command = command.lower()
    curr = os.getcwd()
    os.chdir("E:\\root")
    file = open("history.txt", "a+")
    file.write(command+"\n")
    file.close()
    os.chdir(curr)
    if command[0:5] == "mkdir":
        mkdir(originalCommand[6:])
    elif command[0:5] == "rmdir":
        rmdir(originalCommand[6:])
    elif command == "exit":
        break
    elif command[0:5] == "touch":
        f = open(command[6:], "w+")
        print("File created!")
        f.close()
    elif command[0:3] == "cat":
        try:
            f = open(command[4:], "r")
            if f.mode == 'r':
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("File not found!")
    elif command[0:2] == "ls":
        all_files = os.listdir(".")
        if command[3:5] == "-l":
            for x in all_files:
                print(x)
        else:
            print(all_files)
    elif command[0:4] == "cd..":
        os.chdir("E:\\root")
    elif command[0:3] == "cd.":
        os.chdir("..")
        if os.getcwd() == "E:\\":
            print("You are already at root directory!")
            os.chdir("E:\\root")
    elif command[0:2] == "cd":
        os.chdir(os.getcwd()+"\\"+originalCommand[3:])
    elif command == "pwd":
        if len(os.getcwd()) == 7:
            print("\\")
        else:
            print(os.getcwd()[7:])
    elif command[0:6] == "rename":
        result = originalCommand.split("\"")
        if len(result) >= 4:
            try:
                os.renames(result[1], result[3])
                print("File renamed successfully!")
            except OSError as e:
                print(e.strerror)
        else:
            print("Invalid syntax")
    elif command == "date":
        now = datetime.datetime.now()

        print("Current date: ", end='')
        print(now.strftime("%Y-%m-%d"))
    elif command == "time":
        now = datetime.datetime.now()

        print("Current time: ", end='')
        print(now.strftime("%H:%M:%S"))
    elif command == "calculator":
        calculator()
    elif command == "history":
        f = open("history.txt", "r")
        if f.mode == 'r':
            content = f.read()
            print(content)
    else:
        print("Invalid command!")
