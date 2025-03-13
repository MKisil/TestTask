import json


def test_create_user(client):
    user_data = {
        "name": "John Doe",
        "email": "john@example.com"
    }

    response = client.post(
        '/users',
        data=json.dumps(user_data),
        content_type='application/json'
    )

    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['message'] == 'User created successfully'
    assert data['user']['name'] == user_data['name']
    assert data['user']['email'] == user_data['email']


def test_create_user_invalid_data(client):
    user_data = {
        "name": ""
    }

    response = client.post(
        '/users',
        data=json.dumps(user_data),
        content_type='application/json'
    )

    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data


def test_get_all_users(client, init_database):
    response = client.get('/users')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert len(data['users']) == 2


def test_get_user(client, init_database):
    response = client.get('/users/1')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['user']['id'] == 1
    assert data['user']['name'] == "Test User 1"
    assert data['user']['email'] == "test1@example.com"


def test_get_user_not_found(client):
    response = client.get('/users/999')

    assert response.status_code == 404
    data = json.loads(response.data)
    assert data['error'] == 'User not found'


def test_update_user(client, init_database):
    update_data = {
        "name": "Updated Name",
        "email": "updated@example.com"
    }

    response = client.put(
        '/users/1',
        data=json.dumps(update_data),
        content_type='application/json'
    )

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'User updated successfully'
    assert data['user']['name'] == update_data['name']
    assert data['user']['email'] == update_data['email']


def test_delete_user(client, init_database):
    response = client.delete('/users/1')

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data['message'] == 'User deleted successfully'

    response = client.get('/users/1')
    assert response.status_code == 404
