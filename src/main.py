from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
from redis import asyncio as aioredis

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate, UserUpdate
from src.pages.router import router as router_pages
from src.tasks.router import router as router_tasks
# uvicorn src.main:app --reload
app = FastAPI(
    title='TaskTaking'
)

app.include_router(router_tasks)
app.include_router(router_pages)
app.include_router(fastapi_users.get_auth_router(auth_backend),
                   prefix='/auth/jwt',
                   tags=['auth'])
app.include_router(fastapi_users.get_register_router(UserRead, UserCreate),
                   prefix='/auth',
                   tags=['auth'])
app.include_router(fastapi_users.get_users_router(UserRead, UserUpdate, False),
                   prefix="/users",
                   tags=["users"])


# CORS
# Список сайтов, с которых можно обращаться к API
origins = [
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin",
                   "Authorization"],
)

app.mount("/static", StaticFiles(directory='src/static'), name="static")


@app.get("/")
async def root():
    return RedirectResponse('pages/signin', status_code=302)


@app.on_event("startup")
async def startup():
    redis = aioredis.from_url("redis://localhost")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
