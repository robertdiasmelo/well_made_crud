from http import HTTPStatus

from fastapi.testclient import (  # pyright: ignore[reportMissingImports]
    TestClient,
)

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Hello World'}


def test_hello_deve_retornar_hello_fastapi():
    client = TestClient(app)
    response = client.get('/hello')
    assert response.status_code == HTTPStatus.OK
    assert '<h1> Hello FastAPI! </h1>' in response.text
