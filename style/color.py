from colorama import Fore

# Setcolor

def setcolor(txt,color='white'):
    match color:
        case 'green':
            txt = (Fore.GREEN+txt+Fore.RESET)
        case 'red':
            txt = (Fore.RED+txt+Fore.RESET)
        case 'yellow':
            txt = (Fore.YELLOW+txt+Fore.RESET)
        case 'cyan':
            txt = (Fore.CYAN+txt+Fore.RESET)
        case 'blue':
            txt = (Fore.BLUE+txt+Fore.RESET)
        case 'white':
            txt = (Fore.WHITE+txt+Fore.RESET)
        case 'black':
            txt = (Fore.BLACK+txt+Fore.RESET)
        case _:
            pass
    return txt