from flask import Flask, request, jsonify
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['webhook_db']
collection = db['events']

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    event_type = data.get('event_type')
    author = data.get('author')
    from_branch = data.get('from_branch', '')
    to_branch = data.get('to_branch')
    timestamp = data.get('timestamp')

    if event_type in ['push', 'pull_request', 'merge']:
        event_data = {
            'event_type': event_type,
            'author': author,
            'from_branch': from_branch,
            'to_branch': to_branch,
            'timestamp': datetime.strptime(timestamp, '%a %b %d %H:%M:%S UTC %Y')
        }
        collection.insert_one(event_data)
        return jsonify({'status': 'success'}), 200
    return jsonify({'status': 'error'}), 400

@app.route('/events', methods=['GET'])
def get_events():
    events = list(collection.find({}, {'_id': 0}))
    return jsonify(events), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)
