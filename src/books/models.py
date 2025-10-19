from sqlmodel import SQLModel, Field
from typing import Optional
from enum import Enum
import uuid


class Category(str, Enum):
    Personal = "Personal"
    Work = "Work"


class Status(str, Enum):
    active = "active"
    completed = "completed"
    read = "read"


class Marker_model(SQLModel, table=True):
    __tablename__ = "BookMarkersTBL"

    uid: uuid.UUID = Field(default_factory=uuid.uuid4,primary_key=True, index=True)
    url: str = Field(max_length=1048)
    title: str
    description: Optional[str] = Field(default=None, max_length=255)
    category: Optional[Category] = Field(default=None)
    status: Optional[Status] = Field(default=Status.active)

    def __repr__(self):
        return f"<Book {self.title}>"

