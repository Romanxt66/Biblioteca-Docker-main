def test_index(client):
    response = client.get('/computers/')
    assert response.status_code == 200
    assert b"Lista de Computadoras" in response.data

def test_add_computer(client):
    response = client.post('/computers/add', data={
        'brandComputer': 'new_brand',
        'modelComputer': 'new_model',
        'statusComputer': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"new_brand" in response.data

def test_update_computer(client, computer):
    response = client.post(f'/computers/update/{computer.idComputer}', data={
        'brandComputer': 'updated_brand',
        'modelComputer': 'updated_model',
        'statusComputer': 'Inactive'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"updated_brand" in response.data

def test_delete_computer(client, computer):
    response = client.post(f'/computers/delete/{computer.idComputer}', follow_redirects=True)
    assert response.status_code == 200
    assert b"test_brand" not in response.data
