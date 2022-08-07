class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):

    def test_cat_size_is_increased_after_eating(self):

        cat = Cat("TestCat")

        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):

        cat = Cat("TestCat")

        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_cat_is_fed_raised_if_eat_again(self):

        cat = Cat("TestCat")

        cat.eat()

        with self.assertRaises(Exception) as exception:
            cat.eat()
        self.assertEqual("Already fed.", str(exception.exception))

    def test_cat_sleep_if_not_fed_raises(self):

        cat = Cat("TestCat")

        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as exception:
            cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(exception.exception))

    def test_cat_is_not_sleepy_after_sleep(self):

        # Arrange
        cat = Cat("TestCat")

        self.assertFalse(cat.fed)

        self.assertFalse(cat.sleepy)

        cat.eat()

        self.assertTrue(cat.sleepy)

        # Act
        cat.sleep()

        # Assert
        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    main()
