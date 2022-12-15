from os.path import splitext
import json
import yaml


def read_file(path_file):
    with open(path_file) as f:
        data = f.read()
        return data


def get_format(path_file):
    extension = splitext(path_file)[1].lstrip('.')
    return extension


def parse(data, format):
    if format == 'json':
        return json.loads(data)
    if format in ('yml', 'yaml'):
        return yaml.safe_load(data)
