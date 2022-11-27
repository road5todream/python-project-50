from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def formatter(format):
    if format == 'stylish':
        return format_stylish
    if format == 'plain':
        return format_plain
    if format == 'json':
        return format_json
