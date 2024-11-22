import square_x

def my_sqrt_fixed(x):
    assert 0 <= x
    if x == 0:
        return 0
    return square_x.my_sqrt(x)
