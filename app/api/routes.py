from . import api_bp
from flask import request, jsonify
from flask_jwt_extended import jwt_required
from app.services.conversion_service import convert_currency

@api_bp.route('/convert', methods=['POST'])
@jwt_required()
def convert():
    data = request.get_json()
    result = convert_currency(data['amount'], data['currency_from'], data['currency_to'])
    return jsonify(result)
