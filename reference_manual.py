from color_code import MAJOR_COLORS, MINOR_COLORS, color_pair_to_string, get_color_from_pair_number

def print_reference_manual():
    print("Color Code Reference Manual")
    print("----------------------------")
    for pair_number in range(1, 26):
        major_color, minor_color = get_color_from_pair_number(pair_number)
        color_pair_str = color_pair_to_string(major_color, minor_color)
        print(f'{pair_number:2}: {color_pair_str}')
