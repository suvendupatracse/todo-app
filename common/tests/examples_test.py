import pytest
import responses
from common.util import my_div, get_crypto_values


@pytest.mark.positive_div
def test_add_1():
    result = my_div(6, 2)
    assert result == 3


@pytest.mark.positive_div
def test_add_2():
    result = my_div(100, 20)
    assert result == 5


@pytest.mark.negetive
def test_add_3():
    result = my_div(-100, -20)
    assert result == 5


@pytest.mark.xfail()
def test_add_4():
    result = my_div(0, 0)
    assert result == 6


@pytest.fixture(scope="class")
def get_numbers():
    return 10, 2


@pytest.mark.usefixtures("get_numbers")
class TestsMyDiv:
    def test_div_with_fixture(self, get_numbers):
        num1, num2 = get_numbers
        result = my_div(num1, num2)
        assert result == 5


@pytest.mark.parametrize("num1, num2, expected", [(10, 2, 5), (12, 2, 6), (0, 10, 0)])
def test_div_with_parameters(num1, num2, expected):
    result = my_div(num1, num2)
    assert result == expected


# handling exceptions
def test_handling_exceptions():
    with pytest.raises(ZeroDivisionError) as e:
        my_div(0, 0)
    assert str(e.value) == "division by zero"


@pytest.mark.slow
def test_third_party():
    result = get_crypto_values()
    assert result["ticker"]["base"] == "BTC"

@responses.activate
def test_third_party_with_mock():
    response_data = {
        "ticker": {
            "base": "BTC-Mock",
            "target": "USD",
            "price": "32283.49418563",
            "volume": "54131.43771505",
            "change": "351.22759252",
        },
        "timestamp": 1626885604,
        "success": True,
        "error": "",
    }
    responses.add(
        "GET",
        "https://api.cryptonator.com/api/ticker/btc-usd",
        json=response_data,
        status=200,
    )
    result = get_crypto_values()
    assert result["ticker"]["base"] == "BTC-Mock"