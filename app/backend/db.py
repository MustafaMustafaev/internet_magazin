from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine, AsyncSession

engine = create_async_engine('postgresql+asyncpg://postgres:postgres@localhost:5432/ecommerce', echo=True)
async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

class Base(DeclarativeBase):
    pass

