from corona import create_app
# Test case for the home page.
def test_home(client):
    response = client.get('/')
    assert b'COVID-19 Tracker' in response.data
    assert response.status_code == 200
