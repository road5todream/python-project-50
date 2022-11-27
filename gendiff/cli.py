import argparse


def parse_cli_args():
    parser = argparse.ArgumentParser(description='Compares two configuration\
                        files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        default='stylish',
                        choices=['stylish', 'plain', 'json'],
                        help='set format of output')

    args = parser.parse_args()
    return args.first_file.lower(), args.second_file.lower(), args.format


path1, path2, format_name = parse_cli_args()
