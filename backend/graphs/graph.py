from langgraph.graph import StateGraph,START,END

from backend.state.agent_state import AgentState
from backend.agents.PlannerAgent import planner
from backend.agents.ResearcherAgent import researcher
from backend.agents.WriterAgent import writer
from backend.agents.SearchAgent import search_agent


graph_builder=StateGraph(AgentState)
graph_builder.add_node("planner",planner)
graph_builder.add_node("searcher",search_agent)
graph_builder.add_node("researcher",researcher)
graph_builder.add_node("writer",writer)

graph_builder.add_edge(START,"planner")
graph_builder.add_edge("planner","searcher")
graph_builder.add_edge("searcher","researcher")
graph_builder.add_edge("researcher","writer")
graph_builder.add_edge("writer",END)

graph=graph_builder.compile()

