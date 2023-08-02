# . For any number n, write a program to list all the solutions of the equation x1 + x2 + x3 +
# ...+ xn = C, where C is a constant (C<=10) and x1, x2,x3,...,xn are nonnegative integers,
# using brute force strategy.

def solve_equation(n, C):
    solutions = []

    def generate_combinations(current_sum, current_combination):
        if current_sum == C and len(current_combination) == n:
            solutions.append(current_combination)
            return
        elif current_sum > C or len(current_combination) > n:
            return

        for i in range(C + 1):
            generate_combinations(current_sum + i, current_combination + [i])

    generate_combinations(0, [])

    return solutions

# Example usage
n = 3
C = 4

solutions = solve_equation(n, C)
print(f"Solutions for n={n}, C={C}: {solutions}")