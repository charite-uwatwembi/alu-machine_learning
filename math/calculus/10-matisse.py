#!/usr/bin/env python3
def poly_derivative(poly):


    """
    Calculate the derivative of a polynomial.
    """
    if not isinstance(poly, list) or not all(isinstance(x, (int, float)) for x in poly):
        return None
    if len(poly) == 1:
        return [0]
    
    derivative = [i * poly[i] for i in range(1, len(poly))]
    return derivative

# Example usage
if __name__ == "__main__":
    poly = [5, 3, 0, 1]
    print(poly_derivative(poly))  # Output: [3, 0, 3]
