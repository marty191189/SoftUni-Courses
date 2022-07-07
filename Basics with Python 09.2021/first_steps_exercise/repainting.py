sq_m_nylon = int(input())
litres_of_paint = int(input())
litres_of_paint_thinner = int(input())
hours_of_work = int(input())

price_nylon = 1.50
price_paint = 14.50
price_paint_thinner = 5
price_bags = 0.40

new_nylon = sq_m_nylon + 2
new_paint = litres_of_paint + ((10 / 100) * litres_of_paint)

sum_materials = (new_nylon * price_nylon) + (new_paint * price_paint) + (litres_of_paint_thinner * price_paint_thinner) + price_bags

price_work_for_one_hour = (30 / 100) * sum_materials

sum_work = price_work_for_one_hour * hours_of_work

total_sum = sum_materials + sum_work

print(total_sum)
