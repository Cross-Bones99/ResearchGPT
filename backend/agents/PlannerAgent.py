from backend.services.llm import get_llm
from backend.Schemas.planner_schema import TaskList

llm = get_llm()

planner_llm = llm.with_structured_output(TaskList)  #  the tasklist object


def planner(state):

    query = state["query"]

    response = planner_llm.invoke(
        f"""
        Generate 4-6 research tasks for the following query.

        Query:

        {query}
        """
    )

    return {

            "tasks": response.tasks,

            "current_agent": "Planner",

            "completed_agents": ["Planner"],

            "execution_log": state["execution_log"] + ["Planner completed"]

        }