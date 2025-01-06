from flask import (Flask, jsonify, request, send_from_directory, redirect)
from flask_cors import CORS
from dotenv import load_dotenv
import uuid
load_dotenv()

import os

# from endpoints.archivo import nombre_def
# from endpoints.archivo_2 import nombre_def_2

cors_origins = os.getenv('CORS_ORIGINS', '*').split(',')

app = Flask(__name__)

CORS(app, resources={
    r"/*": {
        "origins": cors_origins if cors_origins else "*", # Si no se define, permitir todos los orígenes
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/')
def home():
    return send_from_directory('static','index.html')

@app.errorhandler(404)
def not_found(e):
    return redirect('/'), 404

@app.after_request
def handle_cors(response):
    # Obtener el origen de la solicitud
    origin = request.headers.get('Origin')
    
    # Si el origen no está en la lista permitida, redirigir a la raíz
    if origin not in cors_origins and cors_origins != ['*']:
        response.status_code = 302  # Código de redirección
        response.headers['Location'] = '/'  # Redirige a la raíz
        response.data = b''  # Limpia el cuerpo de la respuesta
    
    return response

# @app.route('/endpoint-1/<var>', methods=['GET'])
# def function_name_route(var):
#     try:
#         example = nombre_def(var)
#         return jsonify(example), 200
#     except RuntimeError as e:
#         return jsonify({"message": "Error message", "error": str(e)}), 500

# @app.route('/endpoint-2', methods=['POST'])
# def function_name_2_route():
#     input_data = request.json
#     if not input_data:
#         return jsonify({"message": "El cuerpo de la solicitud está vacío o no es JSON válido."}), 400
#     try:
#         example = nombre_def_2(input_data)
#         return jsonify(example), 200
#     except RuntimeError as e:
#         return jsonify({"message": "Error message", "error": str(e)}), 500

# El puerto esta configurado en el 8080, ya que las App Service para Python utilizan dicho puerto de escucha

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True, port=8080)
