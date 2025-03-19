from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('indexold.html')


@app.route('/<name>')
def greeting(name):
    return render_template('user.html', name=name)


@app.route("/hello")
def hello():
    return "Hello"

@app.route("/hello/<int:name>")
def helloName(name):
    return "Hello " + str(name)

@app.route("/coffee")
def servingCoffee():
    return "Here is your coffee"


@app.route("/donut")
def servingDonut():
    return "Here is your donut"

if __name__ == "__main__":
    app.run(debug=True)

    