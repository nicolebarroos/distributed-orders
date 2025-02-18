from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from app.infra.database import db_instance

app = FastAPI()

async def get_db():
    async for session in db_instance.get_session():
        yield session

@app.get("/ping-db/")
async def ping_db(db: AsyncSession = Depends(get_db)):
    try:
        await db.execute(text("SELECT 1"))
        return {"message": "Database connected ✅"}
    except Exception as e:
        return {"error": str(e)}
