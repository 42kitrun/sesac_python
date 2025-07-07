from flask import Flask
from flask import send_file, send_from_directory


app = Flask(__name__)

@app.route('/') # /search?q=apple&page=2
def home():
    # return send_file('static/index.html')
    return send_from_directory('static', 'index.html')

if __name__  == '__main__':
    app.run(debug=True, port =7800)