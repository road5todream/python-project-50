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


def prepare_plain(value, new_path, line):
    if value['status'] == 'nested':
        plain(value['value'], new_path, line)
    if value['status'] == 'removed':
        line.append(forming_line(value['status'], new_path) + '\n')
    if value['status'] == 'added':
        line.append(forming_line(value['status'],
                                 new_path, value['value']) + '\n')
    if value['status'] == 'changed':
        line.append(forming_line(value['status'], new_path, value['old'],
                                 value['new']) + '\n')


def plain(dictionary, path='', line=''):
    if line == '':
        line = []
    for key, value in dictionary.items():
        new_path = path + '.' + key
        prepare_plain(value, new_path, line)
    result = ''.join(line)
    return result[0:len(result) - 1]


def format_plain(dictionary):
    result = plain(dictionary)
    return result
