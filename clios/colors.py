from colorama import Fore, Style
red = Fore.RED
blue = Fore.BLUE
white = Fore.WHITE
cyan = Fore.CYAN
bold = Style.BRIGHT
def colorprint(color,text,style=""):
    print(f"{color}{text}{style}")