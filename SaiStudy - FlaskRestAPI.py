from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def hello_world():
    if(request.method == 'POST'):
        sj = request.get_json()
        return jsonify({'you send': sj}), 201
    else:
        return  jsonify({'about':'Hello World'})
@app.route('/sairam/<int:num>', methods=['GET'])
def somefunc(num):
    result = num * 9
    return jsonify({'result':result})
if __name__ == '__main__':
    app.run()