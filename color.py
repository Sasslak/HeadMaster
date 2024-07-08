from colorama import Fore

# Setcolor

def setcolor(txt,color='white'):
    match color:
        case 'green':
            print(Fore.GREEN+txt+Fore.RESET)
        case 'red':
            print(Fore.RED+txt+Fore.RESET)
        case 'yellow':
            print(Fore.YELLOW+txt+Fore.RESET)
        case 'cyan':
            print(Fore.CYAN+txt+Fore.RESET)
        case 'blue':
            print(Fore.BLUE+txt+Fore.RESET)
        case 'white':
            print(Fore.WHITE+txt+Fore.RESET)
        case 'black':
            print(Fore.BLACK+txt+Fore.RESET)
        case _:
            print(txt)