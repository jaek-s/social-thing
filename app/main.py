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
    docs_url="/api/docs",
    redoc_url="/api/redoc",
    openapi_url="/api/openapi.json",
)
main_router = APIRouter(prefix="/api")

main_router.include_router(posts.router)
main_router.include_router(comments.router)

app.include_router(main_router)
