from flask import Blueprint, request, make_response, url_for, redirect
import json, os

std_bp = Blueprint('std', __name__, url_prefix='/std')

filename = 'mock_data/students.txt'


@std_bp.route('/get', methods=('GET', 'POST'))
def get():
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            students = rfile.readlines()
        if students:
            # 返回json格式
            return dict({"date": students})
        else:
            return '没有学生信息！！！'
    else:
        return '文件不存在！！！'
