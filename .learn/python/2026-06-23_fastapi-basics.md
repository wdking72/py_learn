# FastAPI 入门笔记

## 1. 安装

```bash
# 安装 FastAPI 和服务器
pip install fastapi uvicorn
```

- `FastAPI` — Web 框架，类似 JS 的 Express
- `uvicorn` — ASGI 服务器，类似 Express 的 `app.listen()`

---

## 2. Hello World

```javascript
// JS Express
const express = require('express');
const app = express();

app.get('/', (req, res) => {
    res.json({ message: '你好世界' });
});

app.listen(3000);
```

```python
# Python FastAPI
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "你好世界"}

# 启动命令：uvicorn fastapi_basic:app --reload
```

**关键点**：
- `@app.get("/")` 是装饰器，注册路由
- `--reload` 代码改了自动重启（开发用）
- 文件名不能以数字开头

---

## 3. 路径参数

```python
@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"你好{name}"}
```

访问 `http://127.0.0.1:8000/hello/小明` → `{"message": "你好小明"}`

---

## 4. 查询参数

```python
@app.get("/search")
def search(q: str, limit: int = 10):
    return {"query": q, "limit": limit}
```

访问 `http://127.0.0.1:8000/search?q=python&limit=5` → `{"query": "python", "limit": 5}`

**关键点**：
- 函数参数就是查询参数
- `limit: int = 10` 表示默认值是 10

---

## 5. POST 请求 + 数据验证

```python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

@app.post("/users")
def create_user(user: User):
    return {"message": f"创建了用户{user.name}, {user.age}岁"}
```

**关键点**：
- `BaseModel` 自动验证请求体
- 类型不对会返回 422 错误
- 类名大写（Python 规范）

---

## 6. 自动文档

访问 `http://127.0.0.1:8000/docs` 打开 Swagger UI，可以直接在浏览器测试 API。

---

## 7. 对比 Express

| 功能 | Express | FastAPI |
|------|---------|---------|
| GET 路由 | `app.get('/', handler)` | `@app.get("/")` |
| 路径参数 | `req.params.name` | 函数参数 `name: str` |
| 查询参数 | `req.query.q` | 函数参数 `q: str` |
| 请求体 | `req.body` | `BaseModel` 自动解析 |
| 数据验证 | 需要 Joi/express-validator | `BaseModel` 内置 |
| API 文档 | 需要额外插件 | 自动生成 Swagger UI |

---

## 8. 启动命令

```bash
# 激活虚拟环境
venv\Scripts\activate

# 启动服务
uvicorn fastapi_basic:app --reload

# 访问
# http://127.0.0.1:8000       → API
# http://127.0.0.1:8000/docs  → Swagger UI
```
