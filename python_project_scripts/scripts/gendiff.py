import argparse
import json
from python_project_scripts import generate_diff

def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.",
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')

    parser.add_argument('-f', '--format', help='set format of output')

    args = parser.parse_args()

    file1_path = args.first_file
    file2_path = args.second_file

    file1 = json.load(open(file1_path))
    file2 = json.load(open(file2_path))

    print(generate_diff(file1, file2))

if __name__ == "__main__":
    main()