
def test_welcome(client):
    """
    Test the '/' route to ensure it returns 'api working'.
    """
    response = client.get('/')
    assert response.status_code == 200
    assert response.json == {'status': 'api working'}


def test_store_and_load_data(client):
    """
    Test storing and loading data from the database.
    """
    # Reset the database to ensure it's empty
    client.get('/reset')

    # Store some data
    data = {'context': 'Test context'}
    response = client.post('/store', json=data)
    assert response.status_code == 201

    # Load the data and check if it exists
    response = client.get('/load')
    assert response.status_code == 200
    assert len(response.json) == 1
    assert response.json[0]['context'] == 'Test context'


def test_reset_database(client):
    """
    Test resetting the database.
    """
    # Store some data to ensure the database is not empty
    data = {'context': 'Test context'}
    client.post('/store', json=data)

    # Reset the database
    response = client.get('/reset')

    # Verify the response
    assert response.status_code == 200
    assert 'Successfully deleted' in response.json['message']
