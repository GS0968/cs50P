import jar
import pytest

def test_init():
    with pytest.raises(ValueError):
        i=-15
        cookies=jar.Jar(i)

def test_deposit():
    cookies=jar.Jar(15)
    cookies.deposit(13)
    assert(cookies.size)==13
    with pytest.raises(ValueError):
        cookies.deposit(5)

def test_withdraw():
    cookies=jar.Jar(15)
    cookies.deposit(13)
    cookies.withdraw(10)
    assert(cookies.size)==3
    with pytest.raises(ValueError):
        cookies.withdraw(5)

def test_str():
    cookies=jar.Jar(15)
    assert(cookies.capacity)==15
    cookies.deposit(13)
    assert(cookies.size)==13
