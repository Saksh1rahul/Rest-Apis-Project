
from flask.views import MethodView
from flask_smorest import Blueprint,abort
from flask_jwt_extended import jwt_required,get_jwt
from sqlalchemy.exc import SQLAlchemyError,IntegrityError,OperationalError
from flask import jsonify
from db import db
from models import ItemModel
from schemas import ItemSchema,ItemUpdateSchema

blp = Blueprint("items",__name__, description ="Operations on items")
  
@blp.route("/item/<int:item_id>")

class Item(MethodView):
    @jwt_required()
    @blp.response(200,ItemSchema)
    def get(self,item_id):
        item = ItemModel.query.get_or_404(item_id)
        return item
    
    @jwt_required()
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200,ItemSchema)           
    def put(self, item_data, item_id):
        item = ItemModel.query.get(item_id)
        if item:
            for key,value in item_data.items():
                setattr(item,key,value)
            db.session.add(item)
            db.session.commit()    
            return item
        abort(404,message="item not found")      

    @jwt_required()
    def delete(self,item_id):
        jwt=get_jwt()
        if not jwt.get("is_admin"):
            abort(401,message="Admin privilege required")

        item = ItemModel.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return {"message":"item deleted"}
    
    
@blp.route("/item")
class itemlist(MethodView):
    @jwt_required()
    @blp.response(200,ItemSchema(many=True))
    def get(self):
        return ItemModel.query.all()
    
    @jwt_required(fresh=True)
    @blp.arguments(ItemSchema)
    @blp.response(201,ItemSchema)
    def post(self,item_data):
        print(item_data)
        item = ItemModel(**item_data)
        
        try:
            db.session.add(item)
            db.session.commit()
            return item, 201
        
        except IntegrityError as e:
            db.session.rollback()
            abort(400, message=f"Integrity error:{e}")
        
        except OperationalError as e:
            db.session.rollback()
            abort(500,message=f"Database error:{e}")
                    
        except SQLAlchemyError as e:
            db.session.rollback()
            abort(500,message=f"an error occured while inserting the item:{e}")
                
       
    
   
   