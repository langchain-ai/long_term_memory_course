from pydantic import BaseModel, Field
from typing import List, TypedDict

class State(TypedDict):
    user_input: str
    routing_decision: str
    journal_output: str

class UserProfile(BaseModel):
    name: str = Field(None, description="User's full name")
    location: str = Field(None, description="User's primary location/city")
    workplace: str = Field(None, description="User's place of work")
    relationships: list[dict] = Field(None, description="User's relationships")

class Memory(BaseModel):
    memory_type: str = Field(None, description="Type of memory to extract.")
    memory_content: str = Field(None, description="Specific content of the memory.")

class Memories(BaseModel):
    memories: List[Memory] = Field(None, description="List of memories to extract.")

class MemorySearch(BaseModel):
    collection: str=Field(None, description="Name of the memory collection to search" )

class Example(BaseModel):
    example_input: str = Field(None, description="Input for the example.")
    example_output: str = Field(None, description="Output for the example.")

class Examples(BaseModel):
    examples: List[Example] = Field(None, description="List examples.")
