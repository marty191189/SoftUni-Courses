from unittest import main, TestCase
from custom_list import CustomList

CUSTOM_INDEX_ERROR_MESSAGE = "Invalid index."

class TestCustomList(TestCase):

    def test_append_adds_element_at_the_end_of_the_list(self):

        custom_list = CustomList()
        self.assertEqual([], custom_list._CustomList__values)

        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

    def test_remove_element_invalid_index_raises(self):

        custom_list = CustomList()
        self.assertEqual([], custom_list._CustomList__values)

        with self.assertRaises(IndexError) as error:
            custom_list.remove(0)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_pass_invalid_integer_index_to_remove_raises(self):

        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        with self.assertRaises(ValueError) as error:
            custom_list.remove("0")
        self.assertEqual("Index is not a valid integer. Please pass a integer number.", str(error.exception))

    def test_remove_element_removes_and_returns(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        returned_element = custom_list.remove(0)

        self.assertEqual([], custom_list._CustomList__values)
        self.assertEqual(5, returned_element)

    def test_get_returns_element(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        returned_element = custom_list.get(0)
        self.assertEqual(5, returned_element)
        self.assertEqual([5], custom_list._CustomList__values)

    def test_get_invalid_index_raises(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        with self.assertRaises(IndexError) as error:
            custom_list.get(-2)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

        with self.assertRaises(IndexError) as error:
            custom_list.get(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_extend_appends_new_values(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_list._CustomList__values)

    def test_extend_with_non_iterable_raises(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        with self.assertRaises(ValueError) as error:
            custom_list.extend(15)
        self.assertEqual("Extend method only works with iterable objects.", str(error.exception))

    def test_extend_returns_new_list(self):
        custom_list = CustomList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomList__values)

        result_list = custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_list._CustomList__values)
        self.assertEqual([5, 2, 3, 4], result_list)

        self.assertNotEqual(id(result_list), id(custom_list._CustomList__values))


if __name__ == "__main__":
    main()
