from flask import jsonify
from app.api import bp


@bp.route('/test', methods=['GET'])
def test():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('写出第一个flask小demo')