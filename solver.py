# -*- coding: utf-8 -*-
import numpy as np

def solve_system(A: np.ndarray, b:np.ndarray):
    """
    Solve the linear system Ax = b
    """
    return np.linalg.solve(A, b)
