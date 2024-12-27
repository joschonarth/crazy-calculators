from typing import Dict, List
from flask import Request

class Calculator2:
    def calculate(self, request: Request) -> Dict:
        body = request.json
        print(body)
        input_data = self.__validate_body(body)
        print(input_data)

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise Exception("Malformed body: 'numbers' field is required.")
        
        input_data = body["numbers"]
        return input_data