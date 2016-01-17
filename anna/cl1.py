#!/usr/bin/env python
#
# Anna Lee
# 9/5/15
#

def name(fn,ln):
    a = fn + ' ' + ln
    return a

fn = raw_input('What is your first name?')
ln = raw_input('What is your last name?')

b = name(fn, ln)
print b

