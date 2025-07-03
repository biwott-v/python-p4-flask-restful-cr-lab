from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Plant(db.Model):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    image = db.Column(db.String(500))
    price = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'image': self.image,
            'price': self.price
        }