#!/usr/bin/env python3
def poly_derivative(poly):
    """
    Calculate the derivative of a polynomial.

    Args:
        poly (list): A list of coefficients representing a polynomial. The index
                     of the list represents the power of x that the coefficient belongs to.

    Returns:
        list: A new list of coefficients representing the derivative of the polynomial.
              If the derivative is 0, returns [0].
        None: If poly is not a valid list.
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
