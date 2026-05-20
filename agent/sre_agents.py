from typing import List, Literal
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict, Annotated
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

class SREState(TypedDict):
    alert: dict
    messages: Annotated[list, add_messages]
    root_cause: str
    affected_service:List[str]
    severity: Literal["low","medium","high","critical"]
    remediation_plan: str
    awaiting_approval: bool
    actions_taken: List[str]
    postmortem_report: str


def RCA_Agent(state: SREState):
    pass

def Remediate_Agent(state: SREState):
    pass

def Postmortem_Agent(state: SREState):
    pass


workflow = StateGraph(SREState)

workflow.add_node("RCA_agent", RCA_Agent )
workflow.add_node("Remediate_agent", Remediate_Agent)
workflow.add_node("Postmortem_agent", Postmortem_Agent)

workflow.add_edge(START, "RCA_agent")
workflow.add_edge("RCA_agent","Remediate_agent")
workflow.add_edge("Remediate_agent","Postmortem_agent")
workflow.add_edge("Postmortem_agent", END)

app = workflow.compile(checkpointer=memory)

