import json
import requests
import datetime

import models

ENABLE_DPRINT = not False
dprint = print if ENABLE_DPRINT else lambda *a, **k: None

class Saved:
    def __init__(self):
        with open("saved.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)
        
    def get(self, key: string, default: any) -> any:
        return self.data.get(key, default)
    
    def set(self, key: string, value: any) -> None:
        self.data.update({key: value})
        with open("saved.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f)

class Processor:
    def __init__(self, username: str, password: str) -> None:
        self.saved = Saved()
        self.session = requests.session()
        self.session.cookies.set("PLAY_SESSION", self.saved.get(username, ""))
        self.session.headers = {
            "User-Agent": "mxios/5438 CFNetwork/1325.0.1 Darwin/21.1.0"
        }
        self.info = {}
        self.initialize(username, password)

    def initialize(self, username: str, password: str) -> None: #login
        if self.authorized():
            return
        #follows = self.session.get("https://monoxer.com/api/user/my/follows")
        #clientVersions = self.session.get("https://monoxer.com/api/clientVersions")
        #allPoints = self.session.get("https://monoxer.com/api/user/my/allPoints")
        #structure = self.session.get("https://monoxer.com/api/my/orgs/structure")
        #threads = self.session.get("https://monoxer.com/api/user/my/threads")
        #bookCollections = self.session.get("https://monoxer.com/api/bookCollections")
        #plans = self.session.get("https://monoxer.com/api/user/my/plans?status=0")
        #"not authorized"

        auth = self.session.post(
            "https://monoxer.com/api/auth",
            data={
                "email": username,
                "password": password
            }
        )
        dprint(auth.status_code, auth.text)
        self.info.update(auth.json())

        self.saved.set(username, auth.cookies.get("PLAY_SESSION"))

    def authorized(self) -> bool:
        return not (self.session.get("https://monoxer.com/api/user/my/plans?status=0").text == "\"not authorized\"")

    def get_notices(self) -> list[dict]:
        notices = self.session.get("https://monoxer.com/api/notices")
        notices_user = self.session.get(f"https://monoxer.com/api/notices/user/{self.info['user']['id']}")
        return notices.json()

    def do_all(self) -> None:
        classes = self.get_classes()
        for c in classes:
            for task in c.tasks:
                self.do_task(task)

    def get_classes(self) -> list[models.Class]:
        classes = self.session.get("https://monoxer.com/api/user/my/classes")
        dprint(classes.status_code, classes.text)
        return [models.Class(i) for i in classes.json()]

    def do_task(self, task: models.Task) -> bool:
        ...

def main():
    with open("config.json", "r", encoding="utf-8") as f:
        j = json.load(f)
    processor = Processor(j["username"], j["password"])
    processor.do_all()
    print("All-Done")

if __name__ == "__main__":
    main()