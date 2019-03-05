# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 16:44:43 2019

@author: admin
"""
import sys


def foo():
    friends = ["Tom", "Jerry"]
    for f in friends:
        print("Hello, %s" %f)
    return len(friends)
    
    
def tracefunk(frame, event, arg):
    func_name = frame.f_code.co_name
    var_name = frame.f_locals.keys
    if event == 'return':
        print("function:", func_name, "," "local_vars:", ",".join("{}".format(loc) for loc in var_name))
    return tracefunk

    
sys.settrace(tracefunk)
foo() 
    