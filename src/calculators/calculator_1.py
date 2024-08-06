from typing import Dict
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity_error import HttpUnprocessableEntityError

class Calculator1:

    def calculate(self, request: FlaskRequest) -> Dict: # type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        splitted_number = input_data / 3
        
        first_process_result = self.__first_process(splitted_number)
        second_process_result = self.__second_process(splitted_number)
        calc_result = first_process_result + second_process_result + splitted_number
        
        return self.__format_response(calc_result)

    def __validate_body(self, body: Dict) -> float:
        if "number" not in body:
            raise HttpUnprocessableEntityError("Body mal formatado.")
        
        return body.get("number")
    
    def __first_process(self, first_number: float) -> float:
        first_part = first_number / 4 + 7
        second_part = first_part ** 2 * 0.257
        return second_part
    
    def __second_process(self, second_number: float) -> float:
        first_part = second_number ** 2.121
        second_part = first_part / 5 + 1
        return second_part
    
    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 1,
                "result": round(calc_result, 2)
            }
        }