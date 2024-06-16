import os
import threading

from helpers.ui import Ui
from helpers.colors import ColorHelper
from utils.file_utils import FileUtils
from utils.booster import Booster

TOKENS_PATH = "input/tokens.txt"
PROXIES_PATH = "input/proxies.txt"

def check_files() -> None:
    Ui.show_all()
    
    os.mkdir("input") if not os.path.exists("input") else None
    
    files_to_check = [TOKENS_PATH, PROXIES_PATH]
    for file in files_to_check:
        if not os.path.exists(file):
            FileUtils.create_file(file)

def main() -> None:
    tokens = FileUtils.read_file(TOKENS_PATH).splitlines()

    # TODO: Add proxy support
    proxies = FileUtils.read_file(PROXIES_PATH).splitlines()

    Ui.show_all()
    
    choice = input(f"{ColorHelper.color('[?]')} Enter choice: ")
    
    if choice == "1":
        invite_link = input(f"{ColorHelper.color('[?]')} Enter invite link: ").strip()
        
        if not invite_link:
            main()
        
        invite_code = invite_link.split('/')[-1]
        
        Ui.show_banner()
        
        for token in tokens:
            booster_instance = Booster(token)
            threading.Thread(
                target=booster_instance.join_server, 
                args=(invite_code,)
            ).start()
        
        Ui.wait_for_exit()
    
    elif choice == "2":
        server_id = input(f"{ColorHelper.color('[?]')} Enter server ID: ").strip()
        boost_count = input(f"{ColorHelper.color('[?]')} Enter boost count: ").strip()
        
        if not server_id or not boost_count:
            main()
        
        Ui.show_banner()
        
        for token in tokens:
            booster_instance = Booster(token)
            threading.Thread(
                target=booster_instance.boost_server, 
                args=(server_id, boost_count)
            ).start()
        
        Ui.wait_for_exit()
    else:
        main()

if __name__ == "__main__":
    check_files()
    main()
