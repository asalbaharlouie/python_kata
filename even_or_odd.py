def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def test_even_or_odd_even_number():
    assert even_or_odd(6) == "even"

test_even_or_odd_even_number()

def test_even_or_odd_odd_number():
    assert even_or_odd(3) == "odd"

test_even_or_odd_odd_number()

def test_even_or_odd_negative_even_number():
    assert even_or_odd(-4) == "even"

test_even_or_odd_negative_even_number()

def test_even_or_odd_negative_odd_number():
    assert even_or_odd(-7) == "odd"

test_even_or_odd_negative_odd_number()

print(even_or_odd(0))