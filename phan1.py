color_list = ["blue", 'teal', 'green']

print("Color list: ")
for color in color_list:
    print(color, end=', ')
new_color = input("\nInput a new color: ")
color_list.append(new_color)
print(f"New color list:")
for color in color_list:
    print(color, end=', ')