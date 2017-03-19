import hashlib
import binascii


def crc32(chunk):
    res = (binascii.crc32(chunk) & 0xFFFFFFFF)
    return "%08X" % res


def calculate_hash(chunk, method):
    if method.upper() == 'MD5':
        return hashlib.md5(chunk).hexdigest()
    elif method.upper() == 'SHA1':
        return hashlib.sha1(chunk).hexdigest()
    elif method.upper() == 'CRC32':
        return crc32(chunk)
    elif method.upper() == 'SHA2':
        return hashlib.sha256(chunk).hexdigest()
