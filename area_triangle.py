#!/usr/bin/env python3

# Created by: Navin Balekomebole
# Created on: Jan 19 2022
# This program uses a function to calculate
# the area of a triangle.


def calc_area(base, height):
    # calculate and print area
    area = base * height / 2
    print("The area is {} cm squared.". format(area))


def main():
    # get input
    base_string = input("Enter the base of this triangle (cm): ")
    height_string = input("Enter the height (cm): ")

    # error checking
    try:
        base_input = float(base_string)
        height_input = float(height_string)
    except Exception:
        print("Invalid input(s).")
    else:
        if base_input <= 0 or height_input <= 0:
            print("Numbers must be positive.")
        else:
            calc_area(base_input, height_input)


if __name__ == "__main__":
    main()
