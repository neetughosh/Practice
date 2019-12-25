# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 00:41:33 2019

@author: NGH5KOR
"""

#def repeatedString(s, n):
#    gen_str = s
#    while(len(gen_str)<= n):       
#        gen_str = gen_str + s 
#        print("first", gen_str)
#    req_str = gen_str[:10]
#    req_arr=[]
#    req_arr = req_str.split("a")
#    print("second", len(req_arr)-1)
##    for i in req_str:        
##        req_arr.append(i)
#    print("second", req_arr.count('a'))
##    return sockMerchant(req_arr) 

def repeatedString(s, n):
    a_cnt = s.count('a')
    num = n//len(s)
    mod = n%len(s)
    count = a_cnt*num + s[:mod].count('a')
    return count 