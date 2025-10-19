from fastapi import APIRouter, status, Depends
from fastapi.exceptions import HTTPException
from typing import List
from sqlmodel.ext.asyncio.session import AsyncSession
# from .marker_data import bookmarks
from src.books.schemas import Marker_model, MarkerUpdate_model
from src.books.service import BookService
from src.db.main import get_session

book_router = APIRouter()
book_service = BookService()


@book_router.get("/", response_model=List[Marker_model])
async def get_bookmarks(session: AsyncSession = Depends(get_session)):
    bookmarks = await book_service.get_all_bookmarks(session)
    return bookmarks


@book_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Marker_model)
async def create_a_bookmark(book_data: Marker_model, session: AsyncSession = Depends(get_session)) -> dict:
    print(book_data)
    new_bookmark = await book_service.create_bookmark(book_data, session)
    return new_bookmark
    # return book_data


@book_router.get("/{id}")
async def find_bookmark(id: str, session: AsyncSession = Depends(get_session)) -> dict:
    book = await book_service.get_bookmark_by_id(id, session)
    if book:
        return book
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=f"Bookmark with id {id} not found")


@book_router.patch("/{id}", response_model=Marker_model)
async def update_bookmark(id: str, book_update_data: MarkerUpdate_model, session: AsyncSession = Depends(get_session)) -> dict:
    update_book = await book_service.update_bookmark(
        id, book_update_data, session)
    if update_book:
        return update_book
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bookmark with id {id} not found to update")


@book_router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_bookmark(id: str, session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_bookmark(id, session)
    if book_to_delete:
        return {"message":"succesfully deleted"}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bookmark with id {id} not found to delete")
