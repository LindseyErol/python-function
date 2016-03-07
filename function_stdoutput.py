#!/usr/bin/env python
#Author: Lindsey Erol C. Cadang
#Date: March 7, 2016
#Purpose: Python Script for displaying ouput in three ways

def FuncOut(name, age):
          print "Hi! My name is ", name + "and my age is", age
          print "Hi! My name is %s and my age is %d" %(name, age)
          print "Hi! My name is {} and my age is {}".format(name,age)

print FuncOut("Mary", 19)
