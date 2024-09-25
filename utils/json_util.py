import json


class JsonUtil:

    @staticmethod
    def read_file(path):
        with open(path, 'r', encoding='utf-8') as rf:
            data = json.load(rf)
            return data

    @staticmethod
    def save_file(path, data):
        with open(path, 'w', encoding='utf-8') as wf:
            wf.write(json.dumps(data, ensure_ascii=False, indent=4))
