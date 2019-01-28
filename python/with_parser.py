#!/usr/bin/env python

from __future__ import print_function

import argparse
import os
import sys

DESCRIPTION="""\
Short description regarding the program
"""

def get_parser():
    """
    Description regarding the function
    :returns: Parser
    :rtypepe: argparse.ArgumentParser
    """

    parser = argparse.ArgumentParser(description=DESCRIPTION, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("something", help="something regarding something")
    parser.add_argument("-x", "--xyz", type=str, default="", help="Help text regarding xyz")
    return parser

def main():
    """
    Main Function takes care of the invoking of the CLI parser. Etc
    """

    parser = get_parser()

    args = parser.parse_args()

    exit

if __name__ == '__main__':
    main()
