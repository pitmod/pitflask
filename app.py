from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_pit():
    return 'Hello Piter. This is some test flask app.'

if __name__ == '__main__':
    app.run()
