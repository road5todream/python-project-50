from gendiff.generate import generate_diff
from tests import get_path
from os.path import splitext
import pytest


@pytest.mark.parametrize(
    "file1, file2, format, expected",
    [
        pytest.param(
            'file1.json',
            'file2.json',
            'stylish',
            'correct1.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file1.yaml',
            'file2.yaml',
            'stylish',
            'correct1.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file3.json',
            'file4.json',
            'stylish',
            'correct2.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file3.yaml',
            'file4.yaml',
            'stylish',
            'correct2.txt',
            id="flat_yaml_file"
        ),
        pytest.param(
            'file3.json',
            'file4.json',
            'plain',
            'correct3.txt',
            id="flat_json_file"
        ),
        pytest.param(
            'file3.json',
            'file4.json',
            'json',
            'correct4.txt',
            id="flat_json_file"
        )
    ]
)
def test_gen_diff(file1, file2, format, expected):
    expected_path = get_path(expected)
    with open(expected_path, 'r') as file:
        result = file.read()
        file1 = get_path(file1)
        file2 = get_path(file2)
        assert generate_diff(file1, file2, format) == result
