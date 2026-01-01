#=========================== IMPORTS ======================

from sqlalchemy import Column,Integer,String,Boolean,func,Text,DateTime
from core.database import Base


#==========================================================


#================== MODELS =================================

class TaskModel(Base):
    __tablename__ = "tasks"
    id = Column(Integer,autoincrement=True,primary_key=True)
    title = Column(String(150),nullable=False)
    description = Column(Text(500),nullable=True)
    is_completed = Column(Boolean,default=False)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime,server_default=func.now(),server_onupdate=func.now())
