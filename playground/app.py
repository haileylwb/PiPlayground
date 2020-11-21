from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hello_world.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/dynamic')
def dynamic():
    greeting = "Welcome to Hailey's Dynamic Page,"
    name = "User 101"
    icecream = ["- vanilla", "- chocolate", "- strawberry", "- green tea"]
    return render_template('dynamic.html', greeting=greeting, name=name, icecream=icecream)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')