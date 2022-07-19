# coding: utf-8
from application import db


class Account(db.Model):
    __tablename__ = 'account'

    id = db.Column(db.BigInteger, primary_key=True, info='账户Id')
    email = db.Column(db.String(64, 'utf8_bin'), nullable=False, unique=True, info='邮箱')
    name = db.Column(db.String(32, 'utf8_bin'), nullable=False, unique=True, info='账户名')
    password = db.Column(db.String(256, 'utf8_bin'), nullable=False, info='密码')
    register_time = db.Column(db.DateTime, server_default=db.FetchedValue(), info='注册时间')
    login_time = db.Column(db.DateTime, info='上一次登录时间')
