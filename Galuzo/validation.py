import os


def file_is_exist(path_to_file):
    if os.path.isfile(path_to_file):
        return path_to_file
    else:
        raise Exception('File ' + path_to_file + ' not found')


def method_is_correct(method):
    methods = ['sha1', 'sha2', 'md5', 'crc32']
    if method.lower() in methods:
        return method
    else:
        raise Exception('incorrect method')


def init_mode(argv):
    if len(argv) == 4:
        return 'async'
    elif len(argv) == 5:
        return argv[4]
    else:
        raise Exception('incorrect parameter for mode')


def is_power_of_two(x):
    if (x >= 1024 or x <= 1024 * 1024) and (x & (x - 1)) == 0:
        return x
    else:
        raise ValueError(str(x) + ' is not power of 2 or bigger/smaller than 1Mb/1Kb')
