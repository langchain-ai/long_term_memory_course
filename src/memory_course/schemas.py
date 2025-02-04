from pydantic import BaseModel, Field
from typing import List, TypedDict, Literal, Annotated
import operator
class Router(BaseModel):
    classification: Literal["ignore", "respond", "notify"] = Field(
        None, 
        description="The classification of an email: 'ignore' for irrelevant emails, "
        "'notify' for important information that doesn't need a response, "
        "'respond' for emails that need a reply"
    )

class State(TypedDict):
    email_input: str
    routing_decision: str
    messages: Annotated[list, operator.add]


