from contextlib import asynccontextmanager

from fastapi import (
    FastAPI,
    APIRouter,
)

from app.db import init_db
from app.routers import posts, comments


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
)

app.include_router(posts.router)
app.include_router(comments.router)
