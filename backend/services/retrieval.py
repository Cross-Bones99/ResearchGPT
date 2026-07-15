"""
Responsible for

Searching
Parallel execution
Timeouts
Retries
Caching (later)
Ranking (later)
Everything related to retrieval.
"""




from concurrent.futures import ThreadPoolExecutor,as_completed
from backend.tools.tool_registry import TOOLS
from backend.Schemas.search_schema import SearchResult
import time

search = TOOLS["search"]


def search_single_task(task: str) -> SearchResult:
    """
    Search one task and return a SearchResult object.
    """
    

    try:
        result=search(task)
        return SearchResult(
            task=task,
            result=result
        )
    
    except Exception as e:
        return SearchResult(
            task=task,
            result="",
            success=False,
            error=str(e)
        )




def retrieve(tasks: list[str]) -> list[SearchResult]:
    """
    Search all tasks in parallel.
    """

    start=time.perf_counter()
    
    results = []

    with ThreadPoolExecutor(max_workers=5) as executor:

        futures = [

            executor.submit(
                search_single_task,
                task
            )

            for task in tasks

        ]

        for future in as_completed(futures):

            results.append(
                future.result()
            )

    endtime=time.perf_counter()

    print(f"\nTotal Search Time: {endtime-start:.2f} seconds")  
    
    
    return results    

