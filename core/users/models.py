from sqlalchemy import Column,String,TEXT,Boolean,func,Integer,DateTime
from core.database import Base
from sqlalchemy.orm import relationship




class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(250),nullable=False)
    password = Column(String(),nullable=False)
    is_active = Column(Boolean,default=True)
    created_at = Column(DateTime,server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now(), server_onupdate=func.now())

    tasks = relationship("TaskModel",back_populates="user")

    def __repr__(self):
        return (f'user : {self.id}')

