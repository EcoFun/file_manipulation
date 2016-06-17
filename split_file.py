#!/bin/env python2

__author__ = "Ludovic Duvaux"
__maintainer__ = "Ludovic Duvaux"
__license__ = "GPL_v3"

from sys import argv, exit
from os.path import basename

usage="""
SYNOPSIS:
{0} entry_file n prefix

DESCRIPTION:
Takes a file containing a serie of entries and split it in several files
of 'n' entries.

ARGUMENTS:
    entry_file      file to be split
    n               number of entries per output file
    prefix          prefix of the output files

""".format(basename(argv[0]))

if len(argv) != 4:
    print "ERROR: wrong number of arguments (there should be 3)"
    exit(usage)

inp = argv[1]   # file of entries
sec = int(argv[2])   # number of files per new file
pout = argv[3]  # prefix of output

i = 1
j = 1
with open(inp) as f:
    for l in f:
        # open output file
        if sec == 1:
            fout = "%s_%s_%s.txt" % (pout, j, i)
            out = open(fout, "w")
        elif i % sec == 1:
            fout = "%s_%s_%s-%s.txt" % (pout, j, i, (i + sec -1))
            out = open(fout, "w")
        
        out.write(l)
        
        # close output file
        if i % sec == 0:
            out.close()
            j += 1
        
        i += 1

f.close()
