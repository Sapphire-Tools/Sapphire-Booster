import os
import json
import unittest

from src.utils.file_utils import FileUtils

print("\nRunning tests for file_utils.py:")

class TestFileUtils(unittest.TestCase):
    def setUp(self):
        # Test file paths
        self.test_file_path = 'test_file.txt'
        self.test_json_path = 'test_file.json'
        self.test_content = 'Test content'
        self.test_json_data = {'key': 'value'}

    def tearDown(self):
        try:
            os.remove(self.test_file_path)
            os.remove(self.test_json_path)
        except FileNotFoundError:
            pass

    def test_read_file(self):
        with open(self.test_file_path, 'w') as file:
            file.write(self.test_content)
        
        result = FileUtils.read_file(self.test_file_path)
        self.assertEqual(result, self.test_content)

    def test_read_file_file_not_found(self):
        with self.assertRaises(FileNotFoundError):
            FileUtils.read_file('nonexistent_file.txt')

    def test_read_json(self):
        with open(self.test_json_path, 'w') as file:
            json.dump(self.test_json_data, file)
        
        result = FileUtils.read_json(self.test_json_path)
        self.assertEqual(result, self.test_json_data)

    def test_create_file(self):
        FileUtils.create_file(self.test_file_path, self.test_content)
        
        with open(self.test_file_path, 'r') as file:
            result_content = file.read()
            self.assertEqual(result_content, self.test_content)

    def test_create_file_empty_content(self):
        FileUtils.create_file(self.test_file_path, '')
        
        with open(self.test_file_path, 'r') as file:
            result_content = file.read()
            self.assertEqual(result_content, '')

    def test_create_file_json(self):
        FileUtils.create_file(self.test_json_path, json.dumps(self.test_json_data))
        
        with open(self.test_json_path, 'r') as file:
            result_json = json.load(file)
            self.assertEqual(result_json, self.test_json_data)

if __name__ == '__main__':
    unittest.main()
