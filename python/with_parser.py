#!/usr/bin/env python

from __future__ import print_function

import argparse
import os, sys

DESCRIPTION="""\
Short description regarding the program
"""

def get_parser():
    """
    Description regarding the function
    :returns: Parser
    :rtypepe: argparse.ArgumentParser
    """

    if x>y:


    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--version', action='version', version='0.0')
    parser.add_argument('--optionalargument', '-o', type=str, metavar='TEST META', help="Help Text for optional Argument")
    subparsers = parser.add_subparsers()

    parser_aaa = subparsers.add_parser('aaa') # adds subparser if aaa is argument after above optionalargument
    parser_aaa.add_argument("pos1", metavar='', help='pos1 help')
    parser_aaa.add_argument("--opt1-aaa", "-a", metavar='', help="opt1 help")
    parser_aaa.add_argument("--opt2-aaa", "-b", metavar='', help="opt2 help")
    parser_aaa.add_argument("--opt3-aaa", "-c", metavar='', help="opt3 help")

    parser_bbb = subparsers.add_parser('bbb')
    parser_bbb.add_argument("pos1", metavar='', help='pos1 help')
    parser_bbb.add_argument("--opt1-bbb", "-a", metavar='', help="opt1 help")
    parser_bbb.add_argument("--opt2-bbb", "-b", metavar='', help="opt2 help")
    parser_bbb.add_argument("--opt3-bbb", "-c", metavar='', help="opt3 help")
    parser_bbb.add_argument("--opt4-bbb", "-d", metavar='', help="opt3 help")

    group = parser.add_mutually_exclusive_group()
    group.add_argument('--verbose', '-v', action='store_true')
    group.add_argument('--quite', '-q', action='store_true')

    parser.add_argument("-x", "--xyz", type=str, default="", help="Help text regarding xyz")
    return parser

def main():
    """
    Main Function takes care of the invoking of the CLI parser. Etc
    """

    parser = get_parser()

    args = parser.parse_args()

    print(args)

    exit

if __name__ == '__main__':
    main()
