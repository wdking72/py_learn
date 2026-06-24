# SQLAlchemy ORM 基础笔记

## 1. 什么是 ORM

ORM = Object Relational Mapping（对象关系映射）

用 Python 类定义数据库表，不用写 SQL。

| 概念 | Python (SQLAlchemy) | JS (Prisma) |
|------|---------------------|-------------|
| 连接数据库 | `create_engine("sqlite:///shop.db") | `new PrismaClient()` |
| 定义表 | `class Product(Base):` | `model Product { ... }` |
| 定义列 | `Column(Integer, primary_key=True)` | `id Int @id` |

---

## 2. 安装

```bash
pip install sqlalchemy
```

---

## 3. 定义模型

```python
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base

engine = create_engine("sqlite:///shop.db")  # 三个斜杠 = 相对路径
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"  # 表名

    id: int = Column(Integer, primary_key=True)      # 主键
    name: str = Column(String(100), nullable=False)   # 不能为空
    price: float = Column(Float)                       # 浮点数
    stock: int = Column(Integer, default=0)            # 默认值 0

    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
```

**关键点**：
- `__tablename__` 指定表名
- `primary_key=True` 主键
- `nullable=False` 不能为空
- `default=0` 默认值
- `__repr__` 控制 print() 输出
- 类型注解 `: int`、`: float` 消除编辑器警告（可选）

---

## 4. 创建表

```python
Base.metadata.create_all(engine)  # 表不存在就创建，已存在则跳过
```

---

## 5. CRUD 操作

所有操作都通过 `Session`：

```python
from sqlalchemy.orm import Session

with Session(engine) as session:
    # 增
    p = Product(name="Python 书", price=59.9, stock=100)
    session.add(p)
    session.commit()  # 必须提交！

    # 查
    all_products = session.query(Product).all()           # 全部
    cheap = session.query(Product).filter(Product.price < 100).all()  # 条件
    one = session.query(Product).filter_by(name="Python 书").first()  # 单条

    # 改
    p.price = 49.9
    session.commit()

    # 删
    session.delete(p)
    session.commit()
```

### filter vs filter_by

```python
# filter — 复杂条件，用 类名.属性
session.query(Product).filter(Product.price > 100)
session.query(Product).filter(Product.name == "Python 书")

# filter_by — 简单等值，用 属性名=值
session.query(Product).filter_by(name="Python 书")
```

---

## 6. 防止重复插入

```python
with Session(engine) as session:
    existing = session.query(Product).filter_by(name="Python 书").first()
    if not existing:
        p = Product(name="Python 书", price=59.9, stock=100)
        session.add(p)
        session.commit()
```

---

## 7. ORM vs SQL 对比

| 操作 | ORM | 原生 SQL |
|------|-----|----------|
| 创建表 | `Base.metadata.create_all()` | `CREATE TABLE ...` |
| 插入 | `session.add(Product(...))` | `INSERT INTO ...` |
| 查询 | `session.query(Product).all()` | `SELECT * FROM ...` |
| 条件 | `.filter(Product.price > 100)` | `WHERE price > 100` |
| 更新 | `p.price = 49.9` | `UPDATE ... SET price=49.9` |
| 删除 | `session.delete(p)` | `DELETE FROM ...` |

---

## 8. SQLite 连接字符串

```python
# 相对路径（三个斜杠）
engine = create_engine("sqlite:///shop.db")

# 绝对路径（四个斜杠）
engine = create_engine("sqlite:////tmp/shop.db")
```

---

## 下一步

- 关系查询（一对多、多对多）
- Alembic 数据库迁移
