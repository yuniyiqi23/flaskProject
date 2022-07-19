# coding: utf-8
from application import db


class AccountRole(db.Model):
    __tablename__ = 'account_role'

    account_id = db.Column(db.BigInteger, primary_key=True, nullable=False, info='账户Id')
    role_id = db.Column(db.BigInteger, primary_key=True, nullable=False, index=True, info='角色Id')
