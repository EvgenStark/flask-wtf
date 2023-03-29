from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    param = dict()
    param['title'] = 'Заготовка'
    return render_template('base.html', **param)


@app.route('/odd_event')
def odd_even():
    return render_template('odd_event.html', number=2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')