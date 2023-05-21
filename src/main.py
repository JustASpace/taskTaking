from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from starlette.staticfiles import StaticFiles
# from redis import asyncio as aioredis

from src.auth.base_config import fastapi_users, auth_backend
from src.auth.schemas import UserRead, UserCreate
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

app.mount("/static", StaticFiles(directory='src/static'), name="static")


@app.get("/")
async def root():
    return RedirectResponse('pages/startpage', status_code=302)


# @app.on_event("startup")
# async def startup():
#     redis = aioredis.from_url("redis://localhost")
#     FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
