#!/usr/bin/env python3

# Created by: Andrei Chirilov
# Created on: September 2019
# This program calculated the sum of two integers


def main():
    # this function calculates the total of two integers

    # input
    integer1 = int(input("Enter integer1: "))
    integer2 = int(input("Enter integer2: "))

    # process
    total = integer1 + integer2

    # output
    print("")
    print("The total sum of the two integers is: {}".format(total))


if __name__ == "__main__":
    main()
