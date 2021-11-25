district = ['BD', 'BTL', 'CG', 'DD', 'HBT']
pop = ['247100', '333300', '266800', '420900', '318000']
area = ['9.224', '43.35', '12.04', '9.96', '10.09']
density = []
sum = 0
print("Population density of: ")
for i in range(len(pop)):
    density = int(pop[i]) / float(area[i])
    print(f"- {district[i]}: {density}")
    sum += density
print(f"Average population density: {sum / len(district)}")