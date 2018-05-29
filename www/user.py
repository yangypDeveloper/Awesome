#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Yang'


# from orm import Model,StringField,IntegerField

# class User(Model):
#     __table__ = 'users'

#     id = IntegerField(primary_key=True)
#     name = StringField()

# # 创建实例:
# user = User(id=123, name='Michael')
# # 存入数据库:
# user.insert()
# # 查询所有User对象:
# users = User.findAll()
# 
# 
import asyncio, logging


async def main(loop):
    await create_pool(loop, **database)
    user = User()
    user.id = 1
    user.name = 'ZhouXiaorui_miao'
    await user.save()
    return user.name

loop = asyncio.get_event_loop()
database = {
    'host':'39.104.164.113', #数据库的地址
    'user':'root',
    'password':'123456',
    'db':'db'
}
# host=kw.get('host','39.104.164.113'),
# port=kw.get('port',3306),
# user=kw['root'],
# password=kw['123456'],
# db=kw['db'],

task = asyncio.ensure_future(main(loop))

res = loop.run_until_complete(task)
print(res)