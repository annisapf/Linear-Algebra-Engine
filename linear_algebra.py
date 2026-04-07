# -*- coding: utf-8 -*-
import numpy as np

from linear_algebra_engine.operations import matrix_multiply, determinant, inverse
from linear_algebra_engine.solver import solve_system

def run_linear_algebra():
    A = np.array([2.0, 1.0],
                 [1.0, 3.0])
    
    b = np.array([5.0, 6.0])
    
    print("Matrix A:", A)
    
    print("\nVector b:", b)
    
    x = solve_system(A, b)
    print("\nSolution x to Ax = b: ", x)
    
    print("\nCheck Ax: ", A @ x)
    
    print("\nA multiplied by A: ", matrix_multiply(A, A))
    
    print("\nDeterminant of A: ", determinant(A))
    
    print("\nInverse of A: ", inverse(A)) 
    
if __name__=="__main__":
    run_linear_algebra()
    