from src.auth.auth import router as auth_router
from fastapi import FastAPI
from src.books.routes import book_router
from contextlib import asynccontextmanager
from src.db.main import init_db



@asynccontextmanager
async def life_span(app: FastAPI):
    print(f'server is starting...')
    await init_db()
    yield
    print(f'server is shutting down...')

version = "v1"

app = FastAPI(
    title="Bookmarks API",
    version=version,
    lifespan=life_span
)

app.include_router(
    book_router, prefix=f"/api/{version}/bookmarker", tags=["bookmarks"])

app.include_router(
    auth_router, prefix=f"/api/{version}/auth", tags=["auth"])
