
from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("started")
    yield
    print("shut down")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_routes)