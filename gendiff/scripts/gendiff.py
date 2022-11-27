from gendiff.generate import generate_diff
from gendiff.cli import path1, path2, format_name


def main():
    print(generate_diff(path1, path2, format_name))


if __name__ == '__main__':
    main()
