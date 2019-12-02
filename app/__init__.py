from flask import Flask

app = Flask(__name__)

from app.routes import routes

app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081)