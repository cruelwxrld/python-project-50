import json


def generate_diff(first_file: json, second_file: json) -> str:
    result = []

    all_keys = sorted(set(first_file.keys()) | set(second_file.keys()))

    for key in all_keys:
        if key in first_file and key not in second_file:
            result.append(f"  - {key}: {first_file[key]}")
        elif key not in first_file and key in second_file:
            result.append(f"  + {key}: {second_file[key]}")
        elif first_file[key] != second_file[key]:
            result.append(f'  - {key}: {first_file[key]}')
            result.append(f'  + {key}: {second_file[key]}')
        else:
            result.append(f"    {key}: {first_file[key]}")

    return '{\n' + '\n'.join(result) + '\n}'
