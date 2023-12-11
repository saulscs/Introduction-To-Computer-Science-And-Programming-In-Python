#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 14:50:31 2023

@author: saulcorona
"""

r = 0.04
current_savings = 0.0
months = 0

annual_salary = int(input("Enter your anual salary: "))
print("The starting annual salary ", annual_salary)
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
print("The portion of salary to be saved", portion_saved)
total_cost = int(input("Enter the cost of your dream home: "))
print("The cost of your dream home ", total_cost)

portion_down_payment = total_cost * 0.25

while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12 * portion_saved
    months += 1

print("Nunber of months", months)
