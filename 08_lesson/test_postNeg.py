import requests
from urllib.parse import urljoin


def test_create_project_negative_missing_name():
    # Негативный тест создания проекта без имени
    
    base_url = 'http://your-api-url.com'
    endpoint = '/api-v2/projects/'
    full_url = urljoin(base_url, endpoint)
    
    data = {
        "description": "Project without name"
    }
    
    response = requests.post(full_url, json=data)
    
    assert response.status_code == 400
    assert "errors" in response.json()
