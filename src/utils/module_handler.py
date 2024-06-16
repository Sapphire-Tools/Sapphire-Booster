import threading

from helpers.ui import Ui
from utils.booster import Booster

class ModuleHandler:
    @staticmethod
    def handle_join_server(tokens: list[str]) -> None:
        invite_link = Ui.get_user_input("Enter invite link")
        
        if invite_link:
            invite_code = invite_link.split('/')[-1]
            Ui.show_banner()
            
            for token in tokens:
                booster_instance = Booster(token)
                threading.Thread(
                    target=booster_instance.join_server, 
                    args=(invite_code,)
                ).start()
            
            Ui.wait_for_exit()

    @staticmethod
    def handle_boost_server(tokens: list[str]) -> None:
        server_id = Ui.get_user_input("Enter server ID")
        boost_count = Ui.get_user_input("Enter boost count")
        
        if server_id and boost_count:
            Ui.show_banner()
            
            for token in tokens:
                booster_instance = Booster(token)
                threading.Thread(
                    target=booster_instance.boost_server, 
                    args=(server_id, boost_count)
                ).start()
            
            Ui.wait_for_exit()