#!/usr/bin/env python

import os

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
        if (value.find('.') > -1):
           corrected_line.append(float(value))
        else:
           corrected_line.append(int(value))
    corrected_list.append(corrected_line)
print(corrected_list)
file.close()
