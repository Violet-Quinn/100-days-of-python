import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
import random

load_dotenv()

TopSecretApiKey = os.environ['API_KEY']

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)


    def to_dict(self):
        #Method 1.
        dictionary = {}
        # Loop through each column in the data record
        for column in self.__table__.columns:
            #Create a new dictionary entry;
            # where the key is the name of the column
            # and the value is the value of the column
            dictionary[column.name] = getattr(self, column.name)
        return dictionary


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

# HTTP GET - Read Record
@app.route("/random",methods=["GET"])
def get_random_cafe():
    result=db.session.execute(db.select(Cafe))
    all_cafes=result.scalars().all()
    random_cafe=random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all",methods=["GET"])
def get_all_cafes():
    result=db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafes=result.scalars().all()
    return jsonify(cafes=[cafe.to_dict()for cafe in all_cafes])

@app.route("/find",methods=["GET"])
def find_cafe():
    query_location=request.args.get("loc")
    cafes=db.session.execute(db.select(Cafe).where(Cafe.location==query_location))
    specific_area_cafes=cafes.scalars().all()
    if not specific_area_cafes:
        return jsonify(error="No cafes found")
    return jsonify(cafes=[cafe.to_dict()for cafe in specific_area_cafes])

# HTTP POST - Create Record
@app.route("/add",methods=["POST","GET"])
def add_cafe():
    if request.method == "POST":
        new_cafe=Cafe(
            name=request.form.get("name"),
            map_url=request.form.get("map_url"),
            img_url=request.form.get("img_url"),
            location=request.form.get("location"),
            has_sockets=bool(request.form.get("sockets")),
            has_toilet=bool(request.form.get("toilet")),
            has_wifi=bool(request.form.get("wifi")),
            can_take_calls=bool(request.form.get("calls")),
            seats=request.form.get("seats"),
            coffee_price=request.form.get("coffee_price"),
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."})
    return render_template("add.html")

# HTTP PUT/PATCH - Update Record
@app.route("/update-price/<cafe_id>",methods=["PATCH"])
def update_price(cafe_id):
    new_price=request.args.get("new_price")
    cafe=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
    if cafe:
        cafe.coffee_price=new_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."}),200
    else:
        return jsonify(response={"error": "Failed to update the price."}),404

# HTTP DELETE - Delete Record
@app.route("/report-closed/<cafe_id>",methods=["DELETE"])
def report_closed(cafe_id):
    api_key=request.args.get("api_key")
    if api_key==TopSecretApiKey:
        cafe_to_close=db.session.execute(db.select(Cafe).where(Cafe.id==cafe_id)).scalar()
        if cafe_to_close:
            db.session.delete(cafe_to_close)
            db.session.commit()
            return jsonify(response={"success": "Successfully closed the cafe."}),200
        else:
            return jsonify(response={"error": "No such cafe exist in database."}),404
    else:
        return jsonify(response={"forbidden": "Invalid API key."}),404


if __name__ == '__main__':
    app.run(debug=True)
