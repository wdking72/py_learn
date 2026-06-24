from sqlalchemy import create_engine

engine = create_engine("sqlite:///shop.db") #sqlite:///shop.db → 数据存为当前目录下的 shop.db 文件 相对路径，三个 /

#ORM 的核心思想：一个 Python 类 = 一张数据库表，每个属性 = 一列。
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Product(Base):
    #- __repr__ = representation，控制 print() 和终端显示的内容
    def __repr__(self):
        return f"<Product(id={self.id}, name={self.name}, price={self.price})>"
    __tablename__ = "products"  # 指定表名

    id = Column(Integer, primary_key=True) #主键
    name = Column(String(100), nullable=False) #商品名
    price = Column(Float) #价格
    stock = Column(Integer, default=0) #库存

#创建表 + 添加数据
Base.metadata.create_all(engine) #创建表

from sqlalchemy.orm import Session
#- with 用完自动关闭连接
with Session(engine) as session:
    exisiting = session.query(Product).filter_by(name = "Python 书").first()
    if not exisiting:
        p1 = Product(name = "Python 书", price = 59.9, stock = 100)
        session.add(p1)
        session.commit() # 必须 commit 才会真正写入！


#Step 5：更新数据
with Session(engine) as session:
    p = session.query(Product).filter_by(name = "Python 书").first()
    p.price = 49.9
    p.stock = 200
    session.commit()

#Step 6：删除数据
with Session(engine) as session:
    p = session.query(Product).filter_by(id = 2).first()
    if p:
        session.delete(p)
        session.commit()

# 查询数据
with Session(engine) as session:
    # 查询所有
    all_product = session.query(Product).all()
    # 按条件查询
    cheap = session.query(Product).filter(Product.price < 100).all()
    # 查询单条
    p = session.query(Product).filter_by(name = "Python 书").first()
#     - .all() → 返回列表，类似 JS 的 findMany()                                                                            
#     - .first() → 返回一条或 None，类似 findFirst()                                                                        
#     - .filter() → 条件查询，里面用 类名.属性 比较                                                                         
#     - .filter_by() → 简写，用 属性名=值，适合精确匹配

print(all_product, cheap, p)