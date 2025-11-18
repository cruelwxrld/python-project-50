def test_all_format():
    import json
    import os
    import subprocess
    import tempfile

    import yaml

    with (tempfile.NamedTemporaryFile(mode='w', suffix=".json", delete=False)
          as file1):
        json.dump({'a': 1, 'b': 2}, file1)
        json1 = file1.name

    with (tempfile.NamedTemporaryFile(mode='w', suffix=".json", delete=False)
          as file2):
        json.dump({'a': 1}, file2)
        json2 = file2.name

    with (tempfile.NamedTemporaryFile(mode='w', suffix=".yaml", delete=False)
          as file1yml):
        yaml.dump({'a': 1, 'b': 2}, file1yml)
        yaml1 = file1yml.name

    with (tempfile.NamedTemporaryFile(mode='w', suffix=".yaml", delete=False)
          as file2yml):
        yaml.dump({'a': 1}, file2yml)
        yaml2 = file2yml.name

    try:
        result1 = subprocess.run(['gendiff', json1, json2],
                                 capture_output=True, text=True)
        result2 = subprocess.run(['gendiff', yaml1, yaml2],
                                 capture_output=True, text=True)

        assert '- b: 2' in result1.stdout
        assert '- b: 2' in result2.stdout

    finally:
        for file in [json1, json2, yaml1, yaml2]:
            os.unlink(file)