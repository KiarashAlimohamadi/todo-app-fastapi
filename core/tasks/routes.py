from fastapi import APIRouter

router = APIRouter(tags=["tasks"],prefix="/todo")


@router.get("/tasks/")
async def tasks_list():
    return []

@router.get("/tasks/{task_id}")
async def task_detail(task_id=int):
    return task_id