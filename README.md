# 🚀 Laboratório API Web

Este projeto foi desenvolvido como parte de um **desafio proposto em laboratório** na disciplina de DeVops. O objetivo foi criar uma **API RESTful** com Python e Flask, implementando **autenticação via JWT**, documentação com **Swagger** e conteinerização utilizando **Docker** e **Docker Compose**.

---

## 📦 Tecnologias Utilizadas

- Python 3.9
- Flask
- Flask-JWT-Extended
- Flask-Swagger-UI
- Docker & Docker Compose

---

## 🔧 Como Executar Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/seu-usuario/lab_api.git
cd lab_api
```
### 2. Criar e ativar o ambiente virtual (opcional)
```
python -m venv .venv
source .venv/Scripts/activate  # Windows
# ou
source .venv/bin/activate      # Linux/Mac
```

### 3. pip install -r requirements.txt
```
pip install -r requirements.txt
```
### 4. Executar localmente com Flask
```
python app.py
```

## 🐳 Executar com Docker
### 1. Build e run usando Docker Compose
```
docker-compose up --build
```
### 2. Acessar a API
- Home: http://localhost:1313/
- Itens: http://localhost:1313/items
- Swagger UI: http://localhost:1313/swagger

## 📄 Documentação com Swagger
O Swagger UI está configurado para ler o arquivo static/swagger.json.

Acesse:
http://localhost:1313/swagger

## ✍🏿 Autor
Miguel Ectil
