import shellsort
import random
import tests

num_tests = 1000

for test in range(num_tests):

    arr_len = random.randint(0,100)
    array = []

    for i in range(arr_len):
        array.append(random.randint(-1000000, 1000000))

    sort_array = shellsort.shellsort(array)
    #print(array)
    # print(sort_array)
    assert tests.is_sorted(sort_array) == True
    assert tests.is_permutation(array, sort_array) == True

