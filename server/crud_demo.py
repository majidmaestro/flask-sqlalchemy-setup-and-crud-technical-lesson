from sqlalchemy.exc import IntegrityError

from app import app
from models import db, Pet

with app.app_context():
    db.create_all()

    # CREATE
    db.session.add_all([
        Pet(name="Luna", species="Cat"),
        Pet(name="Rocky", species="Dog"),
        Pet(name="Coco", species="Rabbit"),
    ])
    db.session.commit()
    print("Created:", Pet.query.all())

    # READ
    print("Dogs:", Pet.query.filter_by(species="Dog").all())
    print("Not adopted:", Pet.query.filter_by(adopted=False).count())

    # UPDATE
    rocky = Pet.query.filter_by(name="Rocky").first()
    rocky.adopted = True
    db.session.commit()
    print("Updated:", rocky)

    # DELETE
    coco = Pet.query.filter_by(name="Coco").first()
    db.session.delete(coco)
    db.session.commit()
    print("After delete:", Pet.query.all())

    # CONSTRAINT TEST: name is required
    try:
        db.session.add(Pet(name=None, species="Dog"))
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        print("Constraint works: name cannot be NULL")
