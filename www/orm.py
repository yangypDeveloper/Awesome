#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Yang'

import asyncio, logging
import aiomysql

@asyncio.coroutine
def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool = yield from aiomysql.create_pool(
        host=kw.get('host','39.104.164.113'),
        port=kw.get('port',3306),
        user=kw['root'],
        password=kw['123456'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=ke.get('minsize',1)
        loop=loop
    )
