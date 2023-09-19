from datetime import datetime

from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable
from sqlalchemy import Table, Column, Integer, String, TIMESTAMP, Boolean, Identity, ARRAY

from src.database import Base
from src.database import metadata


user = Table(
    "user",
    metadata,
    Column("id", Integer, Identity(start=1, always=True), primary_key=True),
    Column("email", String, nullable=True),
    Column("username", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("role_id", Integer, nullable=False),
    Column("invited_by", Integer, nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("max_task_available", Integer, nullable=True),
    Column("score_sum", Integer, nullable=True),
    Column("has_unchecked_tasks", Boolean, nullable=True),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
)


class User(SQLAlchemyBaseUserTable[int], Base):  # класс создан из-за fastapi users, библиотеке удобнее работать так
    id = Column(Integer, Identity(start=1, always=True), primary_key=True)
    email = Column(String, nullable=False)
    username = Column(String, nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    role_id = Column(Integer, nullable=False)
    invited_by = Column(Integer, nullable=True)
    hashed_password: str = Column(String(length=1024), nullable=False)
    max_task_available = Column(Integer, nullable=True)
    score_sum = Column(Integer, nullable=True)
    has_unchecked_tasks = Column(Boolean, nullable=True)
    is_active: bool = Column(Boolean, default=True, nullable=False)
    is_superuser: bool = Column(Boolean, default=False, nullable=False)
    is_verified: bool = Column(Boolean, default=False, nullable=False)
