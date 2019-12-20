
# SAMSOS by sam kothe (flouro)
# its cool i guess

from os import system, name
global FL
FL = {}
global RC
RC = 0
global AD
AD = []

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def startUp():
    print('''
     _______  _______  __   __  __   _______    _______  _______ 
|       ||   _   ||  |_|  ||  | |       |  |       ||       |
|  _____||  |_|  ||       ||__| |  _____|  |   _   ||  _____|
| |_____ |       ||       |     | |_____   |  | |  || |_____ 
|_____  ||       ||       |     |_____  |  |  |_|  ||_____  |
 _____| ||   _   || ||_|| |      _____| |  |       | _____| |
|_______||__| |__||_|   |_|     |_______|  |_______||_______|

    dec 18 2019 by Sam Kothe
    enter 'hp' for help
    ''')
    print('\n')

    # Might implement recursive filesystem later idk
''' 
def fileAccess1(name):
    name = name.split("/")
    RC = RC+1
    nf.append(FL[])


def fileAccess2(name):
    name = name.split("/")

'''


def fileAdd(name, data):
    FL[name] = data
    print("File " + name + " was added to the filelist.")


def filePrint(name):
    print("----------------------------------------")
    print(FL[name])
    print("----------------------------------------")


def multiLine(name):
    e = 0
    p = 0
    data = []
    while e == 0:
        p = p + 1
        ll = input(str(p) + "> ")
        data.append(ll)
        if ll == "esc":
            data.pop()
            data = "\n".join(data)
            break
    fileAdd(name, data)


def helpme():
    print("""
    Add file (one line) -------- nf [name] [data]
    Add file (multi line) ------ ml [name]       (you will be prompted to type, enter 'esc' to save)
    Access a file -------------- pf [name]
    Clear the screen ----------- cl
    Execute SOSLANG code ------- sx [name]
    Help ----------------------- hp
    """)


def takeorigPrompt():
    prompt = input(">")
    pList = prompt.split()
    return pList


def promptDistribution(pList):
    RC = 0
    command = pList[0]
    if command == "nf":
        fileAdd(pList[1], pList[2])
    elif command == "pf":
        filePrint(pList[1])
    elif command == "cl":
        clear()
    elif command == "ml":
        multiLine(pList[1])
    elif command == "hp":
        helpme()
    elif command == "sx":
        execSOSLANG(FL[pList[1]])
    elif command == "ep":
        print(pList[1])


def execSOSLANG(code):
    lineNumber = 0
    splitUpCode = dict(zip([i for i in range(len(code.split("\n")))], code.split("\n")))
    while lineNumber < len(code):
        print("Line" + str(lineNumber))
        currentLine = splitUpCode[lineNumber].split("|")
        command = currentLine[0]
        if command == "J":             # I should really implement recursion to allow for using addresses as operands...
            lineNumber = eval(currentLine[1]) - 1             # YAY SECURITY FLAWS
        elif command == "P":
            print(str(currentLine[1]) + str(eval(currentLine[2])))              # YAY SECURITY FLAWS
        elif command == "JA":
            lineNumber = eval(splitUpCode["".join(currentLine[1].split("("))]) - 1
        elif command == "R":
            promptDistribution([currentLine[1], currentLine[2], currentLine[3]])

        lineNumber = lineNumber + 1


startUp()
while True:
    try:
        promptDistribution(takeorigPrompt())
    except IndexError:
        continue
    except KeyError:
        continue
    except NameError:
        continue
