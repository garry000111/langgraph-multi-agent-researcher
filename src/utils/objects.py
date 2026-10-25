from pydantic import BaseModel, Field
from typing import List



# creating our object analyst
class Analyst(BaseModel):
  affiliation: str = Field(description="Primary affiliation of the analyst")
  name: str = Field(description="Name of the analyst")
  role: str = Field(description="Role of the analyst in the context of the topic")
  description: str = Field(description="Descriptio of the analyst focus, concerns and motives")

  @property
  def persona(self) -> str:
    return f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affiliation}\nDescription: {self.description}"


class Perspective(BaseModel):
  analysts: List[Analyst] = Field(description="Comprehensive list of al the analysts with their role")

class SearchQuery(BaseModel):
  search_query: str = Field(description='Search query for the retriever')