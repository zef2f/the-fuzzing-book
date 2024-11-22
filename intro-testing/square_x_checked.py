import square_x

def my_sqrt_checked(x):
    root = square_x.my_sqrt(x)
    square_x.assertEquals(root * root, x)
    return root

