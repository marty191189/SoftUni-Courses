number_of_bottles = int(input())

total_detergent = number_of_bottles * 750

counter = 0
counter_d = 0
counter_p = 0

while total_detergent >= 0:

    number_of_objects = input()

    counter += 1

    if number_of_objects == "End":
        break

    number_of_objects_int = int(number_of_objects)

    if counter % 3 == 0:
        total_detergent = total_detergent - (number_of_objects_int * 15)
        counter_p += number_of_objects_int

    else:
        total_detergent = total_detergent - (number_of_objects_int * 5)
        counter_d += number_of_objects_int

if total_detergent < 0:
    print(f"Not enough detergent, {abs(total_detergent)} ml. more necessary!")

if total_detergent >= 0:
    print("Detergent was enough!")
    print(f"{counter_d} dishes and {counter_p} pots were washed.")
    print(f"Leftover detergent {total_detergent} ml.")
