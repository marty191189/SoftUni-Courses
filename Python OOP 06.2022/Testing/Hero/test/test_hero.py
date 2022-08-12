from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    ATTACKER_USERNAME = "ATTACKER"
    HERO_LEVEL = 10
    HERO_HEALTH = 100
    HERO_DAMAGE = 75

    BATTLE_LEVEL_INCREMENT = 1
    BATTLE_HEALTH_INCREMENT = 5
    BATTLE_DAMAGE_INCREMENT = 5

    def setUp(self) -> None:
        self.attacker = Hero(self.ATTACKER_USERNAME, self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)

    def test_mammal_is_initialized_correctly(self):
        self.assertEqual(self.ATTACKER_USERNAME, self.attacker.username)
        self.assertEqual(self.HERO_LEVEL, self.attacker.level)
        self.assertEqual(self.HERO_HEALTH, self.attacker.health)
        self.assertEqual(self.HERO_DAMAGE, self.attacker.damage)

    def test_battle_raises_when_attacker_attacks_enemy_with_same_username(self):
        enemy = Hero(self.ATTACKER_USERNAME, 5, 20, 30)

        with self.assertRaises(Exception) as exception:
            self.attacker.battle(enemy)

        self.assertEqual("You cannot fight yourself", str(exception.exception))

    def test_battle_raises_when_attacker_is_dead(self):
        enemy = Hero("Enemy", 5, 20, 30)
        self.attacker.health = 0

        with self.assertRaises(ValueError) as exception:
            self.attacker.battle(enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(exception.exception))

    def test_battle_raises_when_enemy_is_dead(self):
        enemy_username = "Enemy"
        enemy = Hero(enemy_username, 5, 0, 30)

        with self.assertRaises(ValueError) as exception:
            self.attacker.battle(enemy)

        self.assertEqual(f"You cannot fight {enemy_username}. He needs to rest", str(exception.exception))

    def test_battle_returns_draw_when_both_enemies_die(self):
        enemy = Hero("Enemy", self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)

        result = self.attacker.battle(enemy)

        expected_health = self.HERO_HEALTH - (self.HERO_LEVEL * self.HERO_DAMAGE)

        self.assertEqual("Draw", result)
        self.assertEqual(expected_health, self.attacker.health)
        self.assertEqual(expected_health, enemy.health)

    def test_battle_returns_win_when_enemy_dies(self):
        enemy_level = 5
        enemy_health = 100
        enemy_damage = 10
        enemy = Hero("Enemy", enemy_level, enemy_health, enemy_damage)

        result = self.attacker.battle(enemy)

        expected_enemy_health = enemy_health - (self.HERO_LEVEL * self.HERO_DAMAGE)
        expected_attacker_level = self.HERO_LEVEL + self.BATTLE_LEVEL_INCREMENT
        expected_attacker_damage = self.HERO_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        expected_attacker_health = self.HERO_HEALTH - (enemy_level * enemy_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You win", result)
        self.assertEqual(expected_enemy_health, enemy.health)
        self.assertEqual(expected_attacker_level, self.attacker.level)
        self.assertEqual(expected_attacker_damage, self.attacker.damage)
        self.assertEqual(expected_attacker_health, self.attacker.health)

    def test_battle_returns_lost_when_attacker_dies(self):
        attacker_level = 5
        attacker_health = 100
        attacker_damage = 10
        attacker = Hero("Attacker", attacker_level, attacker_health, attacker_damage)
        enemy = Hero("Enemy", self.HERO_LEVEL, self.HERO_HEALTH, self.HERO_DAMAGE)

        result = attacker.battle(enemy)

        expected_attacker_health = attacker_health - (self.HERO_LEVEL * self.HERO_DAMAGE)
        expected_enemy_level = self.HERO_LEVEL + self.BATTLE_LEVEL_INCREMENT
        expected_enemy_damage = self.HERO_DAMAGE + self.BATTLE_DAMAGE_INCREMENT
        expected_enemy_health = self.HERO_HEALTH - (attacker_level * attacker_damage) + self.BATTLE_HEALTH_INCREMENT

        self.assertEqual("You lose", result)
        self.assertEqual(expected_attacker_health, attacker.health)
        self.assertEqual(expected_enemy_level, enemy.level)
        self.assertEqual(expected_enemy_damage, enemy.damage)
        self.assertEqual(expected_enemy_health, enemy.health)

    def test_str_method(self):
        expected_result = f"Hero {self.ATTACKER_USERNAME}: {self.HERO_LEVEL} lvl\n" \
               f"Health: {self.HERO_HEALTH}\n" \
               f"Damage: {self.HERO_DAMAGE}\n"

        actual_result = self.attacker.__str__()

        self.assertEqual(expected_result, actual_result)


if __name__ == "__main__":
    main()
