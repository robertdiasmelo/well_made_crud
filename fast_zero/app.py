from fastapi import FastAPI  # pyright: ignore[reportMissingImports]

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Hello World'}
