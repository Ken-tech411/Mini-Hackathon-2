# list = [5, 1, 8, 92, 7, 30]
even_num = []
# for i in range(len(list)):
#     if list[i] % 2 == 0:
#         even_num.append(list[i])
# print(f"Even numbers: {even_num}")

print("Input the list of numbers.\nEnter 0 to finish.")
list_num = []
while True:
    n = int(input())
    if n == 0:
        break
    else:
        list_num.append(n)
for i in range(len(list_num)):
    if list_num[i] % 2 == 0:
        even_num.append(list_num[i])
print(f"Even numbers: {even_num}")