from typing import Dict, List
from pytest import raises
from src.calculators.calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body
        
class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 3.

class MockDriverHandlerSuccess:
    def variance(self, numbers: List[float]) -> float:
        return 101.

def test_calculate_with_variance_error():
    calculator3 = Calculator3(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator3.calculate(MockRequest({ "numbers": [1, 2, 3, 4, 5] }))
    
    assert str(excinfo.value) == "Falha no processo: Variância menor que multiplicação"
    
def test_calculate():
    calculator3 = Calculator3(MockDriverHandlerSuccess())
    
    response = calculator3.calculate(MockRequest({ "numbers": [1, 1, 1, 1, 100] }))
    
    assert response == {'data': {'Calculator': 3, 'value': 101.0, 'sucess': True}}