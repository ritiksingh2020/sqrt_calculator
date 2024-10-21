import json


class writerClass:

    def __init__(self,file) -> None:
        self.file = file

    def write_json(self, data:list):
        try:
            with open("result.json", "w") as writer:
                json.dump(data, self.file)
            return True
        except Exception as e:
            print("Failure while writing file with error", e)
            return False
        


        