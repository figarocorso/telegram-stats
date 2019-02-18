import argparse

from os import listdir
from os.path import isfile, join


def main():
    args = parse_args()
    html_files = [f for f in listdir(args.folder) if isfile(join(args.folder, f)) and '.html' in f]
    print(html_files)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder where the backup is located')
    return parser.parse_args()


if __name__ == '__main__':
    main()
