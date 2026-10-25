from utils.states import GenerateAnalystsState, InterviewState, ResearchGraphState
from langgraph.graph import END
from dotenv import load_dotenv
from utils.nodes import create_analysts
from typing import Literal
from langchain.messages import AIMessage, HumanMessage
from langgraph.types import Send

load_dotenv()

#edges
def should_continue_or_createanalysts_again(state: GenerateAnalystsState) -> Literal["create_analysts", END]:
  """Return the next node to execute"""

  #Check if human feedback
  human_analyst_feedback = state.get('human_analyst_feedback', None)

  if human_analyst_feedback:
    return "create_analysts"

  return END


def routes_messages(state: InterviewState, name: str = "expert"):
  """Route between question and answer"""

  # Get Messages
  messages = state["messages"]
  max_num_turns = state.get("max_num_turns", 2)

  #check number of expert answer
  num_responses = len([m for m in messages if isinstance(m , AIMessage) and m.name == name])

  if num_responses >= max_num_turns:
    return "save_interview"

  return "ask_question"

def initiate_all_interviews(state: ResearchGraphState):
    """ This is the "map" step where we run each interview sub-graph using Send API """    

    # Check if human feedback
    human_analyst_feedback=state.get('human_analyst_feedback')
    if human_analyst_feedback:
        # Return to create_analysts
        return "create_analysts"

    # Otherwise kick off interviews in parallel via Send() API
    else:
        topic = state["topic"]
        return [Send("conduct_interview", {"analyst": analyst,
                                           "messages": [HumanMessage(
                                               content=f"So you said you were writing an article on {topic}?"
                                           )
                                                       ]}) for analyst in state["analysts"]]
