import json
import datetime

class JsonHandler:
    def __init__(self, active_note):
        self.file_path = active_note
        


    def read_json(self):
        try:
            with open(self.file_path, 'r') as file:
                data = json.load(file)
                file.close()
            return data
            # return json.dumps(data, indent = 4)
        except FileNotFoundError:
            print("File not found.")
            return None
        except json.JSONDecodeError:
            print("Invalid JSON format.")
            return None

    def write_json(self, data):
        try:
            with open(self.file_path, 'w') as file:
                json.dump(data, file, indent=4)
            print("Note saved successfully.")
        except Exception as e:
            print(f"Error writing data: {e}")

    def create(self, new_data):
        old_data = self.read_json() or {}
        old_data.update(new_data)
        self.write_json(old_data)

    def read(self):
        data = self.read_json()
        if data:
            return data
        else:
            return {}

    def update(self, **kwargs):
        old_data = self.read_json() or {}
        for key, value in kwargs.items():
            if key in old_data:
                old_data[key] = str(value)  # Convert to string object
                print(f"Value for key '{key}' updated successfully.")
            else:
                print(f"Key '{key}' not found.")
        self.write_json(old_data)

    def delete(self, key):
        old_data = self.read_json() or {}
        if key in old_data:
            del old_data[key]
            self.write_json(old_data)
            print(f"Key '{key}' deleted successfully.")
        else:
            print(f"Key '{key}' not found.")
