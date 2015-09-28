# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0
at_count = 0
a = 0
c = 0
t = 0
g = 0

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1
        if bp == 'C':
            c = c + 1
        else:
            g = g + 1
    if bp == 'A' or bp == 'T':
        at_count = at_count + 1
        if bp == 'A':
            a = a + 1
        else:
            t = t + 1


# divide the gc_count by the total_count
gc_content = float(gc_count) / (a + t + g + c)
at_content = float(at_count) / (a + t + g + c)
classification = ""
if gc_content > 0.6:
    classification = "high GC content"
elif gc_content < 0.4:
    classification = "low GC content"
else:
    classification = "moderate GC content"

# Print the answer
# added float("{0:.12f}".format) to round to same places as expected.txt
print('GC-content:', float("{0:.12f}".format(gc_content)))
print('AT-content:', float("{0:.12f}".format(at_content)))
print('G count:', g)
print('C count:', c)
print('A count:', a)
print('T count:', t)
print('Sum count:', (a + t + g + c))
print('Total count:', total_count)
print('seq length:', len(seq))
print('AT/GC Ratio:', float("{0:.12f}".format(((a + t) / (g + c)))))
print('GC Classification:', classification)
