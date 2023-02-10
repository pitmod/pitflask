from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_pit():
    return 'Hello Pit'

if __name__ == '__main__':
    app.run()
