from unittest import main, TestCase
from custom_hash_table import HashTable

class TestHashTable(TestCase):

    def test_init(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        self.assertEqual([None, None, None, None], table._HashTable__values)
        self.assertEqual(4, table.max_capacity)

    def test_get_item_dunder(self):
        table = HashTable()
        table["name"] = "Test"
        table["age"] = 0

        result = table["name"]

        self.assertEqual("Test", result)

    def test_get_item_dunder_non_existing_key_raises(self):
        table = HashTable()
        table["name"] = "Test"
        table["age"] = 0

        with self.assertRaises(KeyError) as error:
            # Non-existing key
            result = table["asd"]
        self.assertEqual("asd", str(error.exception.args[0]))

    def test_set_item_dunder_(self):
        pass

if __name__ == "__main__":
    main()
