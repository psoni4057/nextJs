from typing import TypedDict, Annotated, Sequence, List
import operator
class DataState(TypedDict):
    messages: Annotated[Sequence[str], operator.add]
    input_text: str
    rules: Annotated[Sequence[str], operator.add]
    filecontent: Annotated[List[str], operator.add]
    services: Annotated[List[str], operator.add]
    selectedapi: Annotated[List[str], operator.add]
    request: Annotated[List[str], operator.add]
    finalresult: Annotated[List[str], operator.add]
    userid: str
    auditstatus: str
    image: str
    results: Annotated[Sequence[str], operator.add]
    grammar: str
    sentiment: str