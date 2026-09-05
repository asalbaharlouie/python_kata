def even_or_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

def test_even_or_odd_when_odd():
    assert even_or_odd(3) == "odd"

test_even_or_odd_when_odd()

def test_even_or_odd_when_even():
    assert even_or_odd(4) == "even"

test_even_or_odd_when_even()

def test_even_or_odd_negative_odd_number():
    assert even_or_odd(-3) == "odd"

test_even_or_odd_negative_odd_number()

def test_even_or_odd_negative_even_number():
     assert even_or_odd(-4) == "even"

test_even_or_odd_negative_even_number()

print(even_or_odd(8))
print(even_or_odd(7))