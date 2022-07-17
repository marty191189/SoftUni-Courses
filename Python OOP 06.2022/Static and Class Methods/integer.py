def roman_to_int(roman_number):

    rom_val_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0

    for i in range(0, len(roman_number)):

        if i > 0 and rom_val_dict[roman_number[i]] > rom_val_dict[roman_number[i - 1]]:
            int_val += rom_val_dict[roman_number[i]] - 2 * rom_val_dict[roman_number[i - 1]]

        else:
            int_val += rom_val_dict[roman_number[i]]

    return int_val


class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):

        if not isinstance(float_value, float):
            return "value is not a float"

        return cls(int(float_value))

    @classmethod
    def from_roman(cls, value):
        int_number = roman_to_int(value)
        return cls(int_number)

    @classmethod
    def from_string(cls, value):

        if not isinstance(value, str):
            return "wrong type"

        try:
            return cls(int(value))

        except ValueError:
            return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
