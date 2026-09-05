def bigger_num(a, b):
    if a > b:
        return a
    elif a < b:
        return b
    else:
        return "They are equal to each other."


def test_bigger_num():
    assert bigger_num(2, 8) == 8

test_bigger_num()

def test_bigger_num2():
    assert bigger_num(5, 5) == "They are equal to each other."

test_bigger_num2()

print(bigger_num(4, 40))