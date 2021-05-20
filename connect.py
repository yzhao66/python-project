from sqlalchemy import create_engine
import pymysql

HOSTNAME= '120.78.124.94'
PORT='3306'
DATABASE = 'test'
USERNAME = 'root'
PASSWORD = 'Xibaoda@2020'

##连接数据连接 URL
Db_url = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,
    PASSWORD,
    HOSTNAME,
    PORT,
    DATABASE,

)
## 连接数据库
engine=create_engine(Db_url)

##创建Moudle

## 表
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base(engine)  ####基类

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(engine)
session= Session() #实例

## 测试
if __name__ == "__main__":
    conection=engine.connect()
    result=conection.execute('select 1')
    print(result.fetchone())