from typing import Dict
from .calculator_2 import Calculator2

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [2.12, 3.21, 4.32]})
    calculator_2 = Calculator2()
    response = calculator_2.calculate(mock_request)
    print(f"{response=}")
    
    assert isinstance(response, dict)
    assert response == {'data': {'Calculator': 2, 'result': 0.13}}