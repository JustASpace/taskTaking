from conftest import async_session_maker, client


def test_register():
    response = client.post('/auth/register', json={
        "email": "teacher",
        "password": "teacher",
        "is_active": True,
        "is_superuser": False,
        "is_verified": False,
        "username": "teacher",
        "role_id": 1,
        "invited_by": ""
    })

    assert response.status_code == 201, "Unable to create teacher"
