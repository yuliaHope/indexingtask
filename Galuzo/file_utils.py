import os


def file_size(file_name):
    stat_info = os.stat(file_name)
    return stat_info.st_size


def write(items, path_to_file, method):
    new_file_name = path_to_file + '.hashes_' + method.lower()
    f = open(new_file_name, 'w')
    for item in items:
        f.write(str(item) + '\n')
    f.close()
