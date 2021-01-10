# Made by Lord-Gianticus, please credit me when using this!
import time
import os
from pip import main as pipmain

name = os.path.basename(__file__)
folder_list = []
file_list = []
entry = int(0)
program_location = os.getcwd()
gm = str('.gitmodules')
gi = str('.gitignore')
ga = str('.gitattributes')

class module:
    def checker(a:str):
        code = 'import',a
        try:
            code()
            imported = True
        except:
            print('Module not found!')
            time.sleep(2)
            print("Attempting pip install.")
            time.sleep(5)
            pipmain(['install', a])
            imported = False
        if imported == True:
            return print(a,'is already installed and is imported!'), time.sleep(5)
        else:
            return print(a,'is now installed. Importing now.'), time.sleep(2), code(), time.sleep(5)

class extension:
    def checker():
        if name.endswith('.py') == True:
            print('The script is a py file. Checking to see what folder checker is in.')
            time.sleep(2)
            if program_location.endswith('modules\checker') == True:
                print('checker is in the modules folder.')
            else:
                print('checker is not in the modules folder.')
                time.sleep(2)
                print('checking that the modules folder exists.')
                time.sleep(2)
                if os.path.isdir('modules') == False:
                    input("the modules folder doesn't exist! This function cannot work without it! Press enter to exit.")
                    exit()
            update = int(input('Do you want to update the submodules inside the modules folder?\n[1]Yes\n[2]No\n'))
            if update == 1:
                if program_location.endswith('modules\checker') == True:
                    os.chdir('../')
                    start = os.getcwd()
                    for dir in os.listdir(os.getcwd()):
                        if os.path.isdir(dir) == True:
                            if dir.endswith('checker') == False:
                                folder_list.append(dir)
                else:
                    os.chdir('modules')
                    start = os.getcwd()
                    for dir in os.listdir(os.getcwd()):
                        if os.path.isdir(dir) == True:
                            folder_list.append(dir)
                length = len(folder_list)
                while entry <= length:
                    os.chdir(folder_list[entry])
                    for file in os.listdir(os.getcwd()):
                        if os.path.isfile(file) == True:
                            if file.endswith('.git') == True and file.endswith(gi) == False and file.endswith(gm) == False and file.endswith(ga) == False:
                                os.system('cmd /c git pull')
                    os.chdir(start)
                    entry = entry + 1
                if entry > length:
                    if program_location.endswith('modules\checker') == True:
                        return print('All submodules (but checker) were updated or are up to date.')
                    else:
                        return print('All submodules were updated or are up to date.')
            elif update == 2:
                print('Ok nothing will be updated! You might want to update stuff next time.')
            return time.sleep(5)
        else:
            print("script is not a .py file so I'm assuming that this is a .exe file.")
            time.sleep(2)
            print('checking that statement of mine...')
            time.sleep(2)
            if name.endswith('.exe') == False:
                input("Script is not a exe! Ima guess it's a pyi or something. Please convert it to a py file! Press enter to exit.")
                exit()
            else:
                return print('Yep! I was right! No need to update submodules because it is all compiled in the exe.')

print('checker is all setup.')
time.sleep(2)