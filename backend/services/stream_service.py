from typing import Generator

from backend.graphs.graph import graph

from backend.utils.event_formatter import (
    format_agent_event,
    format_report,
    format_error
)


def stream_research(query: str) -> Generator[str, None, None]:
    """
    Stream LangGraph execution as Server-Sent Events (SSE).

    Yields:
        Agent completion events
        Final report event
        Error event (if any)
    """

    initial_state = {
        "query": query,
        "tasks": [],
        "search_results": [],
        "research": "",
        "report": "",
        "current_agent": "",
        "completed_agents": [],
        "execution_log": [],
    }

    try:

        for event in graph.stream(
            initial_state,
            stream_mode="updates"
        ):

            # ------------------------------------------
            # Stream the completed agent event
            # ------------------------------------------

            yield f"data: {format_agent_event(event)}\n\n"

            # ------------------------------------------
            # Check whether this event contains the report
            # ------------------------------------------

            payload = next(iter(event.values()))

            report = payload.get("report")

            if report:

                yield f"data: {format_report(report)}\n\n"

    except Exception as e:

        yield f"data: {format_error(str(e))}\n\n"