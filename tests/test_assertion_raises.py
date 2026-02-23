import pytest
from assertpy import assert_that

def test_assertion_raises():
    with pytest.raises(ZeroDivisionError) as err:
        5 / 0
    # assert "divisionnnnnnnnn by zero" in str(err.value)
    assert_that(f"{err.value}").is_equal_to('division by zero')
    # היה צריך להמיר את err.value לסטרינג ולכן זה עבד