import seasons
import pytest

def test_positive():
    #only valid for 2025-12-14#
    input="1999-01-01"
    data=seasons.date_data(input)
    assert(data.checkdate())==None
    assert(data.getdelta())=="Fourteen million, one hundred seventy-five thousand, three hundred sixty minutes"
    input="2001-01-01"
    data=seasons.date_data(input)
    assert(data.checkdate())==None
    assert(data.getdelta())=="Thirteen million, one hundred twenty-two thousand, seven hundred twenty minutes"

def  test_negative():
    with pytest.raises(ValueError):
        input="February 6th, 1998"
        data=seasons.date_data(input)
        data.checkdate()

