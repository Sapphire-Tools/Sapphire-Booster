import os
import json

class FileUtils():
    TOKENS_PATH = "input/tokens.txt"
    PROXIES_PATH = "input/proxies.txt"

    @staticmethod
    def open_file(path: str, method: chr, read_function: callable) -> object:
        with open(path, method) as file:
            return read_function(file)
        
    @staticmethod
    def read_file(path: str) -> str:
        return FileUtils.open_file(path, 'r', lambda file: file.read())
        
    @staticmethod
    def read_json(path: str) -> dict:
        return FileUtils.open_file(path, 'r', lambda file: json.load(file))

    @staticmethod
    def create_file(path: str, content: str = ''):
        return FileUtils.open_file(path, 'x', lambda file: file.write(content))
    
    @staticmethod
    def create_directory(path: str):
        os.makedirs(path, exist_ok=True)

    @staticmethod
    def check_and_create_directory(directory: str) -> None:
        if not os.path.exists(directory):
            os.mkdir(directory)

    @staticmethod
    def check_and_create_file(file_path: str) -> None:
        if not os.path.exists(file_path):
            FileUtils.create_file(file_path)
            
    @staticmethod
    def check_files() -> None:
        FileUtils.check_and_create_directory("input")
        
        files_to_check = [FileUtils.TOKENS_PATH, FileUtils.PROXIES_PATH]
        for file in files_to_check:
            FileUtils.check_and_create_file(file)
