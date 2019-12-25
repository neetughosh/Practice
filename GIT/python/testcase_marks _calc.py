# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 22:47:52 2019

@author: NGH5KOR
"""
import re

def testcase_marks_calc(testcase, result):
    """
    This function calculates the score of the passed testcases
    """
    
    
    #Initialise the testcase_passed, marks, groups with zero
    (testcase_passed, marks, nbr_groups) = (0, 0, 0)
    
    # Run a loop for the testcases given and calculate the passed testcases and calculate the group testcases
    for tc in range(len(testcase)):
        
        # calculate the nbr of passed testcases
        regex = re.compile("^ok$", re.I)
        if regex.match(result[tc]):
            testcase_passed += 1
        
        # calculate the nbr of group testcases like test3a, test3b, test3c
        regex = re.compile("^\w+\d[a-z]$", re.I)
        if(regex.search(testcase[tc].strip())): 
            nbr_groups +=1    
            
        # calculate the marks obtained ie (100*testcases passed)/groups
        marks = (100*testcase_passed)
        
        if nbr_groups > 0:
            marks = (100*testcase_passed)/nbr_groups
        
    # Return the marks
    return marks 
    

print(testcase_marks_calc(["test1", "test2","test3a", "test3b", "test3c"], ["ok", "fail","OK", "fail", "fail"])  )
print(testcase_marks_calc(["test1", "test2","test3", "test4", "test5"], ["ok", "fail","OK", "fail", "fail"])  )
    