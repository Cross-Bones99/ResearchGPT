from typing import TypedDict
from backend.Schemas.search_schema import SearchResult

class AgentState(TypedDict):

    query: str

    tasks: list[str]

    search_results: list[SearchResult]

    research: str

    report: str

    current_agent: str

    completed_agents: list[str]


    execution_log:list[str]   #Keeps track of the agent progress like example ;- Planner started Planner completed