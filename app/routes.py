from flask import request, jsonify, render_template
from .models import WebhookEvent
import uuid

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event = WebhookEvent(
        req_id=str(uuid.uuid4()),
        event_type=data['event_type'],
        author=data['author'],
        from_branch=data.get('from_branch', ''),
        to_branch=data['to_branch'],
        timestamp=data['timestamp']
    )
    event.save()
    return jsonify({"status": "success"}), 201

@app.route('/')
def index():
    events = WebhookEvent.objects().order_by('-timestamp')[:10]
    return render_template('index.html', events=events)
