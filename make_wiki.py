import csv
from itertools import groupby

import mdutils
import os
from argparse import ArgumentParser


def read_files(files, branch):
    parts = []
    for file in files:
        with open(file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['library'] = '[{0}](../tree/{1}/{0})'.format(os.path.dirname(file), branch)
                row['library_name'] = '{}'.format(os.path.dirname(file))
                #print(row)
                parts.append(row)
    return parts

def write_table(parts, keys, md: mdutils.MdUtils, sort_by='Comment'):
    sorted_parts = sorted(parts, key=lambda i: i[sort_by])

    tabulated = list(keys)
    for part in sorted_parts:
        tabulated.extend([part.get(key) for key in keys])
        #print(part)
    #print(len(keys), len(sorted_parts)+1, len(tabulated))
    md.new_line()
    md.new_table(columns=len(keys), rows=len(sorted_parts)+1, text=tabulated)


def write_designators(parts, keys, md: mdutils.MdUtils, sort_by='designator'):
    parts = sorted(parts, key=lambda i: i[sort_by])
    groups = groupby(parts, lambda i: i[sort_by])
    for designator, group in groups:
        #print('Designator {}'.format(designator))
        md.new_line()
        md.new_header(level=2, title=designator)
        sorted_parts = sorted(group, key=lambda i: i['id'])
        tabulated = list(keys)
        for part in sorted_parts:
            tabulated.extend([part.get(key) for key in keys])
        md.new_line()
        md.new_table(columns=len(keys), rows=len(sorted_parts) + 1, text=tabulated)


if __name__ == "__main__":
    parser = ArgumentParser(description="Extract parts from .SchLib or .LibPkg")
    parser.add_argument("files", nargs='*')
    parser.add_argument("--output", '-o')
    parser.add_argument("--branch", default='master')
    args = parser.parse_args()

    parts = read_files(args.files, args.branch)
    #print(parts)
    mdFile = mdutils.MdUtils(file_name=args.output, title='')
    mdFile.new_paragraph('⚠️ Automatically generated page. Any changes will be overwritten.')
    mdFile.new_line()
    x = mdFile.create_marker('toc')
    mdFile.new_header(level=1, title='By designator')
    write_designators(parts, ['id', 'designator', 'Comment', 'description', 'library'], mdFile, sort_by='designator')
    mdFile.new_header(level=1, title='By library')
    write_designators(parts, ['id', 'designator', 'Comment', 'description', 'library'], mdFile, sort_by='library_name')
    mdFile.new_header(level=1, title='By part number')
    write_table(parts, ['id', 'designator', 'Comment', 'description', 'library'], mdFile)
    mdFile.new_table_of_contents(table_title='Contents', depth=2, marker=x)
    mdFile.create_md_file()

