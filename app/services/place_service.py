from sqlalchemy.orm import Session
from models.place_model import PlaceModel
from schemas.place.place_post_schema import PlacePostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def add_place_to_event(place: PlacePostSchema, db: Session):
    db_Place = PlaceModel(
        number=place.number,
        street=place.street,
        city=place.city
   )

    db.add(db_Place)
    db.commit()
    db.refresh(db_Place)

    return db_Place


def delete_place_item(place_id: int, db: Session):
    db_Place = db.query(PlaceModel).filter(PlaceModel.id == place_id).first()
    if (db_Place is None):
        raise NotFoundException()
    db.delete(db_Place)
    db.commit()

    return db_Place