def normal_values(file):
    corr_values = {None: 'null', True: 'true', False: 'false'}
    for key, val in file.items():
        if isinstance(val, dict):
            normal_values(val)
        elif isinstance(val, (bool, type(None))):
            file[key] = corr_values[val]
    return file
