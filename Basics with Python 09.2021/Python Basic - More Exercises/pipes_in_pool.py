volume_pool_litres = int(input())
power_first_pump = int(input())
power_second_pump = int(input())
hours_without_worker = float(input())

filled_first_pump = power_first_pump * hours_without_worker

filled_second_pump = power_second_pump * hours_without_worker

filled_both_pumps = filled_first_pump + filled_second_pump

perc_pool_full = (filled_both_pumps * 100) / volume_pool_litres

perc_first_pump = (filled_first_pump * 100) / filled_both_pumps

perc_second_pump = (filled_second_pump * 100) / filled_both_pumps

if volume_pool_litres >= filled_both_pumps:
    print(f"The pool is {perc_pool_full:.2f}% full. Pipe 1: {perc_first_pump:.2f}%. Pipe 2: {perc_second_pump:.2f}%.")

else:
    diff = abs(filled_both_pumps - volume_pool_litres)
    print(f"For {hours_without_worker:.2f} hours the pool overflows with {diff:.2f} liters.")
