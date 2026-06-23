from fastapi import FastAPI
from pydantic import BaseModel #自动帮你验证请求体，类型不对会报错。

app = FastAPI()

@app.get('/') #把下面的函数注册为处理 GET 请求的路由
def root() :
    return {"message": "hello world"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message":f"你好{name}"}

#查询参数
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
#uvicorn 10_fastapi_basic:app --reload
# - 10_fastapi_basic → 文件名（去掉 .py）                                                                               
# - app → 你代码里的 app = FastAPI()                                                                                    
# - --reload → 代码改了自动重启（开发用）

class User(BaseModel):
    name: str
    age: int
@app.post("/users")
def create_user(user: User):
    return {"message": f"创建了用户{user.name}, {user.age}岁"}

@app.put("/user/{user_id}")
def update(user_id: int, user: User):
    return {"message":f"更新了{user_id}： {user}, {user.age}岁"}
@app.delete("/user/{user_id}")
def delete(user_id: int):
    return {"message":f"删除了用户{user_id}"}