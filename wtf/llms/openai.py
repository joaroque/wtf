import huepy as hue
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import OpenAI

from wtf.utils.models import ErrorMessage
from wtf.utils.prompt import BASE_PROMPT, EXPLAINER_PROMPT

MODEL_NAME = "gpt-3.5-turbo-instruct"


class OpenaiLLM:
    llm = OpenAI(model_name=MODEL_NAME, temperature=0.0)

    def __init__(
        self,
        prompt=EXPLAINER_PROMPT,
        output_model=ErrorMessage,
        language="en",
        response_format="json",
    ):
        self.language = language
        self.response_format = response_format
        self.base_prompt = BASE_PROMPT.format(language=language)
        self.parser = PydanticOutputParser(pydantic_object=output_model)
        self.prompt = PromptTemplate(
            template=prompt,
            input_variables=[
                "user_input",
                "language",
                "response_format",
                "base_prompt",
                "format_instructions",
            ],
        )

    def __call__(self, user_input):
        chain = self.prompt | self.llm | self.parser

        result = chain.invoke(
            {
                "user_input": user_input,
                "language": self.language,
                "response_format": self.response_format,
                "base_prompt": self.base_prompt,
                "format_instructions": self.parser.get_format_instructions(),
            }
        )

        return result

    @staticmethod
    def format_output(result):
        """
        Try to parse the output and return a formatted string.
        If parsing fails, return the raw output.

        ** IMPORTAN T: THIS IS A TEMPORARY IMPLEMENTATION **

        Todo:
            - add support for other output formats and languae
        """
        try:
            formatted_output = (
                f"{hue.que(hue.cyan('REASON:'))} {result.reason}\n"
                f"{hue.bad(hue.red('CAUSES:'))}\n"
                + "\n".join([f" - {cause}" for cause in result.causes])
                + "\n"
                f"{hue.good(hue.green('SOLUTION:'))} {result.solution}\n"
                f"{hue.info(hue.cyan('DOCUMENTATION:'))} {hue.under(result.documentation)}"
            )
            return formatted_output

        except Exception as e:
            # raise Exception(f"Failed to parse the output: {e}")
            print("Raw outuput: {}".format(result))
