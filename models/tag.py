from db import db

class TagModel(db.Model):

    __tablename__="tags"
    __table_args__ = (db.UniqueConstraint('name', 'store_id', name='_tag_uc'),)

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80),nullable=False)
    store_id = db.Column(db.Integer,db.ForeignKey("stores.id"), unique=False,nullable=False)
    store = db.relationship("StoreModel",back_populates="tags")
    items = db.relationship("ItemModel",back_populates="tags",secondary = "item_tags")