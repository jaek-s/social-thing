from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.routing import APIRoute

from app.db import init_db
from app.routers import posts, comments


def generate_route_id(route: APIRoute):
    return f"{route.tags[0]}-{route.name}"


@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json",
    root_path="http://localhost:8000/",
    generate_unique_id_function=generate_route_id,
)

app.include_router(posts.router)
app.include_router(comments.router)
