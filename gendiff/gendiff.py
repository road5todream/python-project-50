from gendiff.formatters import formatter
from collections import OrderedDict
from gendiff.parser import parse
from gendiff.parser import read_file
from gendiff.parser import get_format
from gendiff.formatters.normal import normal_values


def difference(dic1, dic2):
    dic_new = {}
    sorted_keys = sorted(list(set(dic1.keys()) | set(dic2.keys())))
    for key in sorted_keys:
        if key in dic1 and key not in dic2:
            dic_new[key] = {'status': 'removed',
                            'value': dic1[key]}
        elif key in dic2 and key not in dic1:
            dic_new[key] = {'status': 'added',
                            'value': dic2[key]}
        elif isinstance(dic1[key], dict) and isinstance(dic2[key], dict):
            child = difference(dic1[key], dic2[key])
            dic_new[key] = {'status': 'nested',
                            'value': child}
        elif dic1[key] == dic2[key]:
            dic_new[key] = {'status': 'unchanged',
                            'value': dic2[key]}
        else:
            dic_new[key] = {'status': 'changed',
                            'old': dic1[key],
                            'new': dic2[key]}
    return OrderedDict(sorted(dic_new.items()))


def generate_diff(path_file1, path_file2, format='stylish'):
    parc_data1 = parse(read_file(path_file1), get_format(path_file1))
    parc_data2 = parse(read_file(path_file2), get_format(path_file2))
    diff = difference(normal_values(parc_data1), normal_values(parc_data2))
    diff = formatter(format)(diff)
    return diff
