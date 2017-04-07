from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/test')
def test():
    user1 = {'name': 'liuruichao1', 'age': 20}
    user2 = {'name': 'liuruichao2', 'age': 20}
    _list = [
        user1,
        user2
    ]
    return render_template("index.html", _list = _list, name = 'liuruichao')

@app.route('/add')
def add():
    username = request.args.get('username')
    return "SUCCESS"

if __name__ == '__main__':
    app.run()
