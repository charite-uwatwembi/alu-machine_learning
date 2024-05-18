import numpy as np

def np_slice(matrix, axes={}):
    """
    Slices a matrix along specific axes.

    Args:
    - matrix (numpy.ndarray): The input matrix.
    - axes (dict): A dictionary where the key is an axis to slice along
                   and the value is a tuple representing the slice to make along that axis.

    Returns:
    - numpy.ndarray: The sliced matrix.
    """
    # Create a deep copy of the input matrix to avoid modifying the original matrix
    sliced_matrix = np.copy(matrix)

    # Iterate over the axes dictionary and apply slicing along each axis
    for axis, slice_tuple in axes.items():
        # Convert slice tuple to slice object
        axis_slice = slice(*slice_tuple)
        # Apply slicing along the specified axis
        sliced_matrix = np.take(sliced_matrix, axis_slice, axis=axis)

    return sliced_matrix
