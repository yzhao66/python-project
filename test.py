import meta as meta

from connect import session
from user_module import User
import uuid
##增
def add_user():
    #person = User(username = 'xps',password='123')
    #session.add(person)  #增加一条数据
    session.add_all([    #增加多条数据
        User(username = 'xpss',password='123'),
        User(username = 'xpss',password='123'),
        User(username = 'xpsss',password='123'),
    ])
    session.commit() #提交
##查
def search_user():
    rows= session.query(User).all()

##改
def update_user():
    rows=session.query(User).filter(User.username=='xpss').update({User.password:1})
    session.commit()
##删除
def delete_user():
    rows = session.query(User).filter(User.username =='xpss')[0]

    session.delete(rows)   #删除第一条记录
    #rows.deleted()   #批量删除
    session.commit()
def chaxun():
    row = session.query(User).filter(User.username == 'xpss')
    for i in row:
        print(i)

if __name__ =="__main__":
    add_user()
    search_user()
    update_user()
    delete_user()
    #chaxun()