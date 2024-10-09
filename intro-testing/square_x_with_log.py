def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        print("approx = ", approx)
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

print(my_sqrt(9))
