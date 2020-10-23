import os
from sys import platform

def print_repo():
    print(color('red','  ______   __    __'))
    print(color('red',' /      \ /  |  /  |'))
    print(color('red','/$$$$$$  |$$/  _$$ |_'))
    print(color('red','$$ | _$$/ /  |/ $$   |'))
    print(color('red','$$ |/    |$$ |$$$$$$/') + color('green','        ____             __        __'))
    print(color('red','$$ |$$$$ |$$ |  $$ | __') + color('green','     / __ \____  _____/ /_____  / /_'))
    print(color('red','$$ \__$$ |$$ |  $$ |/  |') + color('green','   / /_/ / __ \/ ___/ //_/ _ \/ __/'))
    print(color('red','$$    $$/ $$ |  $$  $$/') + color('green','   / ____/ /_/ / /__/ ,< /  __/ /_'))
    print(color('red',' $$$$$$/  $$/    $$$$/') + color('green','   /_/    \____/\___/_/|_|\___/\__/'))
    print('')
    print('     by MarkusS (https://github.com/MarkusSYT)')
    print('                (https://gitlab.com/MarkusSYT)')
    print('')
    print('     1. Commit           6. Create branch')
    print('')
    print('     2. Add Files        7. Switch branch')
    print('')
    print('     3. Delete Files     8. Merge')
    print('')
    print('     4. Repo status      9. Connect remote Repository')
    print('')
    print('     5. Show Log         10. push to remote Repository')
    print('')
    print('     99. Back')
    print('')

def print_menu():
    print(color('red','  ______   __    __'))
    print(color('red',' /      \ /  |  /  |'))
    print(color('red','/$$$$$$  |$$/  _$$ |_'))
    print(color('red','$$ | _$$/ /  |/ $$   |'))
    print(color('red','$$ |/    |$$ |$$$$$$/') + color('green','        ____             __        __'))
    print(color('red','$$ |$$$$ |$$ |  $$ | __') + color('green','     / __ \____  _____/ /_____  / /_'))
    print(color('red','$$ \__$$ |$$ |  $$ |/  |') + color('green','   / /_/ / __ \/ ___/ //_/ _ \/ __/'))
    print(color('red','$$    $$/ $$ |  $$  $$/') + color('green','   / ____/ /_/ / /__/ ,< /  __/ /_'))
    print(color('red',' $$$$$$/  $$/    $$$$/') + color('green','   /_/    \____/\___/_/|_|\___/\__/'))
    print(color('blue', "       Windows Edition                                         "))
    print('')
    print('     by MarkusS (https://github.com/MarkusSYT)')
    print('                (https://gitlab.com/MarkusSYT)')
    print('')
    print('     1. User Settings        5. Clone Repo')
    print('')
    print('     2. Create new Repo')
    print('')
    print('     3. Use existing Repo')
    print('')
    print('     4. Delete Repo')
    print('')
    print('     99. Exit')
    print('')

def color(c, text):
    if(str(c) == "green"):
        return '\033[92m' + str(text) + '\033[0m'
    elif(str(c) == "red"):
        return '\033[91m' + str(text) + '\033[0m'
    elif(str(c) == "blue"):
        return '\033[1;34;40m' + str(text) + '\033[0m'
    elif(str(c) == "yellow"):
        return '\033[1;33;40m' + str(text) + '\033[0m'
    elif(str(c) == "lightgreen"):
        return '\033[1;32;40m' + str(text) + '\033[0m'

def install():
    os.system('sudo apt -y install git')
    Linux()

def configurate():
    email = input("your email: ")
    name = input("your name: ")
    os.system('git config --global user.name "' + name + '"')
    os.system('git config --global user.email "' + email + '"')
    if platform == "linux" or platform == "linux2":
       Linux()
    elif platform == "darwin":
       MacOS()
    elif platform == "win32" or platform == "win64":
       Windows()


def exist_repo():
    os.system('clear')
    print_repo()
    select = int(input("> "))
    if(select == 1):
        message = input("Message: ")
        os.system("git commit -m " + '"' + message + '"')
        input("press a button to continue")
        exist_repo()
    elif(select == 2):
        file = input("File to add (* for all): ")
        os.system("git add " + file)
        exist_repo()
    elif(select == 3):
        file = input("File to remove (* for all): ")
        os.system("git rm --cached " + file + " -f")
        exist_repo()
    elif(select == 4):
        os.system("git status")
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 5):
        os.system("git log")
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 6):
        name = input("name for the branch: ")
        os.system("git branch " + name)
        exist_repo()
    elif(select == 7):
        name = input("switch to branch: ")
        os.system("git checkout " + name)
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 8):
        name = input("branch to merge: ")
        os.system("git merge " + name)
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 9):
        name = input("Repository Link: ")
        os.system("git remote add origin " + name)
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 10):
        name = input("branch to push: ")
        os.system("git push --force-with-lease origin " + name + ":" + name)
        print("")
        input("press a button to continue")
        exist_repo()
    elif(select == 99):
        if platform == "linux" or platform == "linux2":
            Linux()
        elif platform == "darwin":
            MacOS()
        elif platform == "win32" or platform == "win64":
            Windows()


def init_repos():
    os.system("clear")
    os.system("git init")
    file = open(".gitignore", "w")
    file.write("pocket.py")
    file.close()
    exist_repo()
def Windows():
    os.system('cls')
    print_menu()
    select = int(input("> "))

    if(select == 1):
        configurate()
    elif(select == 2):
        os.system("del .git/")
        init_repos()
    elif(select == 3):
        exist_repo()
    elif(select == 4):
        os.system("del .git/")
        Windows()
    elif(select == 5):
        name = input("repo to clone: ")
        os.system("git clone " + name)
        print("")
    elif(select == 99):
        exit()

def MacOS():
    os.system('clear')
    print_menu()
    select = int(input("> "))
    if(select == 1):
        configurate()
    elif(select == 2):
        os.system("sudo rm -rf .git/")
        init_repos()
    elif(select == 3):
        exist_repo()
    elif(select == 4):
        os.system("sudo rm -rf .git/")
        MacOS()
    elif(select == 5):
        name = input("repo to clone: ")
        os.system("git clone " + name)
        print("")
    elif(select == 99):
        exit()

def Linux():
    os.system('clear')
    print_menu()
    select = int(input("> "))
    if(select == 1):
        install()
    elif(select == 2):
        configurate()
    elif(select == 3):
        os.system("sudo rm -rf .git/")
        init_repos()
    elif(select == 4):
        exist_repo()
    elif(select == 5):
        os.system("sudo rm -rf .git/")
        Linux()
    elif(select == 6):
        name = input("repo to clone: ")
        os.system("git clone " + name)
        print("")
    elif(select == 99):
        exit()

if platform == "linux" or platform == "linux2":
   Linux()
elif platform == "darwin":
   MacOS()
elif platform == "win32" or platform == "win64":
   Windows()
