import pytest
from um import count

def test_all():
    assert count("um")==1
    assert count("Hello, um, world")==1
    assert count("This is, um... CS50")==1
    assert count("Um... what are regular expressions?")==1
    assert count("Um, thanks um, regular expressions makes sense now")==2
    assert count("UM? Mum? Is that the album where, um, umm, the clumsy alums plays drums?")==2
