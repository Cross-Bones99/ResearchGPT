from backend.services.retrieval import retrieve

def search_agent(state):

    tasks=state["tasks"]

    search_results=retrieve(tasks)

    return {
        "search_results": search_results,
        
        "current_agent": "Search Agent",

        "completed_agents": state["completed_agents"] + ["Search Agent"],
        
        "execution_log": state["execution_log"] + ["Search Agent completed"]

    }

    