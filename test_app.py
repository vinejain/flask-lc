import pytest
from flask_lc import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_line_chart(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Line Chart' in response.data
    assert b'myChart' in response.data  # Check if canvas element exists

