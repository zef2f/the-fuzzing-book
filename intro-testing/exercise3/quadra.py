import my_sqrt_fixed

def quadratic_solver(a, b, c):
    q = b * b - 4 * a * c
    if q <= 0:
        print('q <= 0')
        return

    if a == 0:
        print('a == 0')
        return
    solution_1 = (-b + my_sqrt_fixed.my_sqrt_fixed(q)) / (2 * a)
    solution_2 = (-b - my_sqrt_fixed.my_sqrt_fixed(q)) / (2 * a)
    return (solution_1, solution_2)


if __name__ == "__main__":
    print(quadratic_solver(0, 6, -9))
