from unittest import main, TestCase
from custom_hash_table import HashTable

class TestHashTable(TestCase):

    def test_init(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        self.assertEqual([None, None, None, None], table._HashTable__values)
        self.assertEqual(4, table.max_capacity)

if __name__ == "__main__":
    main()
