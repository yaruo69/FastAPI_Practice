from fastapi import FastAPI

app = FastAPI();

# デコレーターを使用して、HTTP GETリクエストを受け取るメソッド
# FastAPIがこの関数を「APIとして登録」している。
@app.get("/")
# def => pythonの関数を定義するキーワード
# read_root => 関数の名前
def read_root():
    # FastAPIは、戻り値をJSON形式に変換してレスポンスする。
    return {"message": "Hello Phase2"}