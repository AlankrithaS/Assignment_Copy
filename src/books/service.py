from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from src.books.models import Marker_model
from src.books.schemas import Marker_Create_model, MarkerUpdate_model


class BookService:
    async def get_all_bookmarks(self, session: AsyncSession):
        statement = select(Marker_model).order_by(Marker_model.title.asc())
        result = session.exec(statement)
        return result.all()

    async def get_bookmark_by_id(self, book_uid: str, session):
        statement = select(Marker_model).where(Marker_model.uid == book_uid)
        result = session.exec(statement)
        result = result.first()
        result = result.model_dump()
        if result is None:
            return {"error": "Bookmark not found"}
        # print("=====================================")
        # print(result)
        # print("=====================================")
        return Marker_Create_model.model_validate(result).model_dump()

    async def create_bookmark(self, book_data: Marker_Create_model, session: AsyncSession):
        book_data_dick = book_data.model_dump()
        new_book = Marker_model(
            **book_data_dick
        )
        session.add(new_book)
        session.commit()
        return new_book

    async def update_bookmark(self, book_uid: str, update_data: MarkerUpdate_model, session: AsyncSession):
        book_to_update = await self.get_bookmark_by_id(book_uid, session)
        if book_to_update is not None:
            update_data_dict = update_data.model_dump()
            for k, v in update_data_dict.items():
                book_to_update[k] = v
            session.commit()
            return book_to_update

    async def delete_bookmark(self, book_uid: str, session: AsyncSession):
        # book_to_delete = await self.get_bookmark_by_id(book_uid, session)
        statement = select(Marker_model).where(Marker_model.uid == book_uid)
        result = session.exec(statement)
        book_to_delete = result.first()
        # book_to_delete = Marker_model(**book_to_delete)
        print("=====================================")
        print(book_to_delete)
        print("=====================================")
        if book_to_delete is not None:
            session.delete(book_to_delete)
            session.commit()
            return {"message":"succesfully deleted"}
        else:
            return None
