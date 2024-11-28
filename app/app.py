from flask import Flask

from db.database import init_neo4j
from routes.phone_blueprint import phone_bp

app = Flask(__name__)


with app.app_context():
    neo4j_driver = init_neo4j()

app.register_blueprint(phone_bp)

if __name__ == '__main__':
    app.run(debug=True,
            host='0.0.0.0',
            port=5000)