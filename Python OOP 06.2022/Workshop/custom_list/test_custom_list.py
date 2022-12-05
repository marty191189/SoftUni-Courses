from custom_list import CustomList

from unittest import main, TestCase

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
            returned_element = custom_list.get(-2)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_extend_appends_new_values(self):
        pass

    def test_extend_with_non_iterable_raises(self):
        pass


if __name__ == "__main__":
    main()
