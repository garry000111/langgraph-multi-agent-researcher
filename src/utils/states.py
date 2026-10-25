from typing_extensions import NotRequired, TypedDict, Annotated
from typing import List, Optional, List
from utils.objects import Analyst
from langgraph.graph import MessagesState
import operator



# state
class GenerateAnalystsState(TypedDict):
  topic: str #Research topic
  max_analysts: int #Number of analysts
  human_analyst_feedback: NotRequired[Optional[str]] #Human feedback
  analysts: NotRequired[List[Analyst]] #List of all the analysts

class InterviewState(MessagesState):
  max_num_turns: int # Number turns of conversation
  context: Annotated[list, operator.add] # source of docs
  analyst: Analyst # my analyst from list of our analysts
  interview: str #interview transcript
  sections: list

class ResearchGraphState(TypedDict):
    topic: str # Research topic
    max_analysts: int # Number of analysts
    human_analyst_feedback: NotRequired[Optional[str]] # Human feedback
    analysts: List[Analyst] # Analyst asking questions
    sections: Annotated[list, operator.add] # Send() API key
    introduction: str # Introduction for the final report
    content: str # Content for the final report
    conclusion: str # Conclusion for the final report
    final_report: str # Final report