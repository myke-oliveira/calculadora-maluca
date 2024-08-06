from typing import Dict, List
from pytest import raises
from src.calculators.calculator_4 import Calculator4
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.http_bad_request_error import HttpBadRequestError

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_badly_formatted_request():
    request = MockRequest({ "wrong_key": "wrong_value" })
    calculator4 = Calculator4()
    
    with raises(HttpUnprocessableEntityError) as excinfo:
        calculator4.calculate(request)
        
    assert str(excinfo.value) == "body mal formatado"

def test_empty_numbers_list():
    request = MockRequest({ "numbers": [] })
    calculator4 = Calculator4()
    
    with raises(HttpBadRequestError) as excinfo:
        calculator4.calculate(request)
        
    assert str(excinfo.value) == "division by zero"

def test_calculate():
    request = MockRequest({ "numbers": [0, 0, 10, 10] })
    calculator4 = Calculator4()
    
    response = calculator4.calculate(request)
        
    assert response == {
            "data": {
                "Calculator": 4,
                "value": 5.0
            }
        }