list = [5, 1, 8, 92, -1, 30]
# num = int(input("Input a number: "))
# for i in range(len(list)):
#     if num == list[i]:
#         print(f"{num} is at position {i + 1}")
#         break
#     elif num != list[i]:
#         print("Number not found")
#         break

# sum = 0
# for i in range(len(list)):
#     sum += list[i]
# print(f"Sum of all numbers: {sum}")

print("Input the list of numbers.\nEnter 0 to finish.")
list_num = []
while True:    
    n = int(input())
    if n == 0:
        break
    else:
        list_num.append(n)
sum = 0
for i in range(len(list_num)):
    sum += list_num[i]
print(f"Sum of numbers in list: {sum}")
