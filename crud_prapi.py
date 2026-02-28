from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

# アイテムを作成するためのリクエストボディのモデルを定義
class ItemCreate(BaseModel):
    name: str = Field(..., min_length=1)
    price: int = Field(..., gt=0)

# アイテムのレスポンスモデルを定義。ItemCreateを継承して、idフィールドを追加する。
class ItemResponse(ItemCreate):
    id: int

# アイテムのデータを保存する為のリスト。
items_db: List[ItemResponse] = []

# 作成API
# リクエストボディとしてItemCreateモデルを受け取り、レスポンスとしてItemResponseモデルを返す。
# ステータスコードは201（Created）を指定。
@app.post("/items/", response_model = ItemResponse, status_code = 201)
def create_item(item: ItemCreate):
    new_item = ItemResponse(
        id = len(items_db) + 1,
        name = item.name,
        price = item.price
    )
    items_db.append(new_item)
    return new_item

# 一覧取得API
@app.get("/items/", response_model=List[ItemResponse])
def get_items():
    return items_db

# 単体取得API
@app.get("/items/{item_id}", response_model=ItemResponse)
def get_item(item_id: int):
    for item in items_db:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

# 削除API
@app.delete("/item/{item_id}", status_code=204)
def delete_item(item_id: int):
    for index, item in enumerate(items_db):
        if item.id == item_id:
            items_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Item not found")
