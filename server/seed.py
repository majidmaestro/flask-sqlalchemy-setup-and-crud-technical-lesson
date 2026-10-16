from faker import Faker
from random import choice, randint

from app import app
from models import db, Pet

fake = Faker()
SPECIES = ["Dog", "Cat", "Rabbit", "Hamster", "Parrot"]

with app.app_context():
    Pet.query.delete()

    pets = [
        Pet(name=fake.first_name(), species=choice(SPECIES), age=randint(1, 12))
        for _ in range(15)
    ]
    db.session.add_all(pets)
    db.session.commit()
    print(f"Seeded {len(pets)} pets")
