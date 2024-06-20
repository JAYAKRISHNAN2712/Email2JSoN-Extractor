from langchain.tools import StructuredTool
from pydantic import BaseModel, Field
import json

# langChain Tool for converting LLM output to JSoN format
class Tool:
    class JSoN_Extractor(BaseModel):
        str_output: str = Field(description="The string to be converted to JSON")

    def __init__(self, str_output: str):
        self.str_output = str_output

    @staticmethod
    def convert_string_to_json(str_output: str):
        # Find the position of the first '{' to locate the start of the JSON
        start = str_output.find('{')
        # Find the position of the last '}' to locate the end of the JSON
        end = str_output.find('}') + 1

        # Extract the JSON part of the string
        json_string = str_output[start:end]
        print(json_string)
        # Convert the JSON string to a Python dictionary
        json_data = json.loads(json_string)

        return json_data

    def json_converter(self):
        json_extractor = StructuredTool.from_function(
            func=self.convert_string_to_json,
            name='JSoN Extractor',
            description='Extracts JSON data from a string',
            return_direct=True
        )

        return json_extractor.invoke({'str_output': self.str_output})