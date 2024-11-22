import square_x

def assertEquals(x, y, epsilon=1e-10):
    assert abs(x - y) < epsilon

if __name__ == "__main__":
    assert abs(square_x.my_sqrt(16) - 4) < 1e-10
