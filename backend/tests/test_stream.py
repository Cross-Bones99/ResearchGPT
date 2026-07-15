from backend.graphs.graph import graph

state = {
    "query": "Compare LangGraph and CrewAI",
    "execution_log": []
}

for event in graph.stream(state):

    print("=" * 60)

    print(event)