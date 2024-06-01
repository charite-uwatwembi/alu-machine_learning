#!/usr/bin/env python3
"""
This module provides a function to calculate the sum of squares of the first n natural numbers.
"""

def summation_i_squared(n):
    """
    Calculate the sum of squares of the first n natural numbers.
    
    Args:
        n (int): The stopping condition. Must be a positive integer.
    
    Returns:
        int: The sum of squares of the first n natural numbers.
        None: If n is not a valid number.
    """
    if not isinstance(n, int) or n < 1:
        return None
    return n * (n + 1) * (2 * n + 1) // 6
