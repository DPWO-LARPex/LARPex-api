from sqlalchemy.orm import Session
from models.qr import QrModel
from schemas.qr.qr_post_schema import QrPostSchema
from config.exceptions import NotFoundException, ObjectAlreadyExistsException

def processQRCode(qr_id: int, db: Session):
    qr: QrModel = db.query(QrModel).filter(QrModel.qr_id == qr_id).first()
    if (qr is None):
        raise NotFoundException(detail="User not found")
    '''
    else:
        return url
    '''