from flask import Flask, render_template,request

app = Flask(__name__)

todos = [
    {'todo':'책읽기'},
    {'todo':'잠자기'},
    {'todo':'밥먹기'},
    {'todo':'해보기'}
]

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST' and request.form['todo']:
        todos.append({'todo':request.form['todo']})
    return render_template('index.html', todos=todos)

@app.route('/delete/<todo>', methods=['POST'])
def delete(todo):
    global todos
    todos = [td for td in todos if td['todo'] != todo]
    return render_template('index.html', todos=todos)

            

if __name__ == '__main__':
    app.run(debug=True, port=7890)