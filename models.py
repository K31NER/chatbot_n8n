from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel,Field

class CreateProject(BaseModel):
    name: str 
    description: str 

class Project(SQLModel, table = True):
    id: Optional[int] = Field(primary_key=True)
    name: str = Field()
    description: str = Field()
    class Config:
        from_attributes = True
        