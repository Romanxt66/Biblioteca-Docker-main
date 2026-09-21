def test_index(client):
    response = client.get('/Author/')
    assert response.status_code == 200
    assert b"Lista de Autores" in response.data

def test_add_author(client):
    response = client.post('/Author/add', data={
        'nameAuthor': 'new_author',
        'nationalityAuthor': 'new_nationality'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"new_author" in response.data

def test_edit_author(client, author):
    response = client.post(f'/Author/edit/{author.idAuthor}', data={
        'nameAuthor': 'updated_author',
        'nationalityAuthor': 'updated_nationality'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"updated_author" in response.data

def test_list_author_books(client, author, book):
    response = client.get(f'/Author/list/{author.idAuthor}')
    assert response.status_code == 200
    assert b"test_book" in response.data

def test_delete_author(client, author):
    response = client.get(f'/Author/delete/{author.idAuthor}', follow_redirects=True)
    assert response.status_code == 200
    assert b"test_author" not in response.data
