def test_index(client):
    response = client.get('/room/')
    assert response.status_code == 200
    assert b"Lista de Salas" in response.data

def test_add_room(client):
    response = client.post('/room/add', data={
        'name': 'new_room',
        'description': 'new_description'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"new_room" in response.data

def test_edit_room(client, room):
    response = client.post(f'/room/edit/{room.id}', data={
        'name': 'updated_room',
        'description': 'updated_description'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"updated_room" in response.data

def test_delete_room(client, room):
    response = client.get(f'/room/delete/{room.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b"test_room" not in response.data
