from fastapi import Depends, FastAPI

app = FastAPI()

def common_query():
    return {"message": "共通処理が実行された"}

@app.get("/items/")
# Dependsを使用して、共通処理を実行する関数を指定する。
def read_items(info: dict = Depends(common_query)):
    return {
        "info": info,
        "data": ["apple", "banana"]
    }