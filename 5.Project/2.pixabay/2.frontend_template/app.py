from flask import Flask, jsonify, url_for, render_template, request

app = Flask(__name__)

images = [
    {"filename":"calendar.jpg", "keywords": ["city", "light", "sky"]},
    {"filename":"cat.jpeg", "keywords": ["cat", "pet", "cute"]},
    {"filename":"cat2.jpeg", "keywords": ["cat", "kitty", "cute"]},
    {"filename":"cat3.jpeg", "keywords": ["dog", "pet", "park"]},
    {"filename":"starbucks.png", "keywords": ["coffee", "logo", "starbucks"]}
]

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search')
def search():
    query = request.args.get("q", "").lower()
    results = []
    
    for item in images:
        # found = False
        # for keyword in item["keywords"]:
        #     if query in keyword:
        #         found = True
        #         # break # 이미지 하나만 찾고 말거다.
        # if found:
        #     image_url = url_for('static', filename=f'img/{item["filename"]}')
        #     results.append(image_url)
        
        # pythonic하게 한줄로...
        if any(query in keyword for keyword in item["keywords"]):
            image_url = url_for('static', filename=f'img/{item["filename"]}')
            results.append(image_url)
    
    # return jsonify({"url": results})  # 순수 BE개발자는 여기까지...
    return render_template("results.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
    