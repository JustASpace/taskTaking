from typing import AsyncGenerator

from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config import DB_HOST, DB_NAME, DB_PASS, DB_PORT, DB_USER

DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()  # аналог metadata


engine = create_async_engine(DATABASE_URL)  # точка входа sqlalchemy в наше приложение
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
metadata = MetaData()


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:  # переиспользуем сессии
    async with async_session_maker() as session:
        yield session
