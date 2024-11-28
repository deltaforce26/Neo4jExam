from flask import Blueprint, request, jsonify, current_app
from neo4j import Neo4jDriver, GraphDatabase
from app.repositories.device_repo import DeviceRepository

neo4j_driver = GraphDatabase.driver(
        "bolt://localhost:7687",
        auth=("neo4j", "12345678")
    )

phone_bp = Blueprint('phone_bp', __name__, url_prefix='/api')


@phone_bp.route('/phone_tracker', methods=['POST'])
def get_interaction():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data'}), 400
    if data['devices'][0]['id'] == data['devices'][1]['id']:
        return jsonify({"message": "invalid call"}), 400
    repo = DeviceRepository(neo4j_driver)
    d1_id = repo.insert_devices(data['devices'][0])
    d2_id = repo.insert_devices(data['devices'][1])
    connection_id = repo.connect_devices(data['interaction'] ,d1_id, d2_id)
    return jsonify({"connection_id": connection_id}), 200



@phone_bp.route('/all_by_method', methods=['GET'])
def get_all_by_method():
    method = request.args.get('method')
    if not method:
        return jsonify({'error': 'No method'}), 400
    repo = DeviceRepository(neo4j_driver)
    length = repo.find_by_method(method)
    return jsonify({"length": length}), 200



@phone_bp.route('/all_by_signal', methods=['GET'])
def get_all_by_signal():
    signal_strength = request.args.get('signal')
    repo = DeviceRepository(neo4j_driver)
    res = repo.find_all_by_signal(int(signal_strength))
    print(res)
    return jsonify({"message": str(res)}), 200




@phone_bp.route('/nearest_device_count', methods=['GET'])
def get_nearest_device_count():
    id = request.args.get('id')
    if not id:
        return jsonify({'error': 'No id'}), 400
    repo = DeviceRepository(neo4j_driver)
    device_count = repo.find_nearest_device_count(id)
    return jsonify({"device_count": device_count}), 200



@phone_bp.route('/connected_devices', methods=['GET'])
def get_connected_devices():
    data = request.get_json()
    id1 = data.get('id1')
    id2 = data.get('id2')
    if not id1 or not id2:
        return jsonify({'error': 'No id'}), 400
    repo = DeviceRepository(neo4j_driver)
    res = repo.find_connected_devices(id1, id2)
    return jsonify({"connected_devices": res}), 200




@phone_bp.route('/most_recent_interaction', methods=['GET'])
def get_most_recent_interaction():
    device_id = request.args.get('device_id')
    if not device_id:
        return jsonify({'error': 'No device_id'}), 400
    repo = DeviceRepository(neo4j_driver)
    res = repo.find_most_recent_interaction(device_id)
    return jsonify({"most_recent_interaction": str(res)}), 200


