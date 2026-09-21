def test_index(client):
    response = client.get('/Book/')
    assert response.status_code == 200
    assert b"Lista de Libros" in response.data

def test_add_book(client, author):
    response = client.post('/Book/add', data={
        'titleBook': 'new_book',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"new_book" in response.data

def test_edit_book(client, book, author):
    response = client.post(f'/Book/edit/{book.idBook}', data={
        'titleBook': 'updated_book',
        'authorId': author.idAuthor
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"updated_book" in response.data

def test_delete_book(client, book):
    response = client.get(f'/Book/delete/{book.idBook}', follow_redirects=True)
    assert response.status_code == 200
    assert b"test_book" not in response.data
