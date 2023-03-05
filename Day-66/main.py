from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
SECRET_KEY = "1234567890"

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/phucnb/100-days-python-challenge/Day-66/cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")
    
## HTTP GET - Read Record
@app.route("/random")
def random_cafe():
    random_cafe = db.session.query(Cafe).order_by(func.random()).first()
    return jsonify(cafe={
        "id": random_cafe.id,
        "name": random_cafe.name,
        "map_url": random_cafe.map_url,
        "img_url": random_cafe.img_url,
        "location": random_cafe.location,
        "seats": random_cafe.seats,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "has_sockets": random_cafe.has_sockets,
        "can_take_calls": random_cafe.can_take_calls,
        "coffee_price": random_cafe.coffee_price
    })

@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    all_cafes = []
    for cafe in cafes:
        all_cafes.append({
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        })
    return jsonify(cafes=all_cafes)

@app.route("/search")
def search_cafe():
    location = request.args.get("loc")
    if not location:
        return jsonify(error={"Invalid Parameter": "Please enter a valid location"})
    
    location = location.title()
    cafes = db.session.query(Cafe).filter_by(location=location).all()
    if cafes:
        all_cafes = []
        for cafe in cafes:
            all_cafes.append({
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            })
        return jsonify(cafes=all_cafes)
    else:
        return jsonify(error={"Not Found": f"Sorry, we don't have a cafe at {location}"})
    
## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add_cafe():
    data = request.form
    if data.get("name") and data.get("map_url") and data.get("img_url") and data.get("location") and data.get("seats") and data.get("has_toilet") and data.get("has_wifi") and data.get("has_sockets") and data.get("can_take_calls") and data.get("coffee_price"):
        new_cafe = Cafe(
            name=data.get("name"),
            map_url=data.get("map_url"),
            img_url=data.get("img_url"),
            location=data.get("location"),
            seats=data.get("seats"),
            has_toilet=bool(data.get("has_toilet")),
            has_wifi=bool(data.get("has_wifi")),
            has_sockets=bool(data.get("has_sockets")),
            can_take_calls=bool(data.get("can_take_calls")),
            coffee_price=data.get("coffee_price")
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    else:
        return jsonify(error={"Invalid Parameter": "Please enter all required fields."})

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    new_price = request.args.get("new_price")
    if not new_price:
        return jsonify(error={"Invalid Parameter": "Please enter a valid price."})
    
    cafe = db.session.query(Cafe).get(cafe_id)
    if cafe:
        cafe.coffee_price = new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."})


## HTTP DELETE - Delete Record
@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    key = request.args.get("api-key")
    if key == SECRET_KEY:
        cafe_to_delete = db.session.query(Cafe).filter_by(id=cafe_id)
        if not cafe_to_delete.first():
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
        cafe_to_delete.delete()
        db.session.commit()
        return jsonify(response={"success": "Successfully deleted the cafe."}), 200
    else:
        return jsonify(error={"Invalid API Key": "Sorry, that's not allowed. Make sure you have the correct API key."}), 403
    



if __name__ == '__main__':
    app.run(debug=True)
