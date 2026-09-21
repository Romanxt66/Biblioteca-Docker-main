def test_index(client):
    response = client.get('/cloans/')
    assert response.status_code == 200
    assert b"Lista de Pr" in response.data

def test_add_computer_loan(client, computer, user):
    response = client.post('/cloans/add', data={
        'computerId': computer.idComputer,
        'userId': user.idUser,
        'status': 'Active'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Active" in response.data

def test_edit_computer_loan(client, computer_loan, computer, user):
    response = client.post(f'/cloans/update/{computer_loan.idLoan}', data={
        'computerId': computer.idComputer,
        'userId': user.idUser,
        'loanDate': '2024-01-01',
        'returnDate': '2024-01-15',
        'status': 'Updated'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated" in response.data

def test_return_computer_loan(client, computer_loan):
    response = client.post(f'/cloans/return/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Returned" in response.data

def test_delete_computer_loan(client, computer_loan):
    response = client.post(f'/cloans/delete/{computer_loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Active" not in response.data
