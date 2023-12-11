#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 12:04:43 2023

@author: saulcorona
"""

def find_savings_rate(annual_salary, semi_annual_raise, total_cost=1000000, months=36, epsilon=100):
    portion_down_payment = 0.25 * total_cost
    r = 0.04  # Tasa de retorno anual
    low = 0  # 0%
    high = 10000  # 100%
    portion_saved = (high + low) // 2
    steps = 0

    while low <= high:
        steps += 1
        current_savings = 0
        test_salary = annual_salary

        for month in range(1, months + 1):
            if month % 6 == 0:
                test_salary += test_salary * semi_annual_raise
            current_savings += (test_salary / 12) * (portion_saved / 10000) + (current_savings * r / 12)

        if abs(current_savings - portion_down_payment) <= epsilon:
            return portion_saved / 10000, steps
        elif current_savings < portion_down_payment:
            low = portion_saved + 1
        else:
            high = portion_saved - 1

        portion_saved = (high + low) // 2

    return None, steps

# Solicitar entrada del usuario
annual_salary = float(input("Enter your anual salary: "))
semi_annual_raise = float(input("Enter the percent of your semi­annual salary raise: "))

# Llamar a la función
result, steps = find_savings_rate(annual_salary, semi_annual_raise)

if result is not None:
    print(f"Your save is: {result:.4f} ({result * 100:.2f}%)")
    print(f"step number {steps}")
else:
    print("It's not posible save with your salary")
