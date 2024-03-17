from fastapi import APIRouter,Depends
import json
router = APIRouter(
    prefix="/data",
    tags=["Fetching"]
    )

with open("./questions.json") as f:
        q_data = json.load(f)
list_cat = []
for i in q_data:
    list_cat.append(i["category"])         

@router.get("/user/{category}")
def select(category: str):
     ind = list_cat.index(list_cat[category])     
     return q_data[ind]

@router.get("/user/")
def all():
    return q_data


           
      