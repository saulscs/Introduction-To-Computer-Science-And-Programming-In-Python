#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 10:15:57 2023

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
semi_annual_raise = float(input("Enter the percent of your semi­annual salary raise: "))
print("The portion to increase", semi_annual_raise)

portion_down_payment = total_cost * 0.25

while current_savings < portion_down_payment:
    current_savings += current_savings * r / 12
    current_savings += annual_salary / 12 * portion_saved
    months += 1
    
    # Aumento de salario cada 6 meses
    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise

print("Nunber of months", months)