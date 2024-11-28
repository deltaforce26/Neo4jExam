from flask import Flask
from routes.phone_blueprint import phone_bp

app = Flask(__name__)




app.register_blueprint(phone_bp)

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)