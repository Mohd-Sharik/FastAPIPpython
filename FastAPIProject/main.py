#from typing import Union

# main.py
from fastapi import FastAPI
from routers import users

app = FastAPI()
app.include_router(users.router)



"""
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from bson import ObjectId

app = FastAPI()



app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


conn = MongoClient("mongodb+srv://sharikkhan9012:H78WuXGwxONveKf4@projectcrud.wfwxigx.mongodb.net")
db = conn["notes"]
collection = db["notes"]

# Helper to convert MongoDB documents to JSON-serializable dicts
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc



# GET all items
@app.get("/items")
def get_all_items():
    try:
        items = list(collection.find())
        print([serialize_doc(item) for item in items])
        return [serialize_doc(item) for item in items]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@app.get("/item/{item_id}")
def read_item(item_id: int):
   try:
       item = list(collection.find_one({"_id": ObjectId(item_id)}))
       print([serialize_doc(item) for item in item])
       return {"item_id": item_id}
   except Exception as e:
       raise HTTPException(status_code=500, detail=str(e))

@app.get("/dataB")
async def datab():
    docs = conn.notes.notes.find_one({})
    print(docs)

@app.get("/htmlTem", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


"""