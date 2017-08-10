from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('hello.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def aboutMe():
    return render_template('about.html')


app.run(debug=True)
