from pydantic import BaseModel,Field
from typing import Optional
from datetime import datetime



class TaskBaseSchema(BaseModel):
    title : str = Field(...,max_length=150,min_length=5,description="Title of the Task")
    description : Optional[str] = Field(None,max_length=500,description="Write something about your task")
    is_completed : bool = Field(...,description="State of the task")



class TaskCreateSchema(TaskBaseSchema):
    pass


class TaskUpdateSchema(TaskBaseSchema):
    pass


class TaskResponseSchema(TaskBaseSchema):
    id : int = Field(...,description="id for the task(task number)")
    created_at :datetime = Field(...,description="creation date and time of the task")
    updated_at :datetime = Field(...,description="update date and time of the task")

    model_config = {
        "from_attributes": True
    }