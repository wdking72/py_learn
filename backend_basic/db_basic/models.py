from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey

Base = declarative_base()
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True) #主键
    name = Column(String(100))
    email = Column(String(100))
    posts = relationship("Post", back_populates="user")
    # relationship() 的第一个参数是你要到达的目标：
    # back_populates 就是让这两张通讯录互相指向对方。

class Post(Base):
    __tablename__ = "posts"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String())
    user_id = Column(Integer, ForeignKey("users.id")) # 外键，指向 users 表的 id
    age = Column(Integer)
    user = relationship("User", back_populates="posts")
