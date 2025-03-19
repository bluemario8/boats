from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is the home page"

@app.route("/about/<item>")
def about(item):
    return f"{item} is an item"

@app.route("/int/<int:num>")
def integer(num):
    return f"{num} is a number"

@app.route("/html")
def htmlImport():
    return render_template("test.html")

@app.route("/color/<color>")
def htmlImportItem(color):
    return render_template("test2.html", color=color)


if __name__ == '__main__':
    app.run(debug=True)