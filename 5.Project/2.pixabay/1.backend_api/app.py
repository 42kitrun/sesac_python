from flask import Flask, jsonify, url_for
import random

app = Flask(__name__)

dog_images = [
    'calendar.jpg',
    'cat.jpeg',
    'cat2.jpeg',       
    'cat3.jpeg',       
    'starbucks.png'
]

@app.route('/random-dog')
def random_dog():
    random_img = random.choice(dog_images)
    # image_url = url_for('static', filename=f'img/{random_img}') # 상대경로가 만들어짐
    image_url = url_for('static', filename=f'img/{random_img}', _external=True) # 절대경로 만들기
    return jsonify({"url": image_url})

if __name__ == "__main__":
    app.run(debug=True, port=7890)