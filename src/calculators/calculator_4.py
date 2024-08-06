from typing import List, Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError
from src.errors.http_bad_request_error import HttpBadRequestError

class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        numbers = self.__validate_body(body)
        mean = self.__calculate_mean(numbers)
        formatted_response = self.__format_response(mean)
        return formatted_response
    
    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("body mal formatado")
        
        return body.get("numbers")
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        try:
            return sum(numbers) / len(numbers)
        except ZeroDivisionError:
            raise HttpBadRequestError("division by zero")
    
    def __format_response(self, mean: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "value": round(mean, 2)
            }
        }