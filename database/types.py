from operator import eq, ne, lt, gt, le, ge
from typing import Literal, Union

OPERATORS = {
    "==": eq,
    "!=": ne,
    ">": gt,
    ">=": ge,
    "<": lt,
    "<=": le,
}

class Conditions[T]:
    key: str
    value: T
    opr: Literal["==", "!=", ">", "<", "<="]
    
    def __init__(self, key: str, value: T, opr: str):
        self.key = key
        self.value = value
        self.opr = opr
    
    def getOperation(self) -> Union[eq, ne, lt, gt, le, ge] | None:
        return OPERATORS.get(self.opr)
