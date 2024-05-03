from flask import Blueprint, request, jsonify
import pika_sender as send
bp = Blueprint('gateway', __name__)

@bp.route('/api/billing', methods=['POST'])
def post_billing():
    if not request.is_json:
        return jsonify({'message': 'body is not json'}), 400
    data = request.get_json()
    send.mq_sneder(data)
    return jsonify({'message': 'body received seccessfully'}), 200
    