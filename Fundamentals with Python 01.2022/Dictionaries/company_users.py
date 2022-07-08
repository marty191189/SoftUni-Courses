command = input()

company_dict = {}

while not command == "End":
    data = command.split(" -> ")

    company_name = data[0]
    employee_id = data[1]

    if company_name not in company_dict:
        company_dict[company_name] = []
        company_dict[company_name].append(employee_id)

    else:
        if employee_id not in company_dict[company_name]:
            company_dict[company_name].append(employee_id)

    command = input()

for key, value in company_dict.items():
    print(f"{key}")

    for el in value:
        print(f"-- {''.join(el)}")
