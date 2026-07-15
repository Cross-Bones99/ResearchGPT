from backend.services.llm import llm


def writer(state):

    research = state["research"]

    prompt = f"""
    Write a professional research report.

    Research:

    {research}

    Format using Markdown.
    """

    response = llm.invoke(prompt)

    return {
        "report": response.content,

        "execution_log": state["execution_log"] + ["Writer Agent completed"]
    }