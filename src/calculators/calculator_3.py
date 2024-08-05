from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3():
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler
        
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        variance = self.__calculate_variance(input_data)
        multiplication = self.__calculate_multiplication(input_data)
        self.__veryfy_result(variance, multiplication)
        formatted_response = self.__format_response(variance)
        return formatted_response
    
    def __validate_body(self, body):
        if not "numbers" in body:
            raise Exception("body mal formatado")
        
        return body.get("numbers")
    
    def __calculate_variance(self, numbers: List[float]) -> float:
        return self.__driver_handler.variance(numbers)
    
    def __calculate_multiplication(self, numbers: List[float]) -> float:
        multiplication = 1
        for number in numbers:
            multiplication *= number
        
        return multiplication
    
    def __veryfy_result(self, variance: float, multiplication: float) -> None:
        if variance < multiplication:
            raise Exception("Falha no processo: Variância menor que multiplicação")
        
    def __format_response(self, variance: float) -> Dict:
        return {
            "data": {
                "Calculator": 3,
                "value": variance,
                "sucess": True
            }
        }