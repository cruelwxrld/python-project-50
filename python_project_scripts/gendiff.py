import argparse
import json
from pathlib import Path

import yaml

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
    format_output = args.format

    file1_path = args.first_file
    file2_path = args.second_file

    format_output = args.format

    if not format_output:
        suffix = Path(file1_path).suffix.lower()

        if suffix == '.json':
            format_output = 'json'

        elif suffix == '.yaml':
            format_output = 'yaml'

        elif suffix == '.yml':
            format_output = 'yml'

    try:
        if format_output == 'json':
            file1 = json.load(open(file1_path))
            file2 = json.load(open(file2_path))

            print(generate_diff(file1, file2))
        elif format_output == 'yaml' or format_output == 'yml':
            file1 = yaml.load(open(file1_path), Loader=yaml.SafeLoader)
            file2 = yaml.load(open(file2_path), Loader=yaml.SafeLoader)

            print(generate_diff(file1, file2))
    except FileNotFoundError as e:
        print('{}'.format(e))


if __name__ == "__main__":
    main()