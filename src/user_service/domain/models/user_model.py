import datetime 
import uuid
from sqlmodel import SQLModel, Field

class User(SQLModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    username: str = Field(index=True, unique=True)
    user_document: str = Field(index=True, unique=True)
    email: str = Field(index=True, unique=True)
    