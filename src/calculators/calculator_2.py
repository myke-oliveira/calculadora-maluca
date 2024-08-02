from typing import Dict, List
from flask import request as FlaskRequest
from src.drivers.numpy_handler import NumpyHandler

class Calculator2:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_numbers = self.__validate_body(body)
        result = self.__process_data(input_numbers)
        return self.__format_response(result)
        
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Body mal formatado!")
        
        return body["numbers"]
    
    def __process_data(self, input_data: List[float]) -> float:
        numpy_handler = NumpyHandler()
        first_process_result = [(num * 11) ** 0.95 for num in input_data]
        result = numpy_handler.standard_derivation(first_process_result)
        return 1/result
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }