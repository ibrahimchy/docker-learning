import os
from flask import Flask
import redis

app = Flask(__name__)
redis_host: os.getenv('REDIS_HOST', 'redis')
redis_port: int(os.getenv('REDIS_PORT', 6379))
r = redis.Redis(host=redis_host, port=redis_port)


@app.route('/')
def welcome():
    return "Welcome to the Flask + Redis App!"

@app.route('/count')
def count():
    count = r.incr('visits')
    return f"Visit count: {count}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)