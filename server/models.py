from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False, index=True)
    species = db.Column(db.String(50), nullable=False)
    adopted = db.Column(db.Boolean, default=False)
    age = db.Column(db.Integer)

    def __repr__(self):
        return f"<Pet {self.id}: {self.name} ({self.species}) adopted={self.adopted}>"
