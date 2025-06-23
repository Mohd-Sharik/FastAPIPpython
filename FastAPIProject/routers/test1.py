""" 
from fastapi import APIRouter, Request, HTTPException, Depends
#from fastapi import FastAPI,
from db import get_db
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson import ObjectId

router = APIRouter(
    prefix="/users",
    tags=["users"]
)


router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Helper to convert MongoDB documents to JSON-serializable dicts
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc



# GET all items
@router.get("/items")
def get_all_items(db=Depends(get_db)):
    try:
      #  cursor = db.tes1.find({})
       # items = list(collection.find())
       # print([serialize_doc(item) for item in items])
      #  return [serialize_doc(item) for item in items]
      users = []
      cursor = db.users.find({})
      print( print([serialize_doc(item) for item in cursor]))
      print(cursor)
      async for doc in cursor:
          doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
          users.append(doc)
      return users
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/dataB")
async def datab():
   return

@router.get("/htmlTem", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

    """


