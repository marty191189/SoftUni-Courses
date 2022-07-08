import re

number_of_lines = int(input())

pattern = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]"

all_barcodes_list = []

valid_barcode_dict = {}

current_number = ""

counter_letters = 0

for number in range(1, number_of_lines + 1):
    barcode = input()

    all_barcodes_list.append(barcode)

for barcode in all_barcodes_list:

    matches = re.findall(pattern, barcode)

    if matches:

        for char in barcode:

            if 48 <= ord(char) <= 57:
                current_number += char

            else:
                counter_letters += 1

        if counter_letters == len(barcode):
            current_number = "00"

        if barcode not in valid_barcode_dict:
            valid_barcode_dict[barcode] = current_number

        current_number = ""
        counter_letters = 0

        print(f"Product group: {valid_barcode_dict[barcode]}")

    elif not matches:
        print("Invalid barcode")
