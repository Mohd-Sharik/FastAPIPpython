# routers/users.py
from fastapi import APIRouter, Depends, HTTPException
from db import get_db
from model.user import User
from bson import ObjectId
from bson.errors import InvalidId

router = APIRouter(prefix="/users", tags=["users"])

# Utility to validate ObjectId
def is_valid_object_id(id: str) -> bool:
    return ObjectId.is_valid(id)


# Helper to convert MongoDB documents to JSON-serializable dicts
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@router.post("/adduser")
async def create_user(user: User, db=Depends(get_db)):
    user_dict = user.dict()
    result = await db.users.insert_one(user_dict)
    return {"id": str(result.inserted_id)}


@router.get("/getuser")
async def get_user( db=Depends(get_db)):
    users = []
    cursor = db.users.find({})
    async for document in cursor:
        document["_id"] = str(document["_id"])  # Convert ObjectId to string
        users.append(document)
    return users


@router.get("/user/{user_id}")
async def get_user_by_id(user_id: str, db=Depends(get_db)):
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="Invalid ID format")

    user = await db.users.find_one({"_id": obj_id})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    user["_id"] = str(user["_id"])
    return user


# DELETE API - delete by ID
@router.delete("/items/{item_id}")
async def delete_item(item_id: str, db=Depends(get_db)):
    if not is_valid_object_id(item_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await db.users.delete_one({"_id": ObjectId(item_id)})

    if result.deleted_count == 1:
        return {"message": "Item deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Item not found")




# PUT API - update item by ID
@router.put("/items/{item_id}")
async def update_item(item_id: str, item: User, db=Depends(get_db)):
    if not is_valid_object_id(item_id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    update_data = {k: v for k, v in item.dict().items() if v is not None}
    if not update_data:
        raise HTTPException(status_code=400, detail="No data to update")

    result = await db.users.update_one(
        {"_id": ObjectId(item_id)},
        {"$set": update_data}
    )

    if result.modified_count == 1:
        return {"message": "Item updated successfully !!!"}
    else:
        raise HTTPException(status_code=404, detail="Item not found or not modified")
