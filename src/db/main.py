from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, create_engine, Session
from src.config import Config
from sqlalchemy import Engine


async_engine = create_engine(
    url=Config.DATABASE_URL,
    echo=True,
)


async def init_db() -> None:
    SQLModel.metadata.create_all(
        bind=async_engine
    )


async def get_session():
    with Session(async_engine) as session:
        yield session
