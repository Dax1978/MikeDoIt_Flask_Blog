from flask import Flask, render_template

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    # return render_template('index.html')
    return render_template('index.html', title='Главная')


if __name__ == '__main__':
    # app.run(debug=True, port=5757)
    app.run(port=5757)