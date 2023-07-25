from fastapi import FastAPI
from app.models.organization_models import Base
from app.db.database import engine
from app.router import organizations

app = FastAPI(title="Yogdaan fosscu api")

Base.metadata.create_all(bind=engine)

app.include_router(organizations.router)

