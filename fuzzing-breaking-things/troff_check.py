import string

def no_backslash_d(inp):
    pattern = "\\D"
    index = inp.find(pattern)

    if index < 0 or index + len(pattern) >= len(inp):
        return True
    c = inp[index + len(pattern)]
    assert c in string.printable

def no_8bit(inp):
    for i in range(len(inp) - 1):
        assert ord(inp[i]) <= 127 or inp[i + 1] != '\n'
    return True

def no_dot(inp):
    assert inp != ".\n"
    return True


if __name__ == "__main__":
    test_str = "asdfakdf324234"
    test_str_backslash_d = "abc\\D"
    test_str_backslash_d += '\0'
    test_str_8bit = "abcé\n"
    test_str_dot = ".\n"
    no_backslash_d(test_str)
    no_8bit(test_str)
    no_dot(test_str)
