from fastapi import APIRouter
from fastapi.responses import StreamingResponse


from pydantic import BaseModel

from backend.graphs.graph import graph
from backend.services.stream_service import stream_research

router=APIRouter()

class ResearchRequest(BaseModel):
    query: str


@router.post("/research")
def research(request: ResearchRequest):

    result = graph.invoke(
        {
            "query": request.query,
            "execution_log":[]
        }
        
    )

    return result



@router.get("/research/stream")
def research_stream(query: str):

    return StreamingResponse(
        stream_research(query),
        media_type="text/event-stream"
    )



