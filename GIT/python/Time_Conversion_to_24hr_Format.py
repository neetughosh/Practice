# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 22:50:12 2019

@author: NGH5KOR
"""

#!/bin/python3

import os
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    time_arr = s.split(":")

    if(re.match(r".*PM$",s)):
        if(time_arr[0] != "12"):
            time_arr[0] = str(int(time_arr[0]) + 12)
            s = ":".join(time_arr)
    else:
        if(time_arr[0] == "12"):
            time_arr[0] = "00"
            s = ":".join(time_arr)
    s = re.sub("[PM|AM]","",s)    

    return s

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
