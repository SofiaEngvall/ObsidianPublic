#----------------------------------------------
print('\nlist all keywords and soft keywords')
import keyword
print(keyword.kwlist)
print(keyword.softkwlist)

#----------------------------------------------
print('\nrandom numbers')
import random
#random.seed(345) #by default the system time is used
for i in range(5):
    number = random.randint(1,5)
    print(number)

#----------------------------------------------
print('\nmath')
import math
radians = math.pi /2
print(radians)

#----------------------------------------------
#datetime
#numpy         calculations
#scipy         tools for numpy
#scikit-learn  artificiell intelligens (AI)
#pandas        data analysis
#csv           handling files
#matplotlib    plottning
#Tkinter       graphics

import datetime
print(dir(datetime.datetime))

#----------------------------------------------
from math import acos
print(acos(0.4))

from random import *
print(randint(0,9))

import math as m
print(m.tan(5.5))

#convertions
import numpy as np
import pandas as pd
import mathplotlib.pyplot as plt

#----------------------------------------------
import datetime as dt
datum = dt.datetime(year=2020, mon)
