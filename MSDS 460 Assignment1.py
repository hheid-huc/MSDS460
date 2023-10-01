#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:30:45 2023

@author: johnmhanson
"""
from pulp import *
# declare variables
r = LpVariable("r", 0, None) # Breakfast Bars
m = LpVariable("m", 0, None) # Milk
t = LpVariable("t", 0, None) # Turkey
s = LpVariable("s", 0, None) # Pasta Sauce
p = LpVariable("p", 0, None) # Pasta

prob = LpProblem("problem", LpMinimize)

prob += 20*r + 120*m + 470*t + 490*s + 0*p <= 5000
prob += 210*r + 120*m + 60*t + 80*s + 200*p >= 2000
prob += 3*r + 8*m + 12*t + 2*s + 7*p >= 50
prob += 0*r + 2.1*m + 0*t +0*s + 0*p >= 20
prob += 26*r + 300*m + 0*t + 20*s + 0*p >= 1300
prob += 2.16*r + 0*m + .7*t + .5*s + .9*p >= 18
prob += 94*r + 350*m + 0*t + 440*s + 140*p >= 4700



#define the objective function
prob += 1.08*r + .42*m + 1.83*t + .66*s + .25*p

status = prob.solve()
print (LpStatus[status])

print(value(r), "Breakfast Bars Servings")
print(value(m), "Milk Servings")
print(value(t), "Turkey Lunch Meant Servings")
print(value(s), "Pasta Sauce Servings")
print(value(p), "Pasta Servings")

m_value = (value(r))
p_value = (value(p))

results = 1.08*m_value + .25*p_value
print(results, "Total Cost Dollars")
