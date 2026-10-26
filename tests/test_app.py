from app import app

def test_saved_map_is_served():
    with app.test_client() as client:
        response=client.get("/")
        assert response.status_code == 200
        assert b"leaflet" in response.data.lower()
