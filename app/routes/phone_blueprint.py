from flask import Blueprint, request, jsonify

phone_bp = Blueprint('phone_bp', __name__, url_prefix='/api')


@phone_bp.route('/phone_tracker', methods=['POST'])
def get_interaction():
    print(request.json)
    return jsonify({}), 200