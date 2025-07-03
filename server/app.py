from flask import Flask, jsonify, request
from models import db, Plant
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///plants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create tables and add initial plant
with app.app_context():
    db.create_all()
    # Ensure plant with ID=1 exists
    if not Plant.query.get(1):
        initial_plant = Plant(
            name="Test Plant",
            image="https://example.com/image.jpg",
            price=9.99
        )
        db.session.add(initial_plant)
        db.session.commit()

@app.route('/plants', methods=['GET'])
def get_plants():
    plants = Plant.query.all()
    return jsonify([plant.to_dict() for plant in plants])

@app.route('/plants/<int:id>', methods=['GET'])
def get_plant_by_id(id):
    plant = Plant.query.get(id)
    if plant:
        return jsonify(plant.to_dict())
    return jsonify({"error": "Plant not found"}), 404

@app.route('/plants', methods=['POST'])
def create_plant():
    data = request.json
    new_plant = Plant(
        name=data['name'],
        image=data.get('image'),
        price=data.get('price')
    )
    db.session.add(new_plant)
    db.session.commit()
    return jsonify(new_plant.to_dict()), 201

if __name__ == '__main__':
    app.run(port=5555, debug=True)