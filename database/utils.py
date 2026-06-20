from operator import eq, ne, lt, gt, le, ge
from typing import Literal, Union


class Conditions[T]:
    key: str
    value: T
    opr: Literal["==", "!=", ">", "<", "<="]
    
    OPERATORS = {
        "==": eq,
        "!=": ne,
        ">": gt,
        ">=": ge,
        "<": lt,
        "<=": le,
    }

    def __init__(self, key: str, value: T, opr: str):
        self.key = key
        self.value = value
        self.opr = opr

    
    def parse_condition(self, clss: type) -> str | None:
        column = getattr(clss, self.key, None)
        if column is None:
            raise Exception(f"field {self.key} does not exist in database")
        
        expected_type = column.type.python_type 
        if not isinstance(self.value, expected_type):
            raise Exception(f"{self.key} expects type {expected_type.__name__}")
        
        operation = self.OPERATORS.get(self.opr)
        if operation is None:
            raise Exception(f"invalid operation {self.opr}")
        
        return operation(column, self.value)
    
