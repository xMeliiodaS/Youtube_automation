import json


class ConfigProvider:

    @staticmethod
    def load_config_json():
        try:
            with open('C:\\Users\\Bahaa\\Desktop\\config.json', 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"File not found. Starting with an empty library.")