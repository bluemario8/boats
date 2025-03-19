from flask import Flask, render_template, request
from sqlalchemy import create_engine, text

app = Flask(__name__)
conn_str = "mysql://root:cset155@localhost/boatdb"
engine = create_engine(conn_str, echo=True)
conn = engine.connect()


@app.route('/')
def main():
    return render_template("index.html")


@app.route('/<name>')
def user(name):
    return render_template("user.html", name=name)


@app.route('/boats', methods=['GET'])
def boats():
    boats = conn.execute(text("select * from boats")).all()
    return render_template("boats.html", boats=boats[:10], id=None)


@app.route('/boats', methods=['POST'])
def boatsPost():
    id = request.form["search_id"]
    print("id: " + str(id))
    if id != "":
        boats = conn.execute(text(f"SELECT * FROM boats WHERE id = {id}")).all()
    else:
        boats = conn.execute(text("select * from boats")).all()
    return render_template("boats.html", boats=boats[:10], id=id)


@app.route('/createBoat', methods=['GET'])
def getBoat():
    return render_template("boat_create.html")


@app.route('/createBoat', methods=['POST'])
def createBoat():
    try:
        conn.execute(text("INSERT INTO boats VALUES (:id, :name, :type, :owner_id, :rental_price)"), request.form)
        conn.commit()
        return render_template("boat_create.html", error=None, success="Successful")
    except:
        return render_template("boat_create.html", error="Failed", success=None)


if __name__ == "__main__":
    app.run(debug=True)
