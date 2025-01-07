from flask import Flask, render_template, request, jsonify



app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks = tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return jsonify({'task': task})

@app.route('/delete', methods=['POST'])
def delete_task():
    task = request.form.get('task')
    if task in tasks:
        tasks.remove(task)
    return jsonify({'task': task})

if __name__ == '__main__':
    app.run(debug=True)