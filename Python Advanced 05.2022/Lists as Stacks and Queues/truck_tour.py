from collections import deque

number_gas_stations = int(input())

gas_stations_queue = deque()

for num in range(1, number_gas_stations + 1):
    gas_stations_queue.append([int(el) for el in input().split()])

for attempt in range(0, number_gas_stations):

    trunk = 0
    failed = False

    for gas_station in gas_stations_queue:

        petrol = gas_station[0]
        distance = gas_station[1]

        trunk = (trunk + petrol) - distance

        if trunk < 0:
            failed = True
            break

    if failed:
        gas_stations_queue.append(gas_stations_queue.popleft())
    else:
        print(attempt)
        break
