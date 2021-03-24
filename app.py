#!/usr/bin/env python3
from flask import Flask, render_template
from redis import Redis
import os,random

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

images = [
    "cloud-01.png",
    "cloud-02.png",
    "cloud-03.png",
    "cloude-04.png",
    "cloud-05.png"
]

@app.route('/')
def index():
    image_path = "/static/images/" + random.choice(images)

    count = redis.incr('count')
    return render_template('index.html', image_path=image_path, access_count=count)

# Main
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8899))
    try:
        app.run(host="0.0.0.0", port=port, debug=True)
    except Exception as ex:
        print(ex)
