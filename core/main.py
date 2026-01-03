
from fastapi import FastAPI
from contextlib import asynccontextmanager
from tasks.routes import router as tasks_routes
from users.routes import router as users_route


@asynccontextmanager
async def lifespan(app:FastAPI):
    print("started")
    yield
    print("shut down")


app = FastAPI(lifespan=lifespan)

app.include_router(tasks_routes)
app.include_router(users_route)