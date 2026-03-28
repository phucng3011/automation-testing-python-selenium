import json

class ConfigReader:
    def __init__(self, config_path="config/config.json"):
        with open(config_path, "r") as file:
            self.config = json.load(file)

    def get_base_url(self):
        return self.config.get("base_url")

    def get_browser(self):
        return self.config.get("browser")

    def get_timeout(self):
        return self.config.get("timeout")
    
    def get_route(self, name):
        return self.config.get("routes", {}).get(name)