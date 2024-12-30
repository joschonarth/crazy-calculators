from typing import Dict, List
from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.errors.http_bad_request import HttpBadRequestError

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandler:
    def mean(self, numbers: List[float]) -> float:
        return sum(numbers) / len(numbers)

class MockDriverHandlerError:
    def mean(self, numbers: List[float]) -> float:
        raise Exception("Some error in the driver")

def test_calculate_with_empty_list():
    mock_request = MockRequest({ "numbers": [] })
    calculator_4 = Calculator4(MockDriverHandler())
    
    with raises(HttpBadRequestError) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "The list of numbers cannot be empty."

def test_calculate_with_driver_error():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Some error in the driver"

def test_calculate_mean():
    mock_request = MockRequest({ "numbers": [1, 2, 3, 4, 5] })
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    
    assert response == {'data': {'calculator': 4, 'value': 3.0, 'success': True}}
