from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

#O padrão Singleton garante que sempre utilizamos a mesma conexão com o banco, 
#evitando múltiplas conexões desnecessárias e melhorando a performance.
class Database:
    _instance = None
    _engine = None
    _SessionLocal = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._setup()
        return cls._instance

    @classmethod
    def _setup(cls):
        DATABASE_URL = os.getenv("DATABASE_URL")

        #Criando o engine assíncrono
        cls._engine = create_async_engine(DATABASE_URL, echo=True)

        #Criando um sessionmaker assíncrono
        cls._SessionLocal = sessionmaker(
            bind=cls._engine, class_=AsyncSession, expire_on_commit=False
        )

    async def get_session(self):
        async with self._SessionLocal() as session:
            yield session

Base = declarative_base()
db_instance = Database()