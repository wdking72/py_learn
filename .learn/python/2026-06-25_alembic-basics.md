# Alembic 数据库迁移基础

## 什么是 Alembic
数据库版本管理工具，类比 Git 管理代码版本，Alembic 管理数据库结构版本。

## 核心工作流程
1. 改模型（models.py）
2. 生成迁移：`alembic revision --autogenerate -m "描述"`
3. 执行迁移：`alembic upgrade head`

## 配置要点
- `alembic.ini`：设置 `sqlalchemy.url` 数据库连接地址
- `alembic/env.py`：导入模型 `from models import Base`，设置 `target_metadata = Base.metadata`
- 注意删除模板自带的 `target_metadata = None`，否则会覆盖

## 常用命令
| 命令 | 说明 |
|------|------|
| `alembic init alembic` | 初始化迁移项目 |
| `alembic revision --autogenerate -m "msg"` | 自动生成迁移脚本 |
| `alembic upgrade head` | 升级到最新版本 |
| `alembic downgrade -1` | 回滚一步 |
| `alembic history` | 查看迁移历史 |
| `alembic current` | 查看当前版本 |

## Windows 注意事项
- `alembic.ini` 中不要写中文注释，GBK 编码会报错
- 路径用正斜杠 `/` 或 `%(here)s` 代替反斜杠

## 踩过的坑
1. `env.py` 中 `target_metadata = None` 覆盖了之前的设置
2. `relationship()` 的第一个参数是目标类名，写反了会指向自己
3. `alembic.ini` 中文注释导致 GBK 解码错误
