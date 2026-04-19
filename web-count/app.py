from flask import Flask, render_template
import random

app = Flask(__name__)

images = [
    "cloud-01.png",
    "cloud-02.png",
    "cloud-03.png",
    "cloud-04.png",
    "cloud-05.png",
    "docker_logo.png",
    "k8s_logo.png"
]

@app.route('/')
def index():
    image_path = "/static/images/" + random.choice(images)
    count = 1
    return render_template('index.html', image_path=image_path, visit_count=count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8899)
