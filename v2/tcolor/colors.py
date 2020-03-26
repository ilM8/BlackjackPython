import sys
import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

clear()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    background_black=" \u001b[40m"
    background_red=" \u001b[41m"
    background_green=" \u001b[42m"
    background_yellow=" \u001b[43m"
    background_blue=" \u001b[44m"
    background_magenta=" \u001b[45m"
    background_cyan="\u001b[46m"
    background_white=" \u001b[47m"

    black=" \u001b[30m"
    red=" \u001b[31m"
    green=" \u001b[32m"
    yellow=" \u001b[33m"
    blue=" \u001b[34m"
    magenta=" \u001b[35m"
    cyan=" \u001b[36m"
    white=" \u001b[37m"

    reset=" \u001b[0m"


#Normal Text:
#print(f"{bcolors.#color#}#text#{bcolors.ENDC}")
