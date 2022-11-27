def forming_line(status, path, value1='', value2=''):
    arg = 'Property ' + "'" + str(path)[1:] + "'" + ' was '
    if status == 'removed':
        return arg + status
    elif status == 'added':
        return f"{arg}{status} with value: {correct_value(value1)}"
    elif status == 'changed':
        return f"{arg}updated. From {correct_value(value1)} " \
               f"to {correct_value(value2)}"


def correct_value(value=''):
    if isinstance(value, dict):
        value = '[complex value]'
        return value
    elif value not in ['false', 'true', 'null']:
        if isinstance(value, str):
            value = "'" + str(value) + "'"
        return value
    else:
        return str(value)


LINE = []


def plain(dictionary, path=''):
    for key, value in dictionary.items():
        pr = path + '.' + key
        if value['status'] == 'nested':
            plain(value['value'], pr)
        if value['status'] == 'removed':
            LINE.append(forming_line(value['status'], pr) + '\n')
        if value['status'] == 'added':
            LINE.append(forming_line(value['status'],
                                     pr, value['value']) + '\n')
        if value['status'] == 'changed':
            LINE.append(forming_line(value['status'], pr, value['old'],
                                     value['new']) + '\n')
    result = ''.join(LINE)
    return result[0:len(result) - 1]


def format_plain(dictionary):
    result = plain(dictionary)
    return result
