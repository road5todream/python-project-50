def to_str(element, depth):
    if isinstance(element, dict):
        string = ['{']
        for key, value in element.items():
            string.append(
                '\n' + '  ' * depth + '  ' + str(key) + ': ' + str(
                    to_str(value, depth + 2)))
        string.append('\n' + '  ' * (depth - 1) + '}')
        result = ''.join(string)
        return result
    else:
        return element


def new_status(status):
    if status == 'unchanged':
        status = '  '
    elif status == 'added':
        status = '+ '
    else:
        status = '- '
    return status


def stylish(diff, depth=1):
    line = []
    for key, value in diff.items():
        if value['status'] == 'nested':
            line.append('  ' * depth + '  ' + str(key) + ': {' '\n')
            line.append(stylish(value['value'], depth + 2))
            line.append('  ' * (depth + 1) + '}' + '\n')
        elif value['status'] == 'changed':
            line.append(
                '  ' * depth + '- ' + str(key) + ': ' + str(
                    to_str(value['old'], depth + 2)) + '\n')
            line.append(
                '  ' * depth + '+ ' + str(key) + ': ' + str(
                    to_str(value['new'], depth + 2)) + '\n')
        else:
            line.append(
                '  ' * depth + new_status(
                    value['status']) + str(key) + ': ' + str(
                    to_str(value['value'], depth + 2)) + '\n')
    result = ''.join(line)
    return result


def format_stylish(diff):
    diff = stylish(diff)
    result = '{' + '\n' + diff + '}'
    return result
