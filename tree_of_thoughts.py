from custom_llm import CustomLLMModel
import json
from pydantic import BaseModel
from typing import List

# define the structure for parsing the llm output
class Idea(BaseModel):
    name: str
    description:str

class IdeasList(BaseModel):
    solutions: List[Idea]

class TreeOfThoughts:
# instantiate the local llm
    def __init__(self):
        self.llm = CustomLLMModel()

    def getidea(self, thought:str):
    # prompt the user for their idea to brainstorm
        client = self.llm.getclientinterface()
        ideas = client.generate(
                    model = "mistral:latest",
                    prompt = (
                        f"Brainstorm a solution path for : {thought}"
                        f"Respond in the following JSON format"
                        """
                        {
                            "solutions" :[
                                {"name":"", "description":""},
                                {"name":"", "description":""},
                                {"name":"", "description":""},
                            ]
                        }
                        """

                    ),
                    format=IdeasList.model_json_schema()
                )
    #parse the llm output into a structured list using pydantic classes
        return IdeasList.model_validate_json(ideas.response)



