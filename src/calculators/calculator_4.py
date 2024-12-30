from typing import Dict, List
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError
from src.errors.http_bad_request import HttpBadRequestError

class Calculator4:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)
        
        mean_value = self.__calculate_mean(input_data)
        
        formated_response = self.__format_response(mean_value)
        
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Malformed body: 'numbers' field is required.")
        
        if len(input_data) == 0:
            raise HttpBadRequestError("The list of numbers cannot be empty.")
        
        input_data = body["numbers"]
        return input_data
    
    def __calculate_mean(self, numbers: List[float]) -> float:
        mean_value = self.__driver_handler.mean(numbers)
        return mean_value
    
    def __format_response(self, mean_value: float) -> Dict:
        return {
            "data": {
                "calculator": 4,
                "value": mean_value,
                "success": True
            }
        }
