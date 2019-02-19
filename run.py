import argparse

from os import listdir
from os.path import isfile, join

from user_stats_parser import UserStatsParser


def main():
    args = parse_args()
    html_files = [f for f in listdir(args.folder) if isfile(join(args.folder, f)) and '.html' in f]
    user_stats = process_files(args.folder, html_files)


def process_files(folder, files):
    user_stats_parser = UserStatsParser()
    file_template = "%s/messages%s.html"
    user_stats_parser.process_file(file_template % (folder, ''))
    # TODO: iterate over: range(1, len(files))


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('folder', help='Folder where the backup is located')
    return parser.parse_args()


if __name__ == '__main__':
    main()
