from flask import Flask, jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from datetime import timedelta
from dotenv import load_dotenv
import os

# Carrega variáveis do .env
load_dotenv()

app = Flask(__name__)

# Configuração do JWT
app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "default_secret")
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)
jwt = JWTManager(app)

# Swagger UI
SWAGGER_URL = '/swagger'
API_DOC_URL = '/static/swagger.json'  # Certifique-se que esse arquivo existe
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_DOC_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)


@app.route('/')
def home():
    return jsonify(message="API is running"), 200


@app.route('/items', methods=['GET'])
def get_items():
    items = ["item1", "item2", "item3"]
    return jsonify(items=items), 200


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Autenticação simples (apenas como exemplo)
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    return jsonify(message="Credenciais inválidas"), 401


@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(message=f"Bem-vindo, {current_user}! Esta é uma rota protegida."), 200


@app.errorhandler(404)
def not_found(e):
    return jsonify(error="Rota não encontrada"), 404


@app.errorhandler(500)
def internal_error(e):
    return jsonify(error="Erro interno do servidor"), 500


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 1313))
    app.run(host='0.0.0.0', port=port, debug=True)
