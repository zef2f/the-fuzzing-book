import square_x
import square_x_test_assert
import time

start_time = time.time()

square_x_test_assert.assertEquals(5.0, square_x.my_sqrt(25.0))
square_x_test_assert.assertEquals(4.0, square_x.my_sqrt(16.0))
square_x_test_assert.assertEquals(25.0,square_x.my_sqrt(25.0) * square_x.my_sqrt(25.0))

n_loop = 10000

for i in range(1, n_loop):
    square_x_test_assert.assertEquals(i, square_x.my_sqrt(i) * \
            square_x.my_sqrt(i), epsilon=1e-5)

end_time = time.time()

print("program work time = ", end_time - start_time)
