#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 05:45:04 2016

@author: duane
"""

import pandas
import numpy

#read data into the program
#lesson 2 (4:50)
data = pandas.read_csv('nesarc_pds.csv',  low_memory=False)

#print out 
print(len(data))
print(len(data.columns))

print(len(data.index))

data['S1Q6A']=data['S1Q6A'].convert_objects(convert_numeric=True)
data['S1Q234']=data['S1Q234'].convert_objects(convert_numeric=True)
data['S2AQ6A']=data['S2AQ6A'].convert_objects(convert_numeric=True)

#the output that displays three of your variables as frequency tables

print("Variable 1 - frequency distribution - whole numbers")
c1 = data["S1Q6A"].value_counts(sort=False, dropna=False)
print (c1)

print("Variable 1 - frequency distribution - percents")
p1 = data["S1Q6A"].value_counts(sort=False, normalize=True)
print (p1)

print("Variable 2 - frequency distribution - whole numbers")
c2 = data["S1Q234"].value_counts(sort=False, dropna=False)
print (c2)

print("Variable 2 - frequency distribution - percents")
p2 = data["S1Q234"].value_counts(sort=False, normalize=True)
print (p2)


print("Variable 3 - frequency distribution - whole numbers")
c3 = data["S2AQ6A"].value_counts(sort=False, dropna=False)
print (c3)

print("Variable 3 - frequency distribution - percents")
p3 = data["S2AQ6A"].value_counts(sort=False, normalize=True)
print (p3)

#drink wine in the last 12 months and were laid off or fired in the last 12 months
sub1=data[(data['S2AQ6A']==1) & (data['S1Q234']==1)]
print(sub1)

#drink wine in the last 12 months and were not laid off or fired in the last 12 months
#sub2=data[(data['S2AQ6A']==1) & (data['S1Q234']==2)]
#print(sub2)