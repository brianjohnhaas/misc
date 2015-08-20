#!/usr/bin/env python

import os, sys, re
from Bio import SeqIO
import subprocess

usage ="\n\n\tusage: " + sys.argv[0] + " file.fastq\n\n"

if len(sys.argv) < 2:
    print >> sys.stderr, usage
    sys.exit(1)

fastq_file = sys.argv[1]

fh = None

if re.search(".gz$", fastq_file):
    p = subprocess.Popen("gunzip -c " + fastq_file, shell=True, stdout=subprocess.PIPE)
    fh = p.stdout
else:
    fh = open(fastq_file)
    raise Exception("ERROR")

def main():

    
    fq_reader = SeqIO.parse(fh, 'fastq')

    for fq_record in fq_reader:
        print fq_record.id

        fq_record_text = fq_record.format("fastq")

    sys.exit(0)



main()
