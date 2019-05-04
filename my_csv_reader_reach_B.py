#!/usr/bin/env python

import os
import numpy

file_path = 'housing.data'

if os.path.isfile(file_path):
    print('I have a valid file!!!')
else:
    print('Invalid file, I\'ll crash')

file = open('housing.data')

corrected_list = []
for line in file.readlines():
    clean_line = line.replace('  ', ' ').replace('  ', ' ').strip()
    line_values = clean_line.split(' ')
    corrected_line = []
    for value in line_values:
        corrected_line.append(value)
    corrected_list.append(corrected_line)

A = numpy.array(corrected_list)
for value in A.transpose():
   s = str(value).replace("'","")
   print(s)


file.close()
