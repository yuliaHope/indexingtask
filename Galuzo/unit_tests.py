import unittest
import calculate_hash as ch
from validation import is_power_of_two


class TestStringMethods(unittest.TestCase):

    def test_is_power_of_two(self):
        self.assertTrue(1024)
        with self.assertRaises(ValueError):
            is_power_of_two(512)
            is_power_of_two(7)
            is_power_of_two(1048578)

    def test_calculate_hash(self):
        test_str = str.encode('Test Line')
        self.assertEqual(ch.calculate_hash(test_str, 'md5'), '79eda7d7a89ffec20feccd9f3b84fd75')
        self.assertEqual(ch.calculate_hash(test_str, 'MD5'), '79eda7d7a89ffec20feccd9f3b84fd75')
        self.assertEqual(ch.calculate_hash(test_str, 'crc32'), '8D2CC4BA')
        self.assertEqual(ch.calculate_hash(test_str, 'CRC32'), '8D2CC4BA')
        self.assertEqual(ch.calculate_hash(test_str, 'sha2'), '0a0c12d072612d5e933d97bc74c7c3daf30661d2761d6640c33023c12a7309f5')
        self.assertEqual(ch.calculate_hash(test_str, 'SHA2'), '0a0c12d072612d5e933d97bc74c7c3daf30661d2761d6640c33023c12a7309f5')
        self.assertEqual(ch.calculate_hash(test_str, 'sha1'), '8f12a90ab3bec0638f618e4e0c3f0414443d6425')
        self.assertEqual(ch.calculate_hash(test_str, 'SHA1'), '8f12a90ab3bec0638f618e4e0c3f0414443d6425')


if __name__ == '__main__':
    unittest.main()

