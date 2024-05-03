from flask import Blueprint, request, jsonify
import requests
import pika_sender as send
bp = Blueprint('gateway', __name__)

@bp.route('/api/billing', methods=['POST'])
def post_billing():
    if not request.is_json:
        return jsonify({'message': 'body is not json'}), 400
    data = request.get_json()
    send.mq_sneder(data)
    return jsonify({'message': 'body received seccessfully'}), 200

@bp.route('/<path:path>', methods=['GET', 'PUT', 'POST', 'DELETE'])
def movies_api(path):
    service_mapping = { "movies": "http://127.0.0.1:8080" }
    try:
        response = requests.request(
            method=request.method,
            url=f"http://127.0.0.1:8080/{path}",
            headers=request.headers,
            data=request.get_data(),
            params=request.args
        )
        return (response.text, response.status_code, response.headers.items())
    except Exception as e:
            return jsonify(error=f"{e}"), 500