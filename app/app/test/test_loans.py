from datetime import datetime, timedelta

def test_index(client):
    response = client.get('/Loan/')
    assert response.status_code == 200
    assert b"Lista de Pr" in response.data

def test_add_loan(client, book, user):
    response = client.post('/Loan/add', data={
        'bookId': book.idBook,
        'userId': user.idUser
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"test_book" in response.data
    assert b"test_user" in response.data

def test_edit_loan(client, loan):
    response = client.post(f'/Loan/edit/{loan.idLoan}', data={
        'returnDate': '2030-01-01',
        'fine': '5.0',
        'status': 'Updated'
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Updated" in response.data
    assert b"2030-01-01" in response.data

def test_return_loan(client, loan):
    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b"Returned" in response.data

def test_return_loan_late_fine(client, app, loan):
    from app import db
    from app.models.loans import Loan
    loan.returnDate = datetime.now() - timedelta(days=3, hours=1)
    db.session.commit()

    response = client.get(f'/Loan/return/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert db.session.get(Loan, loan.idLoan).fine == 3.0

def test_delete_loan(client, loan):
    response = client.get(f'/Loan/delete/{loan.idLoan}', follow_redirects=True)
    assert response.status_code == 200
    assert b"test_book" not in response.data
