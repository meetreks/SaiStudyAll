from flask import Flask
from flask import render_template

app = Flask(__name__)


index = '''
        <html>
<head>
    <title>{{ title }} - Microblog</title>
</head>
<body>
<h1>Hello, {{ user.username }}!</h1>
</body>
</html>
        '''

@app.route('/')
@app.route('/index')
def hello_world():
    user = {'username': 'OmSaiRam'}
    return index
    #return render_template(index, title='Home', user=user)
if __name__ == '__main__':
    app.run()