#=================== IMPORTS ======================================

from fastapi import APIRouter,Path
from tasks.schemas import *
from tasks.models import TaskModel

#===================================================================


#================ ROUTER SETUP =====================================
router = APIRouter(tags=["tasks"],prefix="/todo")
#===================================================================



#========================= FUNCTIONS ===============================

@router.get("/tasks/")
async def tasks_list():
    return []

@router.get("/tasks/{task_id}")
async def task_detail(task_id=int):
    return task_id

@router.post("/tasks")
async def create_task():
    return []

@router.put("/tasks/{task_id}")
async def update_task(task_id:int = Path(...,gt=0)):
    return []

@router.delete("tasks/{task_id}")
async def delete_task(task_id:int = Path(...,gt=0)):
    return []

#===================================================================