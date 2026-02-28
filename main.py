from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI();

# PydanticのBaseModelを継承して、リクエストボディのデータモデルを定義する。
# BaseModelを継承することで、FastAPIは自動的にデータのバリデーションやシリアライズを行うことができる。
class Item(BaseModel):
    name: str
    price: int

# デコレーターを使用して、HTTP GETリクエストを受け取るメソッド
# FastAPIがこの関数を「APIとして登録」している。
@app.get("/")
# def => pythonの関数を定義するキーワード
# read_root => 関数の名前
def read_root():
    # FastAPIは、戻り値をJSON形式に変換してレスポンスする。
    return {"message": "Hello Phase2"}

# パスパラメータを使用して、URLの一部を変数として受け取ることができる。
# 引数に型指定をすることで、FastAPIがバリデーションを行う。
@app.get("/users/{user_id}")
def read_user(user_id: int):
    return {"user_id": user_id}

# クエリパラメータを使用して、URLのクエリ部分から値を受け取ることができる。
@app.get("/items/")
def read_item(name:str, price:int):
    return {"name": name, "price": price}

# postリクエストを受け取るためのエンドポイントを定義する。
@app.post("/items/")
# Itemクラスを引数に取る関数を定義することで、FastAPIはリクエストボディからJSONをパースして、Itemクラスのインスタンスを作成する。
def create_item(item: Item):
    return {"received": item}