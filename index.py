import json
import requests
import datetime

ENABLE_DPRINT = not False
dprint = print if ENABLE_DPRINT else lambda *a, **k: None

class Processor:
    def __init__(self, username: str, password: str) -> None:
        self.session = requests.session()
        self.initialize(username, password)

    def initialize(self, username: str, password: str) -> None: #login
        ...

    def do_all(self) -> None:
        ...

def main():
    with open("config.json", "r", encoding="utf-8") as f:
        j = json.load(f)
    processor = Processor(j["username"], j["password"])
    processor.do_all()
    print("All-Done")

if __name__ == "__main__":
    main()