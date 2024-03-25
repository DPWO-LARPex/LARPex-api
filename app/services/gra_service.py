from sqlalchemy.orm import Session
from models.gra import Gra
from schemas.gra.gra_post_schema import GraPostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def get_gra_item_by_id(id_gry: int, db: Session):
    db_gra: Gra = db.query(Gra).filter(Gra.id_gry == id_gry).first()
    if(db_gra is None):
        raise NotFoundException()
    
    return db_gra

def get_gry_items_by_osoba_id(id_osoby: int, db: Session):
    return db.query(Gra).filter(Gra.id_osoby == id_osoby)

def add_gra_item(gra: GraPostSchema, db: Session):
    db_gra: Gra = db.query(Gra).filter(Gra.nazwa == gra.nazwa).first()
    if(db_gra is not None):
        raise ObjectAlreadyExistsException(detail="Gra o podanej nazwie juz istnieje")

    db_gra = Gra(
        opis_gry=gra.opis_gry,
        nazwa=gra.nazwa,
        max_liczba_graczy=gra.max_liczba_graczy,
        id_osoby=gra.id_osoby,
        status=gra.status,
        trudnosc=gra.trudnosc,
        scenariusz=gra.scenariusz)
    db.add(db_gra)
    db.commit()
    db.refresh(db_gra)
    return db_gra

def get_all_gra_items(db: Session):
    return db.query(Gra).all()

def edit_gra_item(id_gry: int, gra: GraPostSchema, db: Session):
    db_gra = db.query(Gra).filter(Gra.nazwa == gra.nazwa).first()
    if(db_gra is not None and db_gra.id_gry != id_gry):
        raise ObjectAlreadyExistsException(detail="Gra o podanej nazwie juz istnieje")
    db_gra = db.query(Gra).filter(Gra.id_gry == id_gry).first()
    if(db_gra is None):
        raise NotFoundException()
    db_gra.opis_gry = gra.opis_gry
    db_gra.nazwa = gra.nazwa
    db_gra.max_liczba_graczy = gra.max_liczba_graczy
    db_gra.id_osoby = gra.id_osoby
    db_gra.status = gra.status
    db_gra.trudnosc = gra.trudnosc
    db_gra.scenariusz = gra.scenariusz
    
    db.commit()
    db.refresh(db_gra)
    return db_gra

def delete_gra_item(id_gry: int, db: Session):
    db_gra = db.query(Gra).filter(Gra.id_gry == id_gry).first()
    if(db_gra is None):
        raise NotFoundException()
    db.delete(db_gra)
    db.commit()
    return db_gra