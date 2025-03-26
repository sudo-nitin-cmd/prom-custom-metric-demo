from flask import Flask, jsonify, request
import random
import time
from prometheus_client import start_http_server, Counter, Histogram

app = Flask(__name__)

# Prometheus Metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total number of HTTP requests', ['method', 'endpoint', 'http_status'])
REQUEST_DURATION = Histogram('http_request_duration_seconds', 'Time taken for a request', ['endpoint'])

@app.route('/users')
def get_users():
    start_time = time.time()
    
    # Simulate a random delay
    time.sleep(random.uniform(0.1, 0.5))

    # Simulating an API response
    if random.random() < 0.1:  # Simulate 10% failure rate
        REQUEST_COUNT.labels(method='GET', endpoint='/users', http_status='500').inc()
        return jsonify({'error': 'Internal Server Error'}), 500

    REQUEST_COUNT.labels(method='GET', endpoint='/users', http_status='200').inc()
    REQUEST_DURATION.labels(endpoint='/users').observe(time.time() - start_time)
    
    return jsonify({"users": ["Alice", "Bob", "Charlie"]})

if __name__ == '__main__':
    # Start metrics server on port 8000
    start_http_server(8000)
    app.run(host='0.0.0.0', port=5000)

