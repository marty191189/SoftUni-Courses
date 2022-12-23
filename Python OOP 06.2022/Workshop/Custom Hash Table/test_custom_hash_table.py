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

    def test_set_item_dunder_replace_value_of_existing_key(self):
        table = HashTable()
        table["name"] = "Test"

        self.assertEqual("Test", table["name"])

        table["name"] = "New Test"

        self.assertEqual("New Test", table["name"])

    def test_table_is_full_set_item_dunder_resizes(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 25
        table["is_pet_owner"] = True
        table["weight"] = 100

        self.assertEqual(4, table.size())
        self.assertEqual(4, table.max_capacity)

        table["some"] = "Test"

        self.assertEqual(5, table.size())
        self.assertEqual(8, table.max_capacity)

    def test_set_item_collision_linear_approach_is_taken(self):
        table = HashTable()
        table["name"] = "Peter"

        occupied_index = table._HashTable__keys.index("name")

        self.assertEqual(1, occupied_index)

        expected_index = table._HashTable__calc_index("age")

        # Collision will happen
        self.assertEqual(1, expected_index)

        # Actual index should be the next available one
        table["age"] = 0
        self.assertEqual(2, table._HashTable__keys.index("age"))

    def test_set_item_dunder_linear_approach_starts_at_the_begging_when_reaches_end(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 25
        table["is_pet_owner"] = True

        self.assertEqual([None, "name", "age", "is_pet_owner"], table._HashTable__keys)

        table["weight"] = 100

        self.assertEqual(["weight", "name", "age", "is_pet_owner"], table._HashTable__keys)

    def test_size_returns_only_occupied_places_count(self):
        table = HashTable()
        table["name"] = "Peter"

        self.assertEqual(4, table.max_capacity)

        result = table.size()
        self.assertEqual(1, result)

        table["age"] = 0
        result = table.size()
        self.assertEqual(2, result)
        self.assertEqual(4, table.max_capacity)

    def test_add_adds_pair(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)
        table.add("age", 12)
        self.assertEqual([None, "age", None, None], table._HashTable__keys)

    def test_str_dunder(self):
        table = HashTable()
        table["name"] = "Peter"
        table["age"] = 1

        actual_result = table.__str__()
        expected_result = "{name: Peter, age: 1}"

        self.assertEqual(expected_result, actual_result)

    def test_get_non_existing_key_returns_none(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)

        result = table.get("test key")

        self.assertEqual(None, result)

    def test_get_with_default_value(self):
        table = HashTable()
        self.assertEqual([None, None, None, None], table._HashTable__keys)

        result = table.get("test key", "default value")

        self.assertEqual("default value", result)

    def test_get_existing_key_returns_value(self):
        table = HashTable()
        table["name"] = "Peter"

        result = table.get("name")

        self.assertEqual("Peter", result)

    def test_len_returns_max_capacity(self):
        table = HashTable()
        self.assertEqual(4, table.max_capacity)

        table["name"] = "Peter"

        self.assertEqual(4, table.max_capacity)

        result = len(table)

        self.assertEqual(4, result)

if __name__ == "__main__":
    main()
