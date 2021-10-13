#!/usr/bin/env python3

# Created by: Igor
# Created on: Oct 2021
# This is math_program


def triangle(base, height):
    # This is function for area
    # output
    area = base * height / 2
    print("The area of the triangle is {0} cm²".format(area))


def main():
    # input
    integer1 = input("Enter the base lenght of a triangle (cm): ")
    integer2 = input("Enter the height of a triangle (cm): ")
    try:
        base_from_user = float(integer1)
        height_from_user = float(integer2)
        triangle(base_from_user, height_from_user)

    except Exception:
        print("This was not a number")
    finally:
        print("")
        print("Done.")


if __name__ == "__main__":
    main()
