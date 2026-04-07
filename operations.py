# -*- coding: utf-8 -*-
import numpy as np

def matrix_multiply(A: np.ndarray, B:np.ndarray):
    """
    Multiply two matrices A and B
    """
    return A @ B

def determinant(A: np.ndarray):
    """
    Compute the determinant of matrix A
    """
    return float (np.linalg.det(A))

def inverse(A: np.ndarray):
    """
    Compute the inverse of matrix A
    """
    return np.linalg.inv(A)