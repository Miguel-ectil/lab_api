from flask import Flask, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# Swagger UI
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

@app.route('/')
def home():
    return jsonify(message="API is running")

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items=["item1", "item2", "item3"])

@app.route('/login', methods=['POST'])
def login():
    access_token = create_access_token(identity="user")
    return jsonify(access_token=access_token)

@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    return jsonify(message="Protected route")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1313)
