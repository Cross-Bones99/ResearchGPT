from pydantic import BaseModel, Field
from typing import Optional



class SearchResult(BaseModel):
    """
    Represents the result of searching
    one research task.
    """

    task: str = Field(
        description="Research task"
    )

    result: str = Field(
        description="Search result returned from Tavily"
    )



    source: str = Field(
        default="Tavily",
        description="Search provider"
    )

    success: bool = Field(
        default=True
    )

    error: Optional[str] = Field(
        default=None
    )



