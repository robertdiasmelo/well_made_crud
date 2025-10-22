from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fast_zero.schemas import Message

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/hello', status_code=HTTPStatus.OK, response_class=HTMLResponse)
def say_hello():
    return """
    <html>
      <head>
        <title> Hello FastAPI! </title>
      </head>
      <body>
        <h1> Hello FastAPI! </h1>
      </body>
    </html>
    """
    
