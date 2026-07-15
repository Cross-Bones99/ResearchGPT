from backend.services.llm import get_llm

llm = get_llm()


def researcher(state):
    """
    Research Agent

    Responsibilities:
    -----------------
    1. Read search results
    2. Analyze information
    3. Remove duplicates
    4. Produce research notes
    """

    search_results = state["search_results"]

    formatted_results = ""
    
     # Keep only successful search results
    successful_results = [
        item for item in search_results if item.success
    ]

    failed_results = [
        item for item in search_results if not item.success
    ]

    # If everything failed, don't waste an LLM call
    if not successful_results:

        return {
            "research": " Unable to retrieve information from any search provider.",

            "current_agent": "Research Agent",

            "completed_agents": state["completed_agents"] + [
                "Research Agent"
            ]
        }

    
    for item in successful_results:
        formatted_results += f"""
==================================

    Task:
    {item.task}

    Search Results:
    {item.result}

    """

        prompt = f"""
    You are a Senior Research Analyst.

    You have collected search results from multiple searches.

    Your job is to:

    - Analyze the information.
    - Merge duplicate information.
    - Organize everything logically.
    - Mention conflicting information.
    - Mention missing information if any.
    - DO NOT invent facts.

    Search Results:

    {formatted_results}

    Produce detailed research notes in Markdown.
    """

    response = llm.invoke(prompt)

    return {

        "research": response.content,

        "current_agent": "Research Agent",

        "completed_agents": state["completed_agents"] + ["Research Agent"],

        "execution_log": state["execution_log"] + ["Research Agent completed"]   

    }