from pydantic import BaseModel
from typing import Optional
from .models import Category, Status
import uuid


class Marker_model(BaseModel):
    url: str
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"


class Marker_Create_model(BaseModel):
    url: str
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"


class MarkerUpdate_model(BaseModel):
    url: str
    title: str
    description: Optional[str] | None = None
    category: Optional[Category] | None = None
    status: Optional[Status] | None = "active"
