"""
Utility functions for the calculator application.
Module 8 Assignment — Ostad, AI/ML Engineering Bootcamp, Batch 6
Author: Farjana Ferdausi
"""

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b

# Module 8 Assignment completed — Ostad,Batch 6