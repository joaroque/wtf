from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field


class ErrorMessage(BaseModel):
    reason: str = Field(description="The reason for the error")
    causes: list[str] = Field(description="Possible causes of the error")
    solution: str = Field(description="Suggested solution to fix the error")
    documentation: str = Field(
        description="Link to relevant documentation for the error"
    )


class ConsoleCommand(BaseModel):
    command: str = Field(
        description="The correct command to be executed in the terminal"
    )
