import re

def parse_equation(equation):
    matches = re.findall(r'([+-]?\d*)x([+-]?\d*)y=([+-]?\d+)', equation.replace(' ', ''))
    if matches:
        x_coeff = int(matches[0][0] or '1') if matches[0][0] != '-' else -1
        y_coeff = int(matches[0][1] or '1') if matches[0][1] != '-' else -1
        constant = int(matches[0][2])
        return [x_coeff, y_coeff, constant]
    else:
        raise ValueError("Equation format is incorrect")

# Using Euclid's algorithm 
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def simplify_fraction(numerator, denominator):
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    common = gcd(numerator, denominator)
    return numerator // common, denominator // common

def solve_equations(equation1, equation2):
    a1, b1, c1 = equation1
    a2, b2, c2 = equation2

    # Solve using Cramer's rule
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        raise ValueError("No unique solution exists")

    x_numerator = c1 * b2 - c2 * b1
    y_numerator = a1 * c2 - a2 * c1

    x = simplify_fraction(x_numerator, determinant)
    y = simplify_fraction(y_numerator, determinant)

    return x, y

equation1 = input("Enter an equation Ex:(2x-4y=3)\n")
equation2 = input("Enter an equation Ex:(2x-4y=3)\n")

equation1_sol = parse_equation(equation1)
equation2_sol = parse_equation(equation2)

x, y = solve_equations(equation1_sol, equation2_sol)

print(f"The solution is x = {x[0]}/{x[1]} and y = {y[0]}/{y[1]}")