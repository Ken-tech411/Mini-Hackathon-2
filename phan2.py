from turtle import *
color_list = ["blue", 'teal', 'green']
# print("Color list: ")
# for color in color_list:
#     print(color, end=', ')

# pos = int(input("\nInput position: "))
# position = pos - 1
# print(f"Color at position {pos}: {color_list[position]}")

# del_num_item = int(input("Input to delete: ")) - 1
# color_list.remove(color_list[del_num_item])

# del_item = input("Input to delete: ")
# color_list.remove(del_item)
# for color in color_list:
#     print(color, end=', ')

color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'violet']
speed(1)
penup()
goto(-100, 0)
for i in range(len(color_list)):
    pendown()
    color(color_list[i])
    forward(20)
    penup()
    forward(10)
done()