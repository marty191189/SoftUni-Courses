from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.name = "Pesho"
        self.mammal_type = "Mammal_Type"
        self.sound = "sound"
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_is_initialized_correctly(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_makes_correct_sound(self):
        expected_result = f"{self.name} makes {self.sound}"
        actual_result = self.mammal.make_sound()

        self.assertEqual(expected_result, actual_result)

    def test_kingdom_returns_animals(self):
        expected_result = "animals"
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(expected_result, actual_result)

    def test_info_method(self):
        expected_result = f"{self.name} is of type {self.mammal_type}"
        actual_result = self.mammal.info()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
