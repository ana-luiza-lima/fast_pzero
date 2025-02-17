from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_pzero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)        # Arrange (organização do teste)
    response = client.get('/')          # Act (ação do teste)
    assert response.status_code == HTTPStatus.OK  # Assert (verificação)
    assert response.json() == {'message': 'TESTANDO!'}
