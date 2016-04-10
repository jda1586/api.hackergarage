#!/usr/bin/python
# coding=utf-8

class Config(object):
    DEBUG = True
    HOST = '127.0.0.1'
    PORT = 5000
    SECRET_KEY = '^*d^032DZQX48221d3ZA'

    MONGO_HOST = 'localhost'
    MONGO_PORT = '27017'
    MONGO_DBNAME = 'quotes'


class LocalConfig(Config):
    DEBUG = True


class DevelopConfig(Config):
    HOST = '0.0.0.0'
