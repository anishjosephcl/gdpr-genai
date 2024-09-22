from typing import TypedDict, Annotated, Sequence, List
import operator
class CommentsState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]
    rules: Annotated[Sequence[str], operator.add]
    filecontent: Annotated[List[str], operator.add]
    services: Annotated[List[str], operator.add]
    selectedapi: Annotated[List[str], operator.add]
    request: Annotated[List[str], operator.add]
    finalresult: Annotated[List[str], operator.add]
    userid: str
    auditstatus: str