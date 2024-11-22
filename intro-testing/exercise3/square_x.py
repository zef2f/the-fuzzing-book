def assertEquals(x, y, epsilon=1e-10):
    assert abs(x - y) < epsilon

def my_sqrt(x):
    """Computes the square root of x, using the Newton-Raphson method"""
    approx = None
    guess = x / 2
    while approx != guess:
        approx = guess
        guess = (approx + x / approx) / 2
    return approx

if __name__ == "__main__":
    print(my_sqrt(4))
    print(my_sqrt(2))
    print(my_sqrt(16))
