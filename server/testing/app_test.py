def test_index(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json == {"message": "Welcome to the Pizza API!"}
