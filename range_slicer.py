#!/usr/bin/env python3
##########################################
#  2022/Dec/02 @citb0in bitcointalk.org  #
#                                        #
#   This project is licensed under the   #
#       terms of the GPLv3 license.      #
##########################################

import sys
import pprint
from argparse import ArgumentParser

parser = ArgumentParser(description='Slices a pre-defined range into n equal parts or in given chunk size', epilog='2022-12-02 v1.0 by citb0in')
requiredName = parser.add_argument_group('required named arguments')
requiredName.add_argument("-r", "--range", help = "lower and upper range limits, decimal or hex supported", required=True, type=int, nargs=2)
parser.add_argument("-c", "--chunkmode", help = "range generation based on 'chunksize' instead of 'parts'", action="store_true", dest="chunkmode")
parser.add_argument("-n", "--number", help = "create n slices (or n-sized chunks when in chunkmode), default : 2", type=int, default='2')
parser.add_argument("-nov", "--noverlap", help = "non-overlapping range edges", action="store_true")
parser.add_argument("-V", "--version", action="version", version="%(prog)s v1.0 by citb0in")

if len(sys.argv)==1: parser.print_help(), sys.exit(1)
args = parser.parse_args()
start, end, chunkmode, number, noverlap = args.range[0], args.range[1], args.chunkmode, args.number, args.noverlap

# input validation
assert 0 <= start, "range start cannot be a negative number"
assert start < end, "range start cannot be greater than or equal range end"
assert 0 < number <= (end-start)+1, "n cannot be greater than or equal range size, please reduce n"

def nslice(r, n):
    quotient, remainder = divmod(len(r), n)
    if noverlap:    
        print("Range",start,"-",end,"will be sliced into",number,"equal parts with non-overlapping range edges\n")
        return (r[i*quotient+min(i, remainder):(i+1)*quotient+min(i+1, remainder)] for i in range(n))
    else:
        print("Range",start,"-",end,"will be sliced into",number,"equal parts\n")
        return (r[i*quotient+min(i, remainder):(i+1)*quotient+min(i+1, remainder)] for i in range(n))

def cslice(r, n):
    quotient, remainder = divmod(len(r), n)
    if noverlap:
        print("Range",start,"-",end,"will be sliced into chunks with size",number,"and non-overlapping range edges\n")
        return (r[i:i + n-1] for i in range(0, len(r), n))
    else:
        print("Range",start,"-",end,"will be sliced into chunks with size",number,"\n")
        return (r[i:i + n] for i in range(0, len(r), n))

if not chunkmode:
    pprint.pprint(list(nslice(range(start, end), number)))
    
if chunkmode:
    pprint.pprint(list(cslice(range(start, end), number)))
