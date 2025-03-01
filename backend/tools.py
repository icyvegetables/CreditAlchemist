from langchain.tools import BaseTool, StructuredTool, tool
from pydantic import BaseModel, Field
import ast

# class CalculatorInput(BaseModel):
#     a: int = Field(description="first number")
#     b: int = Field(description="second number")


def multiply(number: str) -> int:
    """Multiply two numbers."""
    number = ast.literal_eval(number.strip())
    return number['a'] * number['b']


calculator = StructuredTool.from_function(
    func=multiply,
    name="Calculator",
    description="multiply numbers. Sample input: {'a': 2, 'b': 3}",
    return_direct=True,
    # coroutine= ... <- you can specify an async method if desired as well
)