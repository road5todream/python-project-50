from os.path import splitext
import json
import yaml


def prepare_data(path_file: str):
    extension = splitext(path_file)[1][1:]
    if extension in ['yaml', 'yml', 'json']:
        with open(path_file) as f:
            data = f.read()
            return data, extension


def parse(data, forma):
    if forma == 'json':
        return json.loads(data)
    if forma in ('yml', 'yaml'):
        return yaml.safe_load(data)
