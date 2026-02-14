import pytest
from twttr import shorten

def test_lowercase():
    assert shorten("twitter")== "twttr"
    assert shorten("bentaiko")== "bntk"

def test_uppercase():
    assert shorten("TWITTER")== "TWTTR"
    assert shorten("BENTAIKO")== "BNTK"

def test_mixedcase():
    assert shorten("TwiTter")== "TwTtr"
    assert shorten("BenTaiko")== "BnTk"
def test_num():
    assert shorten("1234")== "1234"
    assert shorten("56789")== "56789"
def test_punc():
    assert shorten("<.!-_")== "<.!-_"
    assert shorten("()@#$%^&*=+")== "()@#$%^&*=+"
