# ex_5_1.py

import argparse
import sys

def line_count(infile):
    with open(infile, 'r') as file:
        lines = file.readlines()
        line_count = len(lines)
        print("Number of lines:", line_count)

def main():
    # Instantiate ArgumentParser
    parser = argparse.ArgumentParser(description="This program prints the number of lines in infile.")

    # Add positional argument
    parser.add_argument("infile", help="Input file name")

    # Parse the arguments
    args = parser.parse_args()

    # Call line_count with the infile argument
    line_count(args.infile)

if __name__ == "__main__":
    main()
