from typing import Dict
from flask import Request
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class Calculator3:
    def __init__(self, driver_handler: DriverHandlerInterface) -> None:
        self.__driver_handler = driver_handler

    def calculate(self, request: Request) -> Dict:
        pass