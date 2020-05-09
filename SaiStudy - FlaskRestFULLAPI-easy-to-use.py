from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_restplus import Api
#RestPlus is another powerful framework for stuff which further simplifies Restful
app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'about': 'Hello World'}
    def post(self):
        sj = request.get_json()
        return jsonify({'you send': sj}), 201

class Multi(Resource):
    def get(self,num):
        result = num * 9
        return result

api.add_resource(HelloWorld,'/')
api.add_resource(Multi,'/multi/<int:num>')

if __name__ == '__main__':
    app.run()