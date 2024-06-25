from flask import Blueprint, request, jsonify
import requests
import os
import pika_sender as send
bp = Blueprint('gateway', __name__)

INVEN_APP_HOST = os.getenv('INVEN_APP_HOST')
INVENTORY_PORT = os.getenv('INVEN_APP_PORT')

@bp.route('/api/billing', methods=['POST'])
def post_billing():
    if not request.is_json:
        return jsonify({'message': 'body is not json'}), 400
    data = request.get_json()
    send.mq_sneder(data)
    return jsonify({'message': 'body received successfully'}), 200

@bp.route('/<path:path>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def movies_api(path):
    parts = path.split('/')
    if parts[0] != 'api' or parts[1] != 'movies':
        return jsonify({'message': 'service not found'}), 404
    try:
        response = requests.request(
            method=request.method,
            url=f"http://{INVEN_APP_HOST}:{INVENTORY_PORT}/{path}",
            headers=request.headers,
            data=request.get_data(),
            params=request.args
        )
        return (response.text, response.status_code, response.headers.items())
    except Exception as e:
            return jsonify(error=f"{e}"), 500
