from langgraph.graph import END, START,StateGraph
from langgraph.checkpoint.memory import MemorySaver
from agents.rule_agent import rule_agent
from agents.gdpr_agent import gdpr_agent
from agents.audit_agent import audit_agent
from state.comments_state import CommentsState

workflow = StateGraph(CommentsState)

workflow.add_node("rule_agent", rule_agent)
workflow.add_node("gdpr_agent", gdpr_agent)
workflow.add_node("audit_agent", audit_agent)
workflow.add_edge(START,"rule_agent")
workflow.add_edge('rule_agent','gdpr_agent')
workflow.add_edge('gdpr_agent','audit_agent')
workflow.add_edge("audit_agent",END)

# Set up memory
memory = MemorySaver()

commentsapp = workflow.compile()