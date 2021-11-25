district = ['BD', 'BTL', 'CG', 'DD', 'HBT']
pop = ['247100', '333300', '266800', '420900', '318000']
max_pop = pop[0]
min_pop = pop[0]
max_district = district[0]
min_district = district[0]
for i in range(len(district)):
    if int(pop[i]) > int(max_pop):
        max_pop = pop[i]
        max_district = district[i]
    elif int(pop[i]) < int(min_pop):
        min_pop = pop[i]
        min_district = district[i]

max_dis = district.index(max_district)
min_dis = district.index(min_district)
print(f"indices of:\n- Most populated dist.: {max_dis}\n- Least populated dist.: {min_dis}")
print(f"Names of:\n- Most populated dist.: {max_district}\n- Least populated dist.: {min_district}")