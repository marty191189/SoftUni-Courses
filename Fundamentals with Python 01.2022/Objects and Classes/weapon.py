class Weapon:

    def __init__(self, bullets):
        self.bullets = bullets

    def shoot(self):

        if self.bullets > 0:
            self.bullets -= 1
            text = "shooting..."
            return text

        else:
            text = "no bullets left"
            return text

    def __repr__(self):
        text = f"Remaining bullets: {self.bullets}"
        return text


# code to test the class
#
# weapon = Weapon(5)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon.shoot())
# print(weapon)
