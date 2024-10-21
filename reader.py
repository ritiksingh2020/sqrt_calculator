import json

class ReaderClass:

    def __init__(self, file) -> None:
        self.file = file

    def fetch_json(self):
        with open(self.file,"r") as reader:
            data = json.load(reader)
            return data


# result = ReaderClass("numbers_vendor_A.json").fetch_json()
# print(type(result))