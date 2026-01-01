#=================== IMPORTS ======================================

from fastapi import APIRouter,Path,Depends,HTTPException
from fastapi.responses import JSONResponse
from tasks.schemas import *
from tasks.models import TaskModel
from sqlalchemy.orm import Session
from core.database import get_db
from typing import List
from datetime import datetime


#===================================================================


#================ ROUTER SETUP =====================================
router = APIRouter(tags=["tasks"],prefix="/todo")
#===================================================================



#========================= FUNCTIONS ===============================

@router.get("/tasks/",response_model=List[TaskResponseSchema])
async def tasks_list(db:Session = Depends(get_db)):
    result = db.query(TaskModel).all()
    return result






@router.get("/tasks/{task_id}",response_model=TaskResponseSchema)
async def task_detail(task_id=int,db:Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Not Found!")
    return task





@router.post("/tasks",response_model=TaskResponseSchema)
async def create_task(task:TaskCreateSchema,db:Session = Depends(get_db)):
    new_task = TaskModel(title=task.title,description=task.description,is_completed=task.is_completed)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task




@router.put("/tasks/{task_id}",response_model=TaskResponseSchema)
async def update_task(task:TaskUpdateSchema,task_id:int = Path(...,gt=0),db:Session = Depends(get_db)):
    task_obj = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task_obj:
        raise HTTPException(status_code=404, detail="Not Found!")
    task_obj.title = task.title
    task_obj.description = task.description
    task_obj.is_completed = task.is_completed
    now = datetime.now()
    task_obj.updated_at = now
    db.commit()
    db.refresh(task_obj)
    return task_obj




@router.delete("tasks/{task_id}",status_code=204)
async def delete_task(task_id:int = Path(...,gt=0),db:Session = Depends(get_db)):
    task = db.query(TaskModel).filter(TaskModel.id == task_id).first()
    if not task:
        raise HTTPException(status_code=404,detail="Not Found!")
    db.delete(task)
    db.commit()


#===================================================================