from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    FUEL = 100
    HORSE_POWER = 120
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def setUp(self) -> None:
        self.vehicle = Vehicle(self.FUEL, self.HORSE_POWER)

    def test_mammal_is_initialized_correctly(self):
        self.assertEqual(self.FUEL, self.vehicle.fuel)
        self.assertEqual(self.HORSE_POWER, self.vehicle.horse_power)
        self.assertEqual(self.FUEL, self.vehicle.capacity)
        self.assertEqual(self.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)

    def test_drive_raises_error_when_fuel_is_not_enough(self):

        with self.assertRaises(Exception) as exception:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(exception.exception))
        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_drive_reduces_fuel_when_distance_is_reached(self):

        distance = 50
        fuel_needed = self.DEFAULT_FUEL_CONSUMPTION * distance

        self.vehicle.drive(distance)

        expected_result = self.FUEL - fuel_needed
        actual_result = self.vehicle.fuel
        self.assertEqual(expected_result, actual_result)

    def test_drive_reduces_fuel_when_max_reachable_distance(self):

        distance = self.FUEL / self.DEFAULT_FUEL_CONSUMPTION

        self.vehicle.drive(distance)

        self.assertEqual(0, self.vehicle.fuel)

    def test_refuel_raises_error_when_capacity_overflows(self):

        with self.assertRaises(Exception) as exception:
            self.vehicle.refuel(self.vehicle.capacity + 1)
        self.assertEqual("Too much fuel", str(exception.exception))

    def test_refuel_increases_fuel_in_the_car(self):
        fuel_amount = 20
        self.vehicle.fuel -= fuel_amount

        self.vehicle.refuel(fuel_amount)

        self.assertEqual(self.FUEL, self.vehicle.fuel)

    def test_str_method(self):
        expected_result = f"The vehicle has {self.HORSE_POWER} " \
               f"horse power with {self.FUEL} fuel left and {self.DEFAULT_FUEL_CONSUMPTION} fuel consumption"

        actual_result = self.vehicle.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
