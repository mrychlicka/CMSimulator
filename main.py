import os

execution_mode = input("In which mode you want to execute coffee machine simulator? "
                           "Type \'1\' for \'asci drawings\' mode, \'2\' if debug mode: ")
if execution_mode == "1":
    os.system("python execution_ascii.py")
if execution_mode == "2":
    os.system("python execution_debug.py")
else:
    print("Exit")

