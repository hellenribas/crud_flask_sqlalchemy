from httpx import get, post

def testa_rota_get_proprietarios():
    request = get('http://localhost:5100/proprietarios')
    assert request.status_code == 200, 'Código diferente de 200'

def testa_rota_get_carros():
    request = get('http://localhost:5100/carros')
    assert request.status_code == 200, 'Código diferente de 200'

def testa_rota_get_proprietario_id(id=1):
    request = get(f'http://localhost:5100/proprietario/{id}')
    assert request.status_code == 200, 'Código diferente de 200'

def testa_rota_get_carro_id_fail(id=1):
    request = get(f'http://localhost:5100/carro/{id}')
    assert request.status_code == 404, 'Código diferente de 404'

def testa_rota_post_proprietarios_success():
    json = { "nome": "proprietario3", "oportunidade_venda": 1 }
    request = post('http://localhost:5100/cadastro', json=json)
    assert request.status_code == 200, 'Código diferente de 200'

def testa_rota_post_proprietarios_fail():
    json = { "oportunidade_venda": 1 }
    request = post('http://localhost:5100/cadastro', json=json)
    assert request.status_code == 404, 'Código diferente de 404'