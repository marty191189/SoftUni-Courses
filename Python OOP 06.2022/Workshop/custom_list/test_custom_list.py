from unittest import main, TestCase
from custom_list import CustomIntList, NoElementsInTheListError, NoSuchValueError

CUSTOM_INDEX_ERROR_MESSAGE = "Invalid index."
CUSTOM_DATA_INDEX_ERROR_MESSAGE = "Index is not a valid integer. Please pass a integer number."

class TestCustomIntList(TestCase):

    def test_append_adds_element_at_the_end_of_the_list(self):

        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

    def test_append_non_integer_raises(self):
        custom_list = CustomIntList()

        with self.assertRaises(ValueError) as error:
            custom_list.append("5")
        self.assertEqual("Only integers are accepted!", str(error.exception))

    def test_remove_element_invalid_index_raises(self):

        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        with self.assertRaises(IndexError) as error:
            custom_list.remove(0)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_pass_invalid_integer_index_to_remove_raises(self):

        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        with self.assertRaises(ValueError) as error:
            custom_list.remove("0")
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_remove_element_removes_and_returns(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        returned_element = custom_list.remove(0)

        self.assertEqual([], custom_list._CustomIntList__values)
        self.assertEqual(5, returned_element)

    def test_get_returns_element(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        returned_element = custom_list.get(0)
        self.assertEqual(5, returned_element)
        self.assertEqual([5], custom_list._CustomIntList__values)

    def test_get_invalid_index_raises(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        with self.assertRaises(IndexError) as error:
            custom_list.get(-2)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

        with self.assertRaises(IndexError) as error:
            custom_list.get(1)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_extend_appends_new_values(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_list._CustomIntList__values)

    def test_extend_non_integer_raises(self):
        custom_list = CustomIntList()

        with self.assertRaises(ValueError) as error:
            custom_list.extend([5, "10"])
        self.assertEqual("Only integers are accepted!", str(error.exception))

    def test_extend_with_non_iterable_raises(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        with self.assertRaises(ValueError) as error:
            custom_list.extend(15)
        self.assertEqual("Extend method only works with iterable objects.", str(error.exception))

    def test_extend_returns_new_list(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        result_list = custom_list.extend([2, 3, 4])
        self.assertEqual([5, 2, 3, 4], custom_list._CustomIntList__values)
        self.assertEqual([5, 2, 3, 4], result_list)

        self.assertNotEqual(id(result_list), id(custom_list._CustomIntList__values))

    def test_insert_invalid_index_raises(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        with self.assertRaises(IndexError) as error:
            custom_list.insert(0, 5)
        self.assertEqual(CUSTOM_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_insert_invalid_index_data_type_raises(self):
        custom_list = CustomIntList()
        custom_list.append(5)

        self.assertEqual([5], custom_list._CustomIntList__values)

        with self.assertRaises(ValueError) as error:
            custom_list.insert("0", 5)
        self.assertEqual(CUSTOM_DATA_INDEX_ERROR_MESSAGE, str(error.exception))

    def test_insert_returns_the_list_with_inserted_elements(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        custom_list.append(10)
        custom_list.append(15)

        self.assertEqual([5, 10, 15], custom_list._CustomIntList__values)

        my_list = custom_list.insert(1, -3)
        self.assertEqual([5, -3, 10, 15], custom_list._CustomIntList__values)
        self.assertEqual(id(my_list), id(custom_list._CustomIntList__values))

    def test_pop_with_no_elements_raises(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        with self.assertRaises(NoElementsInTheListError) as error:
            custom_list.pop()
        self.assertEqual("No elements in the list.", str(error.exception))

    def test_pop_removes_and_returns_elements(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        self.assertEqual([5], custom_list._CustomIntList__values)

        element = custom_list.pop()

        self.assertEqual(5, element)
        self.assertEqual([], custom_list._CustomIntList__values)

    def test_clear_no_elements_returns_empty_list(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        custom_list.clear()

        self.assertEqual([], custom_list._CustomIntList__values)

    def test_clear(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        custom_list.append(15)
        self.assertEqual([5,15], custom_list._CustomIntList__values)

        custom_list.clear()

        self.assertEqual([], custom_list._CustomIntList__values)

    def test_index_left_returns_left_most_index_of_the_element(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        custom_list.append(15)
        custom_list.append(5)
        self.assertEqual([5, 15, 5], custom_list._CustomIntList__values)

        index = custom_list.index_left(5)
        self.assertEqual(0, index)

    def test_index_right_returns_right_most_index_of_the_element(self):
        custom_list = CustomIntList()
        custom_list.append(5)
        custom_list.append(15)
        custom_list.append(5)
        self.assertEqual([5, 15, 5], custom_list._CustomIntList__values)

        index = custom_list.index_right(5)
        self.assertEqual(2, index)

    def test_index_left_invalid_value_raises(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        with self.assertRaises(NoSuchValueError) as error:
            custom_list.index_left(5)
        self.assertEqual("No such value in the list.", str(error.exception))

    def test_index_right_invalid_value_raises(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        with self.assertRaises(NoSuchValueError) as error:
            custom_list.index_right(5)
        self.assertEqual("No such value in the list.", str(error.exception))

    def test_count_no_such_value(self):
        custom_list = CustomIntList()
        custom_list.append(10)
        self.assertEqual([10], custom_list._CustomIntList__values)

        count = custom_list.count(5)

        self.assertEqual(0, count)

    def test_count(self):
        custom_list = CustomIntList()
        custom_list.append(10)
        custom_list.append(5)
        custom_list.append(10)
        self.assertEqual([10, 5, 10], custom_list._CustomIntList__values)

        count = custom_list.count(10)
        self.assertEqual(2, count)

        count = custom_list.count(5)
        self.assertEqual(1, count)

    def test_reverse_empty_list_returns_list(self):
        custom_list = CustomIntList()
        self.assertEqual([], custom_list._CustomIntList__values)

        custom_list.reverse()

        self.assertEqual([], custom_list._CustomIntList__values)

    def test_reverse_reverses_values_in_the_list(self):
        custom_list = CustomIntList()
        custom_list.append(10)
        custom_list.append(5)
        self.assertEqual([10, 5], custom_list._CustomIntList__values)

        result = custom_list.reverse()

        # The list remains the same
        self.assertEqual([10, 5], custom_list._CustomIntList__values)

        # The result is the reversed list of the values of the original list
        self.assertEqual([5, 10], result)

    def test_copy_returns_same_element_different_list(self):
        custom_list = CustomIntList()
        custom_list.append(10)
        custom_list.append(5)
        self.assertEqual([10, 5], custom_list._CustomIntList__values)

        result = custom_list.copy()

        self.assertEqual([10, 5], result)
        self.assertNotEqual(id(result), id(custom_list._CustomIntList__values))


if __name__ == "__main__":
    main()
