from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', name='Puwadon', project_url='https://github.com/ipuwadon/my_python_project')

if __name__ == '__main__':
    app.run(debug=True)