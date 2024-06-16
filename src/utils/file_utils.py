import os
import json

class FileUtils():
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