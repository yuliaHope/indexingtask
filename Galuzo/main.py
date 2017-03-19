from multiprocessing import Pool, cpu_count
import time
import sys
import validation
from calculate_hash import calculate_hash
import file_utils

async_hashes_list = []


def hash_async(chunk, i, method):
    hex_hash = calculate_hash(chunk, method)
    return {'pos': i, 'hash_value': hex_hash}


def collect_results(res):
    global async_hashes_list
    async_hashes_list[res.get('pos')] = res.get('hash_value')


def read_and_hash_async(path_to_file, block_size, method, chunks_count):
    global async_hashes_list
    pool = Pool(9)
    i = 0

    async_hashes_list = [None] * chunks_count
    f_read = open(path_to_file, 'rb')
    start_time = time.time()
    while True:
        chunk = f_read.read(block_size)
        if not chunk:
            break
        pool.apply_async(hash_async, args=(chunk, i, method), callback=collect_results)
        i += 1
    pool.close()
    pool.join()
    end_time = time.time() - start_time
    print('read and hash in async mode: ' + str(end_time))
    print('hashing speed in async mode: ' + str(end_time / chunks_count / 9))
    f_read.close()
    file_utils.write(async_hashes_list, path_to_file, method, 'async')


def read_and_hash_sync(path_to_file, block_size, method, chunks_count):
    f_read = open(path_to_file, 'rb')
    new_file_name = path_to_file + '.hashes_' + method.lower() + '_sync'
    f_write = open(new_file_name, 'a')
    start_time = time.time()
    while True:
        chunk = f_read.read(block_size)
        if not chunk:
            break
        f_write.write(calculate_hash(chunk, method) + '\n')

    f_read.close()
    end_time = time.time() - start_time
    print('read and hash in sync mode: ' + str(end_time))
    print('hashing speed in sync mode: ' + str(end_time / chunks_count))


def main(argv):
    path_to_file = validation.file_is_exist(argv[1])
    block_size = validation.is_power_of_two(int(argv[2]))
    method = validation.method_is_correct(argv[3])
    mode = validation.init_mode(argv)
    chunks_count = int(file_utils.file_size(path_to_file) / block_size) + 1

    if mode.upper() == 'SYNC':
        read_and_hash_sync(path_to_file, block_size, method, chunks_count)
    else:
        read_and_hash_async(path_to_file, block_size, method, chunks_count)


if __name__ == "__main__":
    main(sys.argv)
