from helpers.ui import Ui

from utils.file_utils import FileUtils
from utils.module_handler import ModuleHandler

def main() -> None:
    Ui.show_all()

    tokens = FileUtils.read_file(FileUtils.TOKENS_PATH).splitlines()
    proxies = FileUtils.read_file(FileUtils.PROXIES_PATH).splitlines() # TODO: Add proxy support

    while True:
        Ui.show_all()

        choice = Ui.get_user_input("Enter choice")
        
        if choice == "1":
            ModuleHandler.handle_join_server(tokens)
        elif choice == "2":
            ModuleHandler.handle_boost_server(tokens)
        else:
            main()

if __name__ == "__main__":
    FileUtils.check_files()
    main()
