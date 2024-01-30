employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# expected output
# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
for keys in employees:
    print(dict(keys,defaults))