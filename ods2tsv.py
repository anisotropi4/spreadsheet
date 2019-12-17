#!/usr/bin/env python3

import pandas as pd
import argparse
import os
import sys

DEBUG=True

if __name__ == '__main__':
    DEBUG = False

parser = argparse.ArgumentParser(description='Dump ods files tab(s) to .tsv files, to the (default output) path')

parser.add_argument('inputfiles', type=str, nargs='*', help='name of ods-file to process')

tabgroup = parser.add_mutually_exclusive_group()

tabgroup.add_argument('--tabnames', dest='tabnames', action='store_true',
                    default=False, help='dump name of tabs')

tabgroup.add_argument('--tab', type=str, dest='tab', default=None,
                    help='name of tab to process')

filegroup = parser.add_mutually_exclusive_group()

filegroup.add_argument('--path', dest='path', type=str, default='output',
                    help='output directory file')

filegroup.add_argument('--csv', dest='csv', action='store_true',
                       default=False, help='csv file output')

filegroup.add_argument('--stdout', dest='stdout', action='store_true',
                    default=False, help='dump a tab to stdout')

parser.add_argument('--sourcename', dest='sourcename', action='store_true',
                    default=False, help='prepend filename to output tab file')


args = parser.parse_args()

path = args.path

delimiter='\t'
extension='tsv'

if DEBUG:
    pd.set_option('display.max_columns', None)
    args.inputfiles = ['bus0112.ods']

if args.csv:
    delimiter=','
    extension='csv'

if not os.path.exists(path):
    os.makedirs(path)

def trim_tabs(tabnames):
    return [tab for tab in tabnames if tab[1:6] not in ['file:', 'http:']]

if args.tabnames:
    for filename in args.inputfiles:
        if len(args.inputfiles) > 1:
            print(filename)
        df = pd.read_excel(filename, None, engine='odf')
        print('\n'.join(trim_tabs(df.keys())))
    sys.exit(0)

for filename in args.inputfiles:    
    if args.tab:
        tab = args.tab
        filebase = ''
        if args.sourcename:
            filebase = filename + ':'
            if '.' in filename:
                filebase = filename.rsplit('.', 1)[0] + ':'
        try:
            df = pd.read_excel(filename, tab, engine='odf')
            if args.stdout:
                df.to_csv(sys.stdout, index=False, sep=delimiter)
            else:
                df.to_csv('{}/{}{}.{}'.format(path, filebase, tab, extension), index=False, sep=delimiter)
        except KeyError:
            pass
    else:
        df = pd.read_excel(filename, None, engine='odf')
        filebase = ''
        if args.sourcename:
            filebase = filename + ':'
            if '.' in filename:
                filebase = filename.rsplit('.', 1)[0] + ':'
        for tab in trim_tabs(df.keys()):
            df[tab].to_csv('{}/{}{}.{}'.format(path, filebase, tab, extension), index=False, sep=delimiter)

