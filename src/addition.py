# testing the addtion function

def add(num1 , num2):
    return num1+num2

def test_add():
    assert add(2,3) == 5
    assert add(2,9) == 11
    assert add(1,5) == 6 
    assert add(5,5) == 10 
    assert add(0,0) == 0