# from src.auth.database import
from sqlmodel import SQLModel, Field
from sqlalchemy import Column, Integer, String
import uuid


class User(SQLModel, table=True):
    __tablename__ = "jwt_users"

    id: uuid.UUID = Field(default_factory=uuid.uuid4,
                          primary_key=True, index=True)
    email: str = Column(String, unique=True)
    hashed_password: str = Column(String, nullable=False)
