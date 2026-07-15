from asyncio import base_events
from asyncio import base_events
import json


def format_agent_event(event: dict) -> str:

    agent_name = list(event.keys())[0]

    AGENT_NAMES = {
        "planner": "Planner",
        "searcher": "Search Agent",
        "researcher": "Research Agent",
        "writer": "Writer"
    }

    agent = AGENT_NAMES.get(agent_name, agent_name)

    return json.dumps({

        "type": "agent_update",

        "agent": agent,

        "status": "completed",


    }, default=str)


def format_report(report: str) -> str:

    return json.dumps({

        "type": "final_report",

        "report": report

    })


def format_error(message: str) -> str:

    return json.dumps({

        "type": "error",

        "message": message

    })