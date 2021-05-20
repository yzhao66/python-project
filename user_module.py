from  datetime import  datetime
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from connect import Base

class User(Base):
    __tablename__ = 'user'
    id=Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(20))
    password = Column(String(50))


    def __repr__(self):  ##
        return """<User(id=%s,username=%s,password=%s,creatime=%s,_locked=%s)>

            """ % (
            self.id,
            self.username,
            self.password,

        )

##创建表
if __name__ =="__main__":
    Base.metadata.create_all()    ##去数据库里面创建所有的表
