#Q5
def evaluate_polynomial(coefficients, x):
    result = 0
    power = len(coefficients) - 1
    for coefficient in coefficients:
        result += coefficient * (x ** power)
        power -= 1
    return result

# Example usage
polynomial = [4, 2, 9]  
x = int(input("Enter value of n : "))  # value of x
result = evaluate_polynomial(polynomial, x)
print(f"The result of evaluating the polynomial at x = {x} is: {result}")
























# n = int(input("Enter value of n : "))
# def calculatePoly(n):
#     poly_fun = 4*n*n + 2*n +9
#     return poly_fun

# print(calculatePoly(n))

# arr = [4*n*n, 2*n, 9]
# print(sum(arr))

# arr [ 1,3,4,5,6]
