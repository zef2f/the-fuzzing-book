import square_x
import my_sqrt_fixed
import sys

def sqrt_program(arg: str) -> None:
    try:
        x = float(arg)
    except ValueError:
        print('int pls')
    else:
        x = int(arg)
        if x < 0:
            print('illegel input')
        else:
            print('the root of', x, 'is', my_sqrt_fixed.my_sqrt_fixed(x))

def main():
    if len(sys.argv) > 1:
        name = sys.argv[1]
        sqrt_program(name)
    else:
        print('unlucky')

if __name__ == "__main__":
    main()
