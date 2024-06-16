import os

from helpers.colors import ColorHelper
from pystyle import Center

class Ui:
    CONSOLE_WIDTH = 100
    CONSOLE_HEIGHT = 25
    BANNER = """
 _____             _   _            _____             _           
|   __|___ ___ ___| |_|_|___ ___   | __  |___ ___ ___| |_ ___ ___ 
|__   | .'| . | . |   | |  _| -_|  | __ -| . | . |_ -|  _| -_|  _|
|_____|__,|  _|  _|_|_|_|_| |___|  |_____|___|___|___|_| |___|_|  
          |_| |_|                                                 
        """
    TITLE = "Sapphire Booster   I    Made by: @nrxlvyy   I   github.com/nrxlvyy/Sapphire-Booster"

    @staticmethod
    def initialize_console():
        os.system("cls" if os.name == "nt" else "clear")
        os.system(f"title {Ui.TITLE}" if os.name == "nt" 
                  else "echo -ne '\033]0;{Ui.TITLE}\007'")
        os.system(f"mode con: cols={Ui.CONSOLE_WIDTH} lines={Ui.CONSOLE_HEIGHT}")

    @staticmethod
    def print_banner():
        print(ColorHelper.color(Center.XCenter(Ui.BANNER)))

    @staticmethod
    def print_menu():
        # This is the only way I could think of to make the    
        # menu centered with colors (pystyle doesn't support that)
        print(f"{30 * ' '}{ColorHelper.color('[01]')} Join Server{' ' * 5} " +
              f"{ColorHelper.color('[02]')} Boost Server\n")

    @staticmethod
    def get_user_input(prompt: str) -> str:
        return input(f"{ColorHelper.color('[?]')} {prompt}: ").strip()

    @staticmethod
    def show_all():
        Ui.initialize_console()
        Ui.print_banner()
        Ui.print_menu()
    
    @staticmethod
    def show_banner():
        Ui.initialize_console()
        Ui.print_banner()

    @staticmethod
    def wait_for_exit():
        input()
