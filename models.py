from app import db
from sqlalchemy import Integer, Unicode, Column

class Example(db.Model):
    __tablename__ = 'example'
    id = Column('id', Integer, primary_key=True)
    data = Column('data', Unicode)

    def __init__(self, id, data):
        self.id = id
        self.data = data