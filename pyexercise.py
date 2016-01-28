import sympy as sy
import numpy as np

def fun_1( your_id ):
    ans = hex(your_id)
    return ans

def my_integral():
    x = sy.Symbol('x')
    ans = sy.integrate( sy.exp(-x**3), (x,0, sy.oo))
    return ans

def my_solution():
    A = np.array( [[18,6,37,37,32,30,16,6,14,20], [4,11,1,22,0,17,21,3,22,37], [4,23,26,0,15,2,3,4,11,30], [5,16,29,21,34,18,8,19,34,1], [19,24,0,26,7,3,29,9,14,11], [23,22,23,21,30,38,13,9,2,4], [17,0,7,3,3,18,19,15,38,39], [25,8,31,20,27,28,23,40,7,28], [2,30,23,16,32,38,9,5,35,35], [18,15,39,11,19,37,2,38,14,37]] )
    b = np.array([23,34,2,21,16,2,9,40,5,8])
    x = np.linalg.solve(A,b) # Solve Ax = b
    return x


if __name__ == '__main__':
    your_id = 1400623
    print('Hexadecimal representation of %d is %s'%( your_id, fun_1( your_id) ))
    print('Integral = ', my_integral())
    print('Solution = ', my_solution())
