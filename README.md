# Phase2 FastAPI アプリケーション

このリポジトリには、シンプルな FastAPI アプリケーションが含まれており、基本的な HTTP GET エンドポイントを示しています。

## ファイル構成

- `main.py`: FastAPI アプリケーションと単一のルートが含まれています。

## アプリケーションの実行手順

1. **仮想環境を作成して有効化**（まだであれば）:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **依存関係をインストール**:

   ```bash
   pip install fastapi uvicorn
   ```

3. **サーバーを起動**:

   ```bash
   uvicorn main:app --reload
   ```

   - `main` は拡張子 `.py` を除いた Python ファイル名を指します。
   - `app` はそのファイル内の FastAPI インスタンスです。
   - `--reload` は開発用ホットリロードを有効にします。

4. **エンドポイントにアクセス**:
   ブラウザで [http://127.0.0.1:8000/](http://127.0.0.1:8000/) にアクセスします。
   以下の JSON レスポンスが表示されるはずです:

   ```json
   { "message": "Hello Phase2" }
   ```

5. **インタラクティブな API ドキュメント**:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## 補足

- エンドポイントを追加するには `main.py` を編集してください。
- FastAPI はコードや型ヒントに基づいてドキュメントを自動生成します。

FastAPI での開発をお楽しみください！
